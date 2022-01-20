"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""
import PyQt6
import os
import json
import glob

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from UI.DatapacksEditors import Ui_MainWindow


class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DatapacksEditors()
    ui.show()
    sys.exit(app.exec())
