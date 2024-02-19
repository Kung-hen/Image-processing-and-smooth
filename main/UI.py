# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(731, 359)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(15)
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Button_separation = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_separation.setFont(font)
        self.Button_separation.setObjectName("Button_separation")
        self.verticalLayout_2.addWidget(self.Button_separation)
        self.Button_transformation = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_transformation.setFont(font)
        self.Button_transformation.setObjectName("Button_transformation")
        self.verticalLayout_2.addWidget(self.Button_transformation)
        self.Button_Detection = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_Detection.setFont(font)
        self.Button_Detection.setObjectName("Button_Detection")
        self.verticalLayout_2.addWidget(self.Button_Detection)
        self.Button_Blend = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_Blend.setFont(font)
        self.Button_Blend.setObjectName("Button_Blend")
        self.verticalLayout_2.addWidget(self.Button_Blend)
        self.gridLayout.addWidget(self.frame, 1, 2, 9, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Button_Gaussian = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_Gaussian.setFont(font)
        self.Button_Gaussian.setObjectName("Button_Gaussian")
        self.verticalLayout_3.addWidget(self.Button_Gaussian)
        self.Button_Bilateral = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_Bilateral.setFont(font)
        self.Button_Bilateral.setObjectName("Button_Bilateral")
        self.verticalLayout_3.addWidget(self.Button_Bilateral)
        self.Button_Median = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(".New York")
        self.Button_Median.setFont(font)
        self.Button_Median.setObjectName("Button_Median")
        self.verticalLayout_3.addWidget(self.Button_Median)
        self.gridLayout.addWidget(self.frame_2, 1, 3, 9, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Computer Vision Image Processing"))
        self.Button_separation.setText(
            _translate("Form", "1.1 Color Separation"))
        self.Button_transformation.setText(
            _translate("Form", "1.2 Color Transformation"))
        self.Button_Detection.setText(
            _translate("Form", "1.3 Color Detection"))
        self.Button_Blend.setText(_translate("Form", "1.4 Blending"))
        self.Button_Gaussian.setText(_translate("Form", "2.1 Gaussian Blur"))
        self.Button_Bilateral.setText(
            _translate("Form", "2.2 Bilateral fliter"))
        self.Button_Median.setText(_translate("Form", "2.3 Median fliter"))
        self.label_4.setText(_translate("Form", "2. Image Smoothing"))
        self.label_3.setText(_translate("Form", "1. Image Processing"))
        self.label.setText(_translate("Form", "No image loaded"))
        self.pushButton.setText(_translate("Form", "Load image 1"))
        self.pushButton_2.setText(_translate("Form", "Load image 2"))
        self.label_2.setText(_translate("Form", "No image loaded"))
