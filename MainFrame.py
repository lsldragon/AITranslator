# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainFrame.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1135, 745)
        MainWindow.setMinimumSize(QtCore.QSize(550, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        MainWindow.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.clear_button.setFont(font)
        self.clear_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/clear.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon1)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout_5.addWidget(self.clear_button)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.search_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_edit.sizePolicy().hasHeightForWidth())
        self.search_edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.search_edit.setFont(font)
        self.search_edit.setObjectName("search_edit")
        self.verticalLayout.addWidget(self.search_edit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 155, 656))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.theme_comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.theme_comboBox.setFont(font)
        self.theme_comboBox.setObjectName("theme_comboBox")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.theme_comboBox.addItem("")
        self.verticalLayout_4.addWidget(self.theme_comboBox)
        self.AI_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AI_button.sizePolicy().hasHeightForWidth())
        self.AI_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.AI_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/AI.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AI_button.setIcon(icon2)
        self.AI_button.setObjectName("AI_button")
        self.verticalLayout_4.addWidget(self.AI_button)
        self.google_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.google_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/google.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.google_button.setIcon(icon3)
        self.google_button.setObjectName("google_button")
        self.verticalLayout_4.addWidget(self.google_button)
        self.youDaoButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.youDaoButton.sizePolicy().hasHeightForWidth())
        self.youDaoButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.youDaoButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/youdao.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.youDaoButton.setIcon(icon4)
        self.youDaoButton.setObjectName("youDaoButton")
        self.verticalLayout_4.addWidget(self.youDaoButton)
        self.bingButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.bingButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/images/bing.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bingButton.setIcon(icon5)
        self.bingButton.setIconSize(QtCore.QSize(16, 16))
        self.bingButton.setObjectName("bingButton")
        self.verticalLayout_4.addWidget(self.bingButton)
        self.about_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.about_button.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/images/about.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_button.setIcon(icon6)
        self.about_button.setObjectName("about_button")
        self.verticalLayout_4.addWidget(self.about_button)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.type_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.type_ComboBox.setFont(font)
        self.type_ComboBox.setEditable(False)
        self.type_ComboBox.setObjectName("type_ComboBox")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.type_ComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.type_ComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.result_edit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro")
        font.setPointSize(12)
        self.result_edit.setFont(font)
        self.result_edit.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.result_edit.setObjectName("result_edit")
        self.verticalLayout_2.addWidget(self.result_edit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.poem_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.poem_label.setFont(font)
        self.poem_label.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.poem_label.setAlignment(QtCore.Qt.AlignCenter)
        self.poem_label.setObjectName("poem_label")
        self.horizontalLayout.addWidget(self.poem_label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AITranslator  v1.22"))
        self.label_2.setText(_translate("MainWindow", "源语言(自动检测)"))
        self.theme_comboBox.setItemText(0, _translate("MainWindow", "酷黑"))
        self.theme_comboBox.setItemText(1, _translate("MainWindow", "炫白"))
        self.theme_comboBox.setItemText(2, _translate("MainWindow", "系统"))
        self.theme_comboBox.setItemText(3, _translate("MainWindow", "自定义"))
        self.AI_button.setText(_translate("MainWindow", "AI 翻译"))
        self.google_button.setText(_translate("MainWindow", "Google 翻译"))
        self.youDaoButton.setText(_translate("MainWindow", "有道查词"))
        self.bingButton.setText(_translate("MainWindow", "Bing 词典"))
        self.about_button.setText(_translate("MainWindow", "关于"))
        self.label.setText(_translate("MainWindow", "目标语:"))
        self.type_ComboBox.setCurrentText(_translate("MainWindow", "汉语"))
        self.type_ComboBox.setItemText(0, _translate("MainWindow", "汉语"))
        self.type_ComboBox.setItemText(1, _translate("MainWindow", "英语"))
        self.type_ComboBox.setItemText(2, _translate("MainWindow", "文言文"))
        self.type_ComboBox.setItemText(3, _translate("MainWindow", "日语"))
        self.type_ComboBox.setItemText(4, _translate("MainWindow", "韩语"))
        self.type_ComboBox.setItemText(5, _translate("MainWindow", "法语"))
        self.type_ComboBox.setItemText(6, _translate("MainWindow", "西班牙语"))
        self.type_ComboBox.setItemText(7, _translate("MainWindow", "泰语"))
        self.type_ComboBox.setItemText(8, _translate("MainWindow", "俄语"))
        self.type_ComboBox.setItemText(9, _translate("MainWindow", "德语"))
        self.poem_label.setText(_translate("MainWindow", "每日一句"))
import res_rc
