"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""
import os.path
import sys

import requests
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

from Downloader.Downloader import Downloader
import utils
from UI.DatapacksEditors import Ui_MainWindow
from UI.Management import Ui_Form

from loguru import logger as log


class MC_Version_Management_Window(QWidget, Ui_Form):
    def __init__(self):
        super(MC_Version_Management_Window, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.show()


class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        if not os.path.exists(os.path.join(os.getcwd(), "logs")):
            os.mkdir("logs")
        log.info("clear latest.log")
        with open("./logs/latest.log", "w") as fp:
            fp.write("")
        log.add("./logs/{time}.log")
        log.add("./logs/latest.log")
        log.info("client starting..")
        log.info("detect Runtime folder")
        if not os.path.exists("Runtime"):
            log.info("mkdir Runtime")
            os.mkdir("Runtime")
        self.RuntimePath = os.path.join(os.getcwd(), "Runtime")
        self.setupUi(self)
        log.success("setupUi")
        self.ChineseSimplified.changed.connect(self.languageRadioChinese)
        self.English.changed.connect(self.languageRadioEnglish)
        self.dialog = QFileDialog()
        self.fileModel = QFileSystemModel()
        self.fileModel.setRootPath("C:/")
        self.fileTree.setModel(self.fileModel)
        self.fileDialogTitle = "打开文件"
        self.open_project.triggered.connect(self.On_open_project_btn_click)
        self.MC_window = MC_Version_Management_Window()
        self.open_MC.triggered.connect(self.MC_window.OPEN)
        self.lang = utils.readLang("./UI/res/ChineseSimplified.lang")
        self.minecraftVersionList = utils.getAllMinecraftVersion()
        self.MC_window.download_progress.setValue(0)
        self.doneTitle = "下载成功"
        self.doneText = "下载成功！"
        for i in self.minecraftVersionList:
            self.MC_window.minecrafts.addItem(i['id'])
        self.MC_window.download.clicked.connect(self.On_download_btn_click)
        log.success("get MinecraftVersionList")
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
        self.lang = utils.readLang("./UI/res/English.lang")
        self.changeLanguage()
        log.success("goto English")

    def useChinese(self):
        self.lang = utils.readLang("./UI/res/ChineseSimplified.lang")
        self.changeLanguage()
        log.success("goto Chinese")

    def changeLanguage(self):
        for id in self.lang.keys():
            content = self.lang[id]
            if id == "MainWindow.Title":
                self.setWindowTitle(content)
            elif id[0:2] == "v!":
                exec(f"self.{id.replace('v!', '')} = '{content}'")
            else:
                ids = id.split(".")
                if len(ids) == 3:
                    eval(f"self.{ids[0]}.{ids[1]}.set{ids[2]}('{content}')")
                else:
                    eval(f"self.{ids[0]}.set{ids[1]}('{content}')")

    def On_open_project_btn_click(self):
        fileName = self.dialog.getOpenFileName(self, self.fileDialogTitle)
        if fileName[0]:
            with open(fileName[0], 'r') as f:
                data = f.read()
                print(data)

    def On_download_btn_click(self):
        for i in self.minecraftVersionList:
            if i['id'] == self.MC_window.minecrafts.selectedItems()[0].text():
                url = i['url']
                sourceList = ["http://launchermeta.mojang.com", "https://bmclapi2.bangbang93.com",
                              "https://download.mcbbs.net"]
                s = utils.selectServer(sourceList)
                source = url.replace("https://launchermeta.mojang.com", s)
                version = requests.get(source).json()
                clientUrl = version['downloads']['client']['url'].replace("https://launcher.mojang.com", s)
                minecraftFolder = os.path.join(self.RuntimePath, "Minecraft")
                if not os.path.exists(minecraftFolder):
                    os.mkdir(minecraftFolder)
                downloadPath = os.path.join(minecraftFolder, i['id'])
                if not os.path.exists(downloadPath):
                    os.mkdir(downloadPath)

                log.info("clienturl = " + clientUrl)
                mute = QMutex()
                do = Downloader(clientUrl, os.path.join(downloadPath, f"{i['id']}.jar"),
                                self.MC_window.download_progress, mute)
                do.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = DatapacksEditors()
    ui.show()
    sys.exit(app.exec())
