"""
 Author : wzpMC,qingchenyou
 Date:   2022/1/19
 Time:   21:32
"""
import utils
import os.path
import sys
import os
import requests
import win32con
import ctypes
from winreg import *
from win32api import SendMessage
from win32gui import ReleaseCapture
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from Downloader.Downloader import Downloader
from UI.DatapacksEditors import Ui_MainWindow
from UI.Management import Ui_Form
from UI.create_full import Ui_createfullwindows
from loguru import logger as log


class MC_Version_Management_Window(QWidget, Ui_Form):
    def __init__(self):
        super(MC_Version_Management_Window, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.show()


class Create_Full_Window(QWidget, Ui_createfullwindows):
    def __init__(self):
        super(Create_Full_Window, self).__init__()
        self.datapackPath = None
        self.pPath = None
        self.projectName = None
        self.setupUi(self)
        # 改变数据包路径
        self.btn_change_Pack.clicked.connect(self.choosePackPath)
        self.datapackPathDialog = QFileDialog()
        self.datapackPathDialogTitle = "选择路径"
        # 获取项目有关信息
        self.packname.textChanged.connect(self.getProjectName)
        self.packPath.textChanged.connect(self.getPackPath)
        self.projectPath.textChanged.connect(self.getProjectPath)
        # 创建按钮连接
        self.create_full_c.clicked.connect(self.create_full_pack)

    def getProjectName(self, text):
        self.projectName = text
        print("projectName:" + str(text))

    def getProjectPath(self, text):
        self.pPath = text
        print("projectPath:" + str(text))

    def getPackPath(self, text):
        self.datapackPath = text
        print("datapackPath:" + str(text))

    def choosePackPath(self):
        self.datapackPath = self.datapackPathDialog.getOpenFileName(self, self.datapackPathDialogTitle)

    def OPEN(self):
        self.show()

    def create_full_pack(self):
        pass


class DatapacksEditors(QMainWindow, Ui_MainWindow):
    def __showRestoreWindow(self):
        """ 复原窗口并更换最大化按钮的图标 """
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def __init__(self, parent=None):
        super(DatapacksEditors, self).__init__(parent)
        # 无边框初始化
        self.window_point = None
        self.start_point = None
        self._startPos = None
        self._endPos = None
        self._tracking = False
        self.tab1 = None
        # 无边框，窗口美化
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowIcon(QIcon('favicon.ico'))
        #
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
        self.fileModel = QFileSystemModel()
        self.fileModel.setRootPath("C:/")
        # self.fileTree.setModel(self.fileModel)
        # self.fileTree.doubleClicked.connect(self.initUI)
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
        self.namel.setIcon(QIcon('favicon.ico'))
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

    # 文件树操作
    def initUI(self, Qmodelidx):
        filePath = self.fileModel.filePath(Qmodelidx)
        print(filePath)

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

    def click_count(self):
        self.count += 1
        print("open:" + str(self.count))

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
