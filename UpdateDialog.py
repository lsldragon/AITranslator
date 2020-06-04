from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices


class UpdateDialog():
    def __init__(self, text):

        self.text = text

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        message = QLabel()
        message.setText(self.text)
        message.setWordWrap(True)

        self.dialog = QDialog()
        self.dialog.setWindowTitle("检查更新")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/update.ico"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialog.setWindowIcon(icon)
        # self.dialog.resize(450, 100)
        self.dialog.setFixedSize(450, 450)

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)

        self.okBtn = QPushButton("下载")
        self.cancelBtn = QPushButton("取消")

        message.setFont(font)
        self.okBtn.setFont(font)
        self.cancelBtn.setFont(font)

        self.okBtn.clicked.connect(self.ok)
        self.cancelBtn.clicked.connect(self.cancel)

        hbox.addWidget(self.okBtn)
        hbox.addWidget(self.cancelBtn)

        vbox.addWidget(message)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    def ok(self):
        QDesktopServices().openUrl(
            QUrl("https://github.com/lsldragon/AITranslator/releases"))
        self.dialog.close()

    def cancel(self):
        self.dialog.close()
