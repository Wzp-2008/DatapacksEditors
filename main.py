"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI.DatapacksEditors import Ui_MainWindow
import requests


class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        self.setupUi(self)
        self.ChineseSimplified.changed.connect(self.languageRadioChinese)
        self.English.changed.connect(self.languageRadioEnglish)

    def languageRadioChinese(self):
        if self.ChineseSimplified.isChecked():
            self.English.setChecked(False)
        else:
            self.English.setChecked(True)

    def languageRadioEnglish(self):
        if self.English.isChecked():
            self.ChineseSimplified.setChecked(False)
        else:
            self.ChineseSimplified.setChecked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DatapacksEditors()
    ui.show()
    sys.exit(app.exec())
