from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class AboutDialog():
    def __init__(self):

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        message = QLabel()
        # https://github.com/lsldragon/AITranslator

        message.setText(
            "<html><a href=\"https://github.com/lsldragon/AITranslator\">https://github.com/lsldragon/AITranslator</a></html>")

        self.dialog = QDialog()
        self.dialog.setMinimumSize(QtCore.QSize(300, 200))
        self.dialog.setMaximumSize(QtCore.QSize(500, 300))
        self.dialog.setWindowTitle("关于")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/about.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)
        self.dialog.resize(450, 100)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)

        self.okBtn = QPushButton("确定")

        message.setFont(font)
        self.okBtn.setFont(font)

        # 绑定事件
        self.okBtn.clicked.connect(self.ok)

        # 确定与取消按钮横向布局
        hbox.addWidget(self.okBtn)

        # 消息label与按钮组合纵向布局
        vbox.addWidget(message)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        # 该模式下，只有该dialog关闭，才可以关闭父界面
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    def ok(self):
        print("确定")
        self.dialog.close()
