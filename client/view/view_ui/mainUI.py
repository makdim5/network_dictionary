# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(771, 550)
        Form.setMinimumSize(QtCore.QSize(500, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
" background-color: rgb(255, 255, 255);\n"
"border : 0;\n"
"color: black;\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit{  \n"
"    \n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pages_bar = QtWidgets.QFrame(Form)
        self.pages_bar.setMinimumSize(QtCore.QSize(0, 40))
        self.pages_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pages_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pages_bar.setObjectName("pages_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pages_bar)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.allPageBtn = QtWidgets.QPushButton(self.pages_bar)
        self.allPageBtn.setStyleSheet("background-color: rgb(202, 212, 255);")
        self.allPageBtn.setObjectName("allPageBtn")
        self.horizontalLayout_2.addWidget(self.allPageBtn)
        self.searchPageBtn = QtWidgets.QPushButton(self.pages_bar)
        self.searchPageBtn.setObjectName("searchPageBtn")
        self.horizontalLayout_2.addWidget(self.searchPageBtn)
        self.aboutPageBtn = QtWidgets.QPushButton(self.pages_bar)
        self.aboutPageBtn.setObjectName("aboutPageBtn")
        self.horizontalLayout_2.addWidget(self.aboutPageBtn)
        self.verticalLayout.addWidget(self.pages_bar)
        self.pages_frame = QtWidgets.QFrame(Form)
        self.pages_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pages_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pages_frame.setObjectName("pages_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pages_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pagesWGT = QtWidgets.QStackedWidget(self.pages_frame)
        self.pagesWGT.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pagesWGT.setObjectName("pagesWGT")
        self.allWordPage = QtWidgets.QWidget()
        self.allWordPage.setObjectName("allWordPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.allWordPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtWidgets.QScrollArea(self.allWordPage)
        self.scrollArea.setStyleSheet("#allWordsWGT{\n"
"background-color:qlineargradient(spread:pad, x1:0.0795455, y1:0.045, x2:1, y2:1, stop:0.0965909 rgba(93, 196, 205, 255), stop:1 rgba(205, 255, 255, 255));\n"
"\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.allWordsWGT = QtWidgets.QWidget()
        self.allWordsWGT.setGeometry(QtCore.QRect(0, 0, 747, 436))
        self.allWordsWGT.setObjectName("allWordsWGT")
        self.allWordsLay = QtWidgets.QVBoxLayout(self.allWordsWGT)
        self.allWordsLay.setContentsMargins(60, 0, 60, 0)
        self.allWordsLay.setSpacing(20)
        self.allWordsLay.setObjectName("allWordsLay")
        self.scrollArea.setWidget(self.allWordsWGT)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.frame = QtWidgets.QFrame(self.allWordPage)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addWordBtn = QtWidgets.QPushButton(self.frame)
        self.addWordBtn.setStyleSheet("background-color: rgb(196, 237, 255);\n"
"border-radious:10px;")
        self.addWordBtn.setObjectName("addWordBtn")
        self.horizontalLayout_3.addWidget(self.addWordBtn)
        self.sortBtn = QtWidgets.QPushButton(self.frame)
        self.sortBtn.setStyleSheet("background-color: rgb(196, 237, 255);\n"
"border-radious:10px;")
        self.sortBtn.setObjectName("sortBtn")
        self.horizontalLayout_3.addWidget(self.sortBtn)
        self.verticalLayout_5.addWidget(self.frame)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.pagesWGT.addWidget(self.allWordPage)
        self.searchPage = QtWidgets.QWidget()
        self.searchPage.setObjectName("searchPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.searchPage)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_frame = QtWidgets.QFrame(self.searchPage)
        self.search_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.search_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.search_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.searchLineLay = QtWidgets.QHBoxLayout(self.search_frame)
        self.searchLineLay.setContentsMargins(0, 0, 0, 0)
        self.searchLineLay.setSpacing(0)
        self.searchLineLay.setObjectName("searchLineLay")
        self.logo = QtWidgets.QLabel(self.search_frame)
        self.logo.setMaximumSize(QtCore.QSize(200, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/newPrefix/изображение_viber_2021-04-25_17-03-24.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.searchLineLay.addWidget(self.logo)
        self.lineEdit = QtWidgets.QLineEdit(self.search_frame)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.searchLineLay.addWidget(self.lineEdit)
        self.searchBtn = QtWidgets.QPushButton(self.search_frame)
        self.searchBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/лупа.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon1)
        self.searchBtn.setIconSize(QtCore.QSize(25, 25))
        self.searchBtn.setObjectName("searchBtn")
        self.searchLineLay.addWidget(self.searchBtn)
        self.verticalLayout_2.addWidget(self.search_frame)
        self.lay2 = QtWidgets.QVBoxLayout()
        self.lay2.setContentsMargins(0, -1, 0, -1)
        self.lay2.setSpacing(0)
        self.lay2.setObjectName("lay2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.searchPage)
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.searchWordsWGT = QtWidgets.QWidget()
        self.searchWordsWGT.setGeometry(QtCore.QRect(0, 0, 765, 395))
        self.searchWordsWGT.setStyleSheet("#searchWordsWGT{\n"
"background-color:qlineargradient(spread:pad, x1:0.0795455, y1:0.045, x2:1, y2:1, stop:0.0965909 rgba(93, 196, 205, 255), stop:1 rgba(205, 255, 255, 255));\n"
"}")
        self.searchWordsWGT.setObjectName("searchWordsWGT")
        self.searchWLay = QtWidgets.QVBoxLayout(self.searchWordsWGT)
        self.searchWLay.setContentsMargins(60, 0, 60, 0)
        self.searchWLay.setSpacing(20)
        self.searchWLay.setObjectName("searchWLay")
        self.scrollArea_2.setWidget(self.searchWordsWGT)
        self.lay2.addWidget(self.scrollArea_2)
        self.verticalLayout_2.addLayout(self.lay2)
        self.pagesWGT.addWidget(self.searchPage)
        self.aboutPage = QtWidgets.QWidget()
        self.aboutPage.setObjectName("aboutPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.aboutPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.aboutPage)
        self.label_3.setMinimumSize(QtCore.QSize(0, 200))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.aboutPage)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/изображение_viber_2021-04-25_17-03-24.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pagesWGT.addWidget(self.aboutPage)
        self.horizontalLayout.addWidget(self.pagesWGT)
        self.verticalLayout.addWidget(self.pages_frame)

        self.retranslateUi(Form)
        self.pagesWGT.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Network DICT"))
        self.allPageBtn.setText(_translate("Form", "Все слова"))
        self.searchPageBtn.setText(_translate("Form", "Поиск"))
        self.aboutPageBtn.setText(_translate("Form", "О программе"))
        self.addWordBtn.setText(_translate("Form", "Добавить слово"))
        self.sortBtn.setText(_translate("Form", "Обновить список "))
        self.label_3.setText(_translate("Form", "Программу разработал\n"
"студент группы 10701119\n"
"Маканов Дмитрий\n"
"\n"
"Минск, БНТУ, 2021"))
import client.view.images.srce