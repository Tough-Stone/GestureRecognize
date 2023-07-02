# -*- coding: utf-8 -*-
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import Qt
from StartRecognize import *
from Utils import *
import time


class MyStartRecognize(QMainWindow, Ui_StartRecognize):
    def __init__(self):
        super(MyStartRecognize, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # 给按钮连接槽函数
        self.pushButton_Get.clicked.connect(self.getGesture)  # 获取手势
        self.pushButton_Recognize.clicked.connect(self.recognize)  # 进行识别
        self.pushButton_Tips.clicked.connect(self.tips)  # 操作提示

    def getGesture(self):
        saveGesture()
        self.label_RecognizeResult.setText("已经将图像保存到本地")
        self.label_RecognizeResult.setAlignment(Qt.AlignCenter)

    def recognize(self):
        self.label_RecognizeResult.setText("正在调用卷积神经网络...")
        self.label_RecognizeResult.setAlignment(Qt.AlignCenter)
        QApplication.processEvents()  # 刷新一下，否则上面的文字不显示
        time_start = time.perf_counter()
        (gesture_num, possibility) = evaluate_one_image()
        time_end = time.perf_counter()
        print("time cost:%.6fs" % (time_end-time_start))
        self.resultShow(gesture_num, possibility)

    def tips(self):
        QMessageBox.information(self, "操作提示",
                                "获取手势：把手势放在摄像头前，可以重新点击以重新获取。")

    def resultShow(self, gesture_num, possibility ):
        label = ['scissors', 'paper', 'rock', 'ok', 'good']
        self.label_RecognizeResult.setText(
            'This is a ' + label[gesture_num-1] + ' with possibility:'+possibility)
        self.label_RecognizeResult.setAutoFillBackground(True)  # 允许上色
        palette = QPalette()  # palette 调色板
        palette.setColor(QPalette.Window, Qt.lightGray)
        self.label_RecognizeResult.setPalette(palette)
        self.label_ImageResult.setToolTip("This is a" + label[gesture_num-1])
        self.label_ImageResult.setPixmap(QPixmap('./ges_ico/ges' + str(gesture_num) + '.ico'))
        self.label_RecognizeResult.setAlignment(Qt.AlignCenter)
        self.label_ImageResult.setAlignment(Qt.AlignCenter)
