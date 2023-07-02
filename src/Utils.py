# -*- coding: utf-8 -*-
import cv2
from PIL import Image
import Train_inputdata
import Train_model
import numpy as np
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()


def saveGesture():
    """
    原始图像的大小为（480,640,3）
    保存的图像是切割后的图像（400,400,3）
    """
    cameraCapture = cv2.VideoCapture(0)
    success, frame = cameraCapture.read()
    if success is True:
        cv2.imwrite("./data/testImage/test.jpg", frame)

    testImg = cv2.imread('./data/testImage/test.jpg')
    print(testImg.shape)  # G7笔记本的摄像头是（480，640,3） 高度，宽度，通道数

    img_roi_y = 30
    img_roi_x = 200
    img_roi_height = 350  # [2]设置ROI区域的高度
    img_roi_width = 350  # [3]设置ROI区域的宽度
    img_roi = testImg[img_roi_y:(img_roi_y + img_roi_height), img_roi_x:(img_roi_x + img_roi_width)]

    cv2.imshow("[ROI_Img]", img_roi)
    cv2.imwrite("./data/testImage/roi/" + "img_roi.jpg", img_roi)
    cv2.waitKey(0)
    cv2.destroyWindow("[ROI_Img]")


def get_one_image(train):
    n = len(train)
    ind = np.random.randint(0, n)
    img_dir = train[ind]

    image = Image.open(img_dir)
    image = image.resize([227, 227])
    image = np.array(image)
    return image


def evaluate_one_image():
    """
    Test one image against the saved models and parameters
    返回字符串1~5
    """
    train_dir = '../data/testImage/roi/'
    train, train_label = Train_inputdata.get_files(train_dir)
    image_array = get_one_image(train)

    with tf.Graph().as_default():
        BATCH_SIZE = 1
        N_CLASSES = 5

        image = tf.cast(image_array, tf.float32)
        image = tf.image.per_image_standardization(image)
        image = tf.reshape(image, [1, 227, 227, 3])
        logit = Train_model.cnn_inference(image, BATCH_SIZE, N_CLASSES, keep_prob=1)

        logit = tf.nn.softmax(logit)

        x = tf.placeholder(tf.float32, shape=[227, 227, 3])

        logs_train_dir = '../checkpoint/'

        saver = tf.train.Saver()

        with tf.Session() as sess:

            print("Reading checkpoints...")
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)
            if ckpt and ckpt.model_checkpoint_path:
                global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
                saver.restore(sess, ckpt.model_checkpoint_path)
                print('Loading success, global_step is %s' % global_step)
            else:
                print('No checkpoint file found')

            prediction = sess.run(logit, feed_dict={x: image_array})
            max_index = np.argmax(prediction)
            if max_index == 0:
                print('This is a scissor with possibility %.6f' % prediction[:, 0])
                return 1, '%.6f' % prediction[:, 0]
            elif max_index == 1:
                print('This is a paper with possibility %.6f' % prediction[:, 1])
                return 2, '%.6f' % prediction[:, 1]
            elif max_index == 2:
                print('This is a rock with possibility %.6f' % prediction[:, 2])
                return 3, '%.6f' % prediction[:, 2]
            elif max_index == 3:
                print('This is a ok with possibility %.6f' % prediction[:, 3])
                return 4, '%.6f' % prediction[:, 3]
            elif max_index == 4:
                print('This is a good with possibility %.6f' % prediction[:, 4])
                return 5, '%.6f' % prediction[:, 4]
