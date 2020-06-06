from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


class AboutDialog():
    def __init__(self):

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        message = QLabel()
        text = """
        <html>
            <h2>软件开源地址</h2></br><a href=\"https://github.com/lsldragon/AITranslator\">https://github.com/lsldragon/AITranslator</a>
            <h3>作者: Lee SL</h3></br>
        </html>
        """
        message.setText(text)

        self.dialog = QDialog()
        self.dialog.setMinimumSize(QtCore.QSize(375, 200))
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

        self.okBtn.clicked.connect(self.ok)

        hbox.addWidget(self.okBtn)

        vbox.addWidget(message)
        vbox.addLayout(hbox)
        self.dialog.setLayout(vbox)

        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.exec_()

    def ok(self):
        self.dialog.close()
