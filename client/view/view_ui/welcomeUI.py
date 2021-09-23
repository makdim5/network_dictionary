# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomeUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(500, 400))
        Form.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setPointSize(16)
        Form.setFont(font)
        Form.setWindowTitle("Network DICT")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"      border-radius: 7px;\n"
"    \n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.91, y1:0.897909, x2:0.175, y2:0.113636, stop:0 rgba(18, 74, 148, 255), stop:1 rgba(26, 197, 165, 255));\n"
"}\n"
"QPushButton{\n"
" color: rgb(255, 255, 255);\n"
"  font-size: 16px;\n"
"  font-weight: 700;\n"
"  padding: .25em .5em;\n"
"  outline: none;\n"
"  border: 3px solid rgb(250,172,17);\n"
"  border-radius: 7px;\n"
" \n"
"    background-color: rgb(19, 154, 127);\n"
"\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 30, 271, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 22pt \"MV Boli\";\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 300, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 141, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/logo.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.warningMsg = QtWidgets.QLabel(Form)
        self.warningMsg.setGeometry(QtCore.QRect(130, 230, 231, 78))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.warningMsg.setFont(font)
        self.warningMsg.setStyleSheet("color: rgb(255, 255, 65);\n"
"font: 16pt \"MV Boli\";\n"
"")
        self.warningMsg.setObjectName("warningMsg")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 231, 78))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MV Boli\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(270, 180, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "Добро пожаловать\n"
"в Network DICT!!!"))
        self.pushButton.setText(_translate("Form", "ok"))
        self.warningMsg.setText(_translate("Form", "Сервер не найден!!!"))
        self.label_2.setText(_translate("Form", "Введите DNS сервера:"))
import client.view.images.srce