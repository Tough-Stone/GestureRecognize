# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_FirstUse = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_FirstUse.setGeometry(QtCore.QRect(90, 169, 250, 251))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.groupBox_FirstUse.setFont(font)
        self.groupBox_FirstUse.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_FirstUse.setFlat(False)
        self.groupBox_FirstUse.setObjectName("groupBox_FirstUse")
        self.pushButton_MakeTrain = QtWidgets.QPushButton(self.groupBox_FirstUse)
        self.pushButton_MakeTrain.setGeometry(QtCore.QRect(50, 40, 161, 41))
        self.pushButton_MakeTrain.setObjectName("pushButton_MakeTrain")
        self.pushButton_ChooseTrain = QtWidgets.QPushButton(self.groupBox_FirstUse)
        self.pushButton_ChooseTrain.setGeometry(QtCore.QRect(50, 140, 161, 41))
        self.pushButton_ChooseTrain.setObjectName("pushButton_ChooseTrain")
        self.pushButton_MakeTest = QtWidgets.QPushButton(self.groupBox_FirstUse)
        self.pushButton_MakeTest.setGeometry(QtCore.QRect(50, 90, 161, 41))
        self.pushButton_MakeTest.setObjectName("pushButton_MakeTest")
        self.pushButton_ChooseTest = QtWidgets.QPushButton(self.groupBox_FirstUse)
        self.pushButton_ChooseTest.setGeometry(QtCore.QRect(50, 190, 161, 41))
        self.pushButton_ChooseTest.setObjectName("pushButton_ChooseTest")
        self.groupBox_AlreadyHas = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_AlreadyHas.setGeometry(QtCore.QRect(440, 170, 250, 181))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.groupBox_AlreadyHas.setFont(font)
        self.groupBox_AlreadyHas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_AlreadyHas.setFlat(False)
        self.groupBox_AlreadyHas.setObjectName("groupBox_AlreadyHas")
        self.pushButton_TrainModel = QtWidgets.QPushButton(self.groupBox_AlreadyHas)
        self.pushButton_TrainModel.setGeometry(QtCore.QRect(50, 40, 161, 41))
        self.pushButton_TrainModel.setObjectName("pushButton_TrainModel")
        self.pushButton_StartUse = QtWidgets.QPushButton(self.groupBox_AlreadyHas)
        self.pushButton_StartUse.setGeometry(QtCore.QRect(50, 110, 161, 41))
        self.pushButton_StartUse.setObjectName("pushButton_StartUse")
        self.label_Welcome = QtWidgets.QLabel(self.centralwidget)
        self.label_Welcome.setGeometry(QtCore.QRect(310, 40, 171, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(20)
        self.label_Welcome.setFont(font)
        self.label_Welcome.setObjectName("label_Welcome")
        self.pushButton_Tips = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Tips.setGeometry(QtCore.QRect(490, 370, 161, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(11)
        self.pushButton_Tips.setFont(font)
        self.pushButton_Tips.setObjectName("pushButton_Tips")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "手势识别系统"))
        self.groupBox_FirstUse.setTitle(_translate("MainWindow", "第一次使用"))
        self.pushButton_MakeTrain.setText(_translate("MainWindow", "录制训练集"))
        self.pushButton_ChooseTrain.setText(_translate("MainWindow", "导入训练集"))
        self.pushButton_MakeTest.setText(_translate("MainWindow", "录制测试集"))
        self.pushButton_ChooseTest.setText(_translate("MainWindow", "导入测试集"))
        self.groupBox_AlreadyHas.setTitle(_translate("MainWindow", "已有数据集"))
        self.pushButton_TrainModel.setText(_translate("MainWindow", "模型训练"))
        self.pushButton_StartUse.setText(_translate("MainWindow", "开始识别"))
        self.label_Welcome.setText(_translate("MainWindow", "手势识别系统"))
        self.pushButton_Tips.setText(_translate("MainWindow", "操作提示"))
