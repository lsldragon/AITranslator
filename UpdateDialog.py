from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class UpdateDialog():
    def __init__(self):

        VERSION = 1.0

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        message = QLabel()
        message.setText("暂无更新")

        self.dialog = QDialog()
        self.dialog.setWindowTitle("检查更新")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/update.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)
        self.dialog.resize(450, 100)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)

        self.okBtn = QPushButton("确定")
        self.cancelBtn = QPushButton("取消")

        message.setFont(font)
        self.okBtn.setFont(font)
        self.cancelBtn.setFont(font)

        # 绑定事件
        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        # 确定与取消按钮横向布局
        hbox.addWidget(self.okBtn)
        hbox.addWidget(self.cancelBtn)

        # 消息label与按钮组合纵向布局
        vbox.addWidget(message)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        # 该模式下，只有该dialog关闭，才可以关闭父界面
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    # 槽函数如下：
    def ok(self):
        print("确定")
        self.dialog.close()

    def cancel(self):
        print("取消")
        self.dialog.close()