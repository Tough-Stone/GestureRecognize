# -*- coding: utf-8 -*-
import sys
import threading

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from MainWindow import *
from MakeImage import *
from StartRecognize_Controller import MyStartRecognize
from Train import train


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.train_path = None
        self.test_path = None

    def initUI(self):
        # 给按钮连接槽函数
        self.pushButton_MakeTrain.clicked.connect(self.getTrain)  # 录制训练集
        self.pushButton_MakeTest.clicked.connect(self.getTest)  # 录制测试集
        self.pushButton_ChooseTrain.clicked.connect(self.importTrain)  # 导入训练集
        self.pushButton_ChooseTest.clicked.connect(self.importTest)  # 导入测试集
        self.pushButton_TrainModel.clicked.connect(self.train)  # 模型训练
        self.pushButton_StartUse.clicked.connect(self.start)  # 开始识别
        self.pushButton_Tips.clicked.connect(self.tips)  # 提示窗

    def getTrain(self):
        makeTrain()

    def getTest(self):
        makeTest()

    def importTrain(self):
        self.train_path = QFileDialog.getExistingDirectory(self, "选择训练集存储路径") + '/'
        print(self.train_path)
        if self.train_path and self.test_path:
            self.pushButton_TrainModel.setText('模型训练')

    def importTest(self):
        self.test_path = QFileDialog.getExistingDirectory(self, "选择测试集存储路径") + '/'
        print(self.test_path)
        if self.train_path and self.test_path:
            self.pushButton_TrainModel.setText('模型训练')

    def train(self):
        if not self.train_path and not self.test_path:
            QMessageBox.information(self, "提示", "请先选择训练集\n和测试集存储路径。")
        elif not self.train_path:
            QMessageBox.information(self, "提示", "请先选择训练集存储路径。")
        elif not self.test_path:
            QMessageBox.information(self, "提示", "请先选择测试集存储路径。")
        else:
            self.pushButton_TrainModel.setEnabled(False)
            self.pushButton_TrainModel.setText('模型训练中')
            th1 = threading.Thread(target=self.thread_train)  # # 创建线程
            th1.start()

    def thread_train(self):
        train(self.train_path)
        self.pushButton_TrainModel.setText('模型训练完成')
        self.pushButton_TrainModel.setEnabled(True)


    def start(self):
        self.form_StartRecognize = QtWidgets.QWidget()
        self.ui_StartRecognize = MyStartRecognize()
        self.ui_StartRecognize.setupUi(self.form_StartRecognize)
        self.ui_StartRecognize.initUI()
        self.form_StartRecognize.show()

    def tips(self):
        QMessageBox.information(self, "操作提示",
                                "录制数据集：修改存放路径后，手势放在摄像头前，坚持一段时间。\n"
                                "导入数据集：导入数据集所在的文件夹。\n"
                                "模型训练：必须录制好数据集后才可以进行，等待至生成图片后即完成训练。\n"
                                "开始识别：必须完成模型训练后才可以进行。")


if __name__ == "__main__":
    app = QApplication(sys.argv)  # sys.argv是一个命令行参数列表
    myWin = MyMainWindow()
    myWin.setObjectName('Window')
    # 给窗口背景上色
    qssStyle = '''
              QPushButton[color='gray']{
              background-color:rgb(205,197,191)
              }
              QPushButton[color='same']{
              background-color:rgb(225,238,238)
              }
              #Window{
              background-color:rgb(162,181,205) 
              }
              '''
    myWin.setStyleSheet(qssStyle)
    myWin.show()
    sys.exit(app.exec_())
