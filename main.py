"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""
import os.path
import sys

from PyQt6.QtWidgets import *

import utils
from UI.DatapacksEditors import Ui_MainWindow

from loguru import logger as log


class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        if not os.path.exists(os.path.join(os.getcwd(),"logs")):
            os.mkdir("logs")
        log.info("clear latest.log")
        with open("./logs/latest.log","w") as fp:
            fp.write("")
        log.add("./logs/{time}.log")
        log.add("./logs/latest.log")
        log.info("client starting..")
        self.setupUi(self)
        log.success("setupUi")
        self.ChineseSimplified.changed.connect(self.languageRadioChinese)
        self.English.changed.connect(self.languageRadioEnglish)
        self.dialog = QFileDialog()
        self.fileDialogTitle = "打开文件"
        self.open_project.triggered.connect(self.On_open_project_btn_click)
        self.useChinese()
        log.success("init Ui with Chinese lang!")
        log.success("starting done.")

    def languageRadioChinese(self):
        if self.ChineseSimplified.isChecked():
            self.English.setChecked(False)
            self.useChinese()
        else:
            self.English.setChecked(True)
            self.useEnglish()

    def languageRadioEnglish(self):
        if self.English.isChecked():
            self.ChineseSimplified.setChecked(False)
            self.useEnglish()
        else:
            self.ChineseSimplified.setChecked(True)
            self.useChinese()

    def useEnglish(self):
        langEnglish = utils.readLang("./UI/res/English.lang")
        for id in langEnglish.keys():
            content = langEnglish[id]
            if id == "MainWindow.Title":
                self.setWindowTitle(content)
            elif id[0:2] == "v!":
                exec(f"self.{id.replace('v!','')} = '{content}'")
            else:
                ids = id.split(".")
                eval(f"self.{ids[0]}.set{ids[1]}('{content}')")
        log.success("goto English")

    def useChinese(self):
        langChinese = utils.readLang("./UI/res/ChineseSimplified.lang")
        for id in langChinese.keys():
            content = langChinese[id]
            if id == "MainWindow.Title":
                self.setWindowTitle(content)
            elif id[0:2] == "v!":
                exec(f"self.{id.replace('v!','')} = '{content}'")
            else:
                ids = id.split(".")
                eval(f"self.{ids[0]}.set{ids[1]}('{content}')")
        log.success("goto Chinese")

    def On_open_project_btn_click(self):
        fileName = self.dialog.getOpenFileName(self,self.fileDialogTitle)
        if fileName[0]:
            with open(fileName[0], 'r') as f:
                data = f.read()
                print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DatapacksEditors()
    ui.show()
    sys.exit(app.exec())
