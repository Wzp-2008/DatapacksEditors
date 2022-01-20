"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""

import sys
from PyQt6.QtWidgets import *
import utils
from UI.DatapacksEditors import Ui_MainWindow


class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        self.setupUi(self)
        self.ChineseSimplified.changed.connect(self.languageRadioChinese)
        self.English.changed.connect(self.languageRadioEnglish)
        self.useChinese()
        self.MinecraftVersionList = utils.getAllMinecraftVersion()
        self.open_MC.clicked.connect()

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
            else:
                ids = id.split(".")
                eval(f"self.{ids[0]}.set{ids[1]}('{content}')")

    def useChinese(self):
        langChinese = utils.readLang("./UI/res/ChineseSimplified.lang")
        for id in langChinese.keys():
            content = langChinese[id]
            if id == "MainWindow.Title":
                self.setWindowTitle(content)
            else:
                ids = id.split(".")
                eval(f"self.{ids[0]}.set{ids[1]}('{content}')")

    def openVersionManagement(self):
        self.versionManagement = Ch

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DatapacksEditors()
    ui.show()
    sys.exit(app.exec())
