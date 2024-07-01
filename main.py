"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""
import _io
import json
import time

import utils
import os.path
import sys
import os
import requests
from winreg import *
from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from Downloader.Downloader import Downloader
from UI.DatapacksEditors import Ui_MainWindow
from UI.Management import Ui_Form
from UI.create_full import Ui_createfullwindows
from loguru import logger as log

temp: _io.TextIOWrapper = None
datapackPath = None
pPath = None
projectName = None
pTree = None
# functionPath = datapackPath + "/data/" + projectName + "/functions"


class MC_Version_Management_Window(QWidget, Ui_Form):
    def __init__(self):
        super(MC_Version_Management_Window, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.show()


class Create_Full_Window(QWidget, Ui_createfullwindows):
    def __init__(self):
        super(Create_Full_Window, self).__init__()
        self.v116 = None
        self.v119 = None
        self.datapackPath = None
        self.pPath = None
        self.projectName = None
        self.setupUi(self)
        # 改变路径
        self.btn_change_Pack.clicked.connect(self.choosePackPath)
        self.btn_change_P.clicked.connect(self.chooseProjectPath)
        self.PathDialog = QFileDialog()
        self.PathDialogTitle = "选择文件夹"
        # 获取项目有关信息
        self.packname.textChanged.connect(self.getProjectName)
        self.packPath.textChanged.connect(self.getPackPath)
        self.projectPath.textChanged.connect(self.getProjectPath)
        self.v_116.toggled['bool'].connect(self.readVersion)
        self.v_119.toggled['bool'].connect(self.readVersion)
        # 创建按钮连接
        self.create_full_c.clicked.connect(self.create_full_pack)

    def getProjectName(self, text):
        global projectName
        projectName = text
        print("projectName:" + str(text))

    def getProjectPath(self, text):
        global pPath
        pPath = text
        print("projectPath:" + str(text))

    def getPackPath(self, text):
        global datapackPath
        datapackPath = text
        print("datapackPath:" + str(text))

    def choosePackPath(self):
        packPath = self.PathDialog.getExistingDirectory(self, self.PathDialogTitle)
        self.packPath.setText(packPath)

    def chooseProjectPath(self):
        projectPath = self.PathDialog.getExistingDirectory(self, self.PathDialogTitle)
        self.projectPath.setText(projectPath)

    def readVersion(self):
        if self.v_116.isChecked():
            self.v116 = 1
        if self.v_119.isChecked():
            self.v119 = 1

    def OPEN(self):
        self.show()

    def create_full_pack(self):
        global temp
        # create project
        os.chdir(projectName)
        os.mkdir("logs")
        # create pack
        os.chdir(datapackPath)
        os.mkdir("data")
        if self.v119 == 1:
            index = {
                "pack": {
                    "pack_format": 10,
                    "description": "Hello World"
                }
            }
            with open("pack.mcmeta", "x") as fp:
                json.dump(index, fp, indent=4, ensure_ascii=False)
        if self.v116 == 1:
            index = {
                "pack": {
                    "pack_format": 6,
                    "description": "Hello World"
                }
            }
            with open("pack.mcmeta", "x") as fp:
                json.dump(index, fp, indent=4, ensure_ascii=False)
        os.chdir(datapackPath + "/data")
        os.mkdir(projectName)
        os.chdir(projectName)
        os.mkdir("functions")
        os.mkdir("tags")
        self.close()

        # Tree_root
        root_p = QTreeWidgetItem(pTree)
        root_p.setText(0, projectName)

        # Tree_children
        child0 = QTreeWidgetItem(root_p)
        child0.setText(0, 'Functions')
        root_p.addChild(child0)
        child1 = QTreeWidgetItem(root_p)
        child1.setText(0, 'Tags')
        root_p.addChild(child1)
        child2 = QTreeWidgetItem(root_p)
        child2.setText(0, 'Advancements')
        root_p.addChild(child2)

class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __showRestoreWindow(self):
        """ 复原窗口并更换最大化按钮的图标 """
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()
    
    def minimize_window(self):
        self.showMinimized()

    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        global pTree
        
        # 无边框初始化
        self.window_point = None
        self.start_point = None
        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.tab1 = None
        
        # 无边框，窗口美化
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon('icon.ico'))
        
        #日志
        if not os.path.exists(os.path.join(os.getcwd(), "logs")):
            os.mkdir("logs")
        log.info("clear latest.log")
        with open("./logs/latest.log", "w") as fp:
            fp.write("")
        log.add("./logs/{time}.log")
        log.add("./logs/latest.log")
        log.info("client starting..")
        self.reg = CreateKeyEx(HKEY_CURRENT_USER, r"Software\DatapacksEditors")
        log.success("get Config reg")
        try:
            self.language_ = QueryValue(self.reg, "language")
            print(self.language_)
        except FileNotFoundError:
            log.warning("Didn't find language value")
            self.language_ = "ChineseSimplified"
            SetValue(self.reg, "language", REG_SZ, self.language_)
            log.success("Create language value with default language:ChineseSimplified")
        log.success("get language config")
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
        # 文件树
        pTree = self.project_tree
        # 打开文件
        self.fileDialogTitle = "打开文件"
        self.open_project.triggered.connect(self.On_open_project_btn_click)
        # 新建mc函数文件
        self.create_ff.triggered.connect(self.On_new_function_btn_click)
        self.create_ff.triggered.connect(self.click_count)
        self.count = 0
        self.tabWidget.tabCloseRequested.connect(self.close_tab)
        # 创建完整数据包
        self.cfwindows = Create_Full_Window()
        self.full_pack.triggered.connect(self.cfwindows.OPEN)
        # 图标
        self.namel.setIcon(QIcon('icon.ico'))
        # 将按钮的点击信号连接到槽函数
        self.minBt.triggered.connect(self.window().showMinimized)
        self.maxBt.triggered.connect(self.__showRestoreWindow)
        self.closeBt.triggered.connect(self.window().close)
        # 下载窗口
        self.MC_window = MC_Version_Management_Window()
        self.open_MC.triggered.connect(self.MC_window.OPEN)
        try:
            self.lang = utils.readLang(f"./UI/res/{self.language_}.lang")
        except FileNotFoundError:
            self.language_ = "ChineseSimplified"
        try:
            self.lang = utils.readLang(f"./UI/res/{self.language_}.lang")
        except FileNotFoundError as e:
            log.error("The language file is incomplete. Please reinstall and try again")
            log.error(e)
            exit(1)
        self.changeLanguage()
        self.minecraftVersionList = utils.getAllMinecraftVersion()
        self.MC_window.download_progress.setValue(0)
        self.doneTitle = "下载成功"
        self.doneText = "下载成功！"
        for i in self.minecraftVersionList:
            self.MC_window.minecrafts.addItem(i['id'])
        self.MC_window.download.clicked.connect(self.On_download_btn_click)
        log.success("get MinecraftVersionList")
        log.success(f"init Ui with {self.language_} lang!")
        log.success("starting done.")
        self.ismoving = False
        self.menubar.setNativeMenuBar(False)

    # 无边框
    # 重写鼠标事件
    def mouseMoveEvent(self, e: QMouseEvent):
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.MouseButton.LeftButton:
            self._startPos = QPoint(e.pos())
            self._tracking = True

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.MouseButton.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

    def mouseDoubleClickEvent(self, event):
        """ 双击最大化/还原窗口 """
        self.__showRestoreWindow()

    def close_tab(self, index):
        self.tabWidget.removeTab(index)
        self.count = self.count - 1
        print("Remain tabs:" + str(self.count))

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
        self.language_ = "English"
        self.changeLanguage()
        log.success("goto English")

    def useChinese(self):
        self.lang = utils.readLang("UI/res/ChineseSimplified.lang")
        self.language_ = "ChineseSimplified"
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
        SetValue(self.reg, "language", REG_SZ, self.language_)

    def On_open_project_btn_click(self):
        fileName = self.dialog.getOpenFileName(self, self.fileDialogTitle)
        if fileName[0]:
            with open(fileName[0], 'r') as f:
                data = f.read()
                print(data)

    def On_new_function_btn_click(self):
        text = QtWidgets.QTextEdit()
        self.tabWidget.addTab(text, 'new.mcfunction')
        # 文本框去边
        text.setStyleSheet("border:none;")
        # open(functionPath + "/new.mcfunction", 'x')

    def click_count(self):
        self.count += 1
        print("open:" + str(self.count))

    def On_download_btn_click(self):
        for i in self.minecraftVersionList:
            if i['id'] == self.MC_window.minecrafts.selectedItems()[0].text():
                url = i['url']
                sourceList = ["https://launchermeta.mojang.com", "https://bmclapi2.bangbang93.com"]
                s = utils.selectServer(sourceList)
                source = url.replace("https://bmclapi2.bangbang93.com", s)
                version = requests.get(source).json()
                clientUrl = version['downloads']['client']['url'].replace("https://bmclapi2.bangbang93.com", s)
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
