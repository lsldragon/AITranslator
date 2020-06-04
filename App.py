import sys
from PyQt5.QtWidgets import *
from MainFrame import *
import json
import requests
from urllib import parse
from PyQt5.QtCore import *
from GetSource import *
import time
import threading
from googletrans import Translator
from AboutDialog import *

from UpdateDialog import *
import qdarkstyle

GTransData = ""
AITransData = ""


class APP(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(APP, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.update_label()
        self.AI_button.clicked.connect(self.on_ai_translate)
        self.bingButton.clicked.connect(self.on_bing)
        self.type_ComboBox.currentIndexChanged.connect(
            self.on_comboBox_changed)
        self.youDaoButton.clicked.connect(self.on_yddict)
        self.google_button.clicked.connect(self.on_google_translate)
        self.about_button.clicked.connect(self.show_about_dialog)

    def show_about_dialog(self):
        about_dialog = AboutDialog()

    def check_update(self):
        dialog = UpdateDialog()

    def on_google_translate(self):

        self.result_edit.setPlainText("")
        dest = "zh-CN"
        text = self.get_word()
        if text == "":
            self.result_edit.insertHtml(
                "<html><font color=yellow>请输入关键词！！！</font></html>")
            return

        self.t = GTranslator(dest, text)
        self.t.start()
        self.result_edit.setPlaceholderText("......")
        self.t.trigger.connect(self.google_translate)

    def google_translate(self):

        global GTransData
        if GTransData:
            self.result_edit.setPlainText(GTransData)
        else:
            self.result_edit.setPlainText("error")
        GTransData = ""

    def on_jscb(self):

        # self.result_edit.clear()
        # url = "http://106.12.179.253:8089/lsl/api/jsword?words=apple"
        # json_str = GetSource.get_source_code(url)
        # self.result_edit.insertPlainText(json_str)
        self.result_edit.insertHtml("开发中.......")

    def on_bing(self):

        self.result_edit.clear()
        query_word = self.get_word()
        url = "http://106.12.179.253:8089/lsl/api/bingword?words="

        if query_word == "":
            self.result_edit.insertHtml(
                "<html><font color=yellow>请输入关键词！！！</font></html>")
            return
        try:
            _url = url + query_word
            json_str = GetSource.get_source_code(_url)
            res_list = json.loads(json_str)
            word = res_list['word']
            pronounce = res_list['pronouncList']
            means = res_list['meansList']
            usage = res_list['usageList']
            exampleE = res_list['exampleEList']
            exampleC = res_list['exampleCList']

            self.result_edit.insertHtml(
                "<html><font color=red>" + word + "</font><br></html>")
            for p in pronounce:
                self.result_edit.insertHtml(
                    "<html><font color=yellow>" + p + "<font><br><br></html>")

            self.result_edit.insertHtml(
                "<html><font color=red>" + "释义" + "</font><br></html>")
            for m in means:
                self.result_edit.insertHtml(
                    "<html><font>" + m + "<font><br></html>")

            self.result_edit.insertPlainText("\r\n")
            self.result_edit.insertHtml(
                "<html><font color=red>" + "用法" + "</font><br></html>")
            for u in usage:
                self.result_edit.insertHtml(
                    "<html><font>" + u + "<font><br></html>")

            self.result_edit.insertPlainText("\r\n")
            self.result_edit.insertHtml(
                "<html><font color=red>" + "例句英" + "</font><br></html>")
            for ee in exampleE:
                _index = exampleE.index(ee)
                self.result_edit.insertHtml(
                    "<html><font>" + str(_index+1) + ". "+ee + "<font><br><br></html>")

            self.result_edit.insertPlainText("\r\n")
            self.result_edit.insertHtml(
                "<html><font color=red>" + "例句汉" + "</font><br></html>")
            for ec in exampleC:
                self.result_edit.insertHtml(
                    "<html><font>" + ec + "<font><br></html>")
        except:
            self.result_edit.insertHtml(
                "<html><font color=red> 只支持单词查询！</font></html>")

    def on_yddict(self):

        self.result_edit.clear()
        url = "http://106.12.179.253:8089/lsl/api/ydword?words="
        query_word = self.get_word()

        if query_word == "":
            self.result_edit.insertHtml(
                "<html><font color=yellow>请输入关键词！！！</font></html>")
            return
        try:
            _url = url + query_word
            json_str = GetSource.get_source_code(_url)
            res_list = json.loads(json_str)

            word = res_list['word']
            pronounce = res_list['pronounce']
            means = res_list['means']
            example1 = res_list['example1']
            example2 = res_list['example2']

            self.result_edit.insertHtml(
                "<html><font color=red>" + word + "</font><br></html>")

            for p in pronounce:
                self.result_edit.insertHtml(
                    "<html><font color=yellow>" + p + "  " + "</font></html>")

            self.result_edit.insertHtml("<br>")
            for m in means:
                self.result_edit.insertPlainText(m + "\r\n")

            self.result_edit.insertPlainText("\r\n")
            self.result_edit.insertHtml(
                "<html><font color=red>" + "柯林斯释义" + "</font><br></html>")
            for e1 in example1:
                self.result_edit.insertPlainText(e1 + "\r\n")

            self.result_edit.insertHtml(
                "<html><font color=red>" + "例句" + "</font><br></html>")
            for e2 in example2:
                self.result_edit.insertPlainText(e2 + "\r\n")
            QApplication.processEvents()
        except:
            self.result_edit.insertHtml(
                "<html><font color=red> 只支持单词查询！</font><br></html>")

    def on_comboBox_changed(self):
        self.on_ai_translate()

    def get_word(self):

        _str = self.search_edit.toPlainText()
        return _str

    def get_combox_index(self):
        _index = self.type_ComboBox.currentIndex()
        return _index

    def update_label(self):
        try:
            url = "http://open.iciba.com/dsapi/"
            json_str = GetSource.get_source_code(url)
            note = json.loads(json_str)
            self.poem_label.setText(note['content'])
        except:
            self.poem_label.setText("Something went wrong ... ")

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,
                  (screen.height() - size.height())/2)

    def on_ai_search(self):
        index = self.get_combox_index()
        self.set_result(index)

    def on_ai_translate(self):

        self.result_edit.setPlainText("")
        index = self.get_combox_index()
        dest = ""
        if index == 0:
            dest = "zh"
        elif index == 1:
            dest = "en"
        elif index == 2:
            dest = "wyw"
        elif index == 3:
            dest = "jp"
        elif index == 4:
            dest = "kor"
        elif index == 5:
            dest = "fra"
        elif index == 6:
            dest = "spa"
        elif index == 7:
            dest = "th"
        elif index == 8:
            dest = "ru"
        elif index == 9:
            dest = "de"
        else:
            self.on_yddict()

        text = self.get_word()
        if text == "":
            self.result_edit.insertHtml(
                "<html><font color=yellow>请输入关键词！！！</font></html>")
            return

        self.t = YouDaoTans(dest, text)
        self.t.start()
        self.result_edit.setPlaceholderText("......")
        self.t.trigger.connect(self.on_AI_translate)

    def on_AI_translate(self):

        global AITransData
        if AITransData:
            self.result_edit.setPlainText(AITransData)
        else:
            self.result_edit.setPlainText("error")
        AITransData = ""


class YouDaoTans(QThread):

    trigger = pyqtSignal()

    def __init__(self, dest, text):
        super().__init__()
        self.dest = dest
        self.text = text

    def run(self):

        global AITransData
        try:
            strings = GetSource.get_source_code(
                "http://106.12.179.253:8089/lsl/api/word?words=" + self.text + "&to=" + self.dest)
            res = json.loads(strings)
            AITransData = res['result']
        except:
            AITransData = "error,请重试!"
        self.trigger.emit()


class GTranslator(QThread):

    trigger = pyqtSignal()

    def __init__(self, dest, content):
        super().__init__()
        self.content = content
        self.dest = dest

    def run(self):

        Data = []
        global GTransData
        T = Translator(service_urls=["translate.google.cn"])
        try:
            ts = T.translate(self.content, dest=self.dest)
            if isinstance(ts.text, list):
                for i in ts:
                    Data.append(i.text)
                GTransData = Data
            else:
                GTransData = ts.text
        except:
            GTransData = "An error happended. Please retry..."
        self.trigger.emit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myWin = APP()
    myWin.show()
    sys.exit(app.exec_())