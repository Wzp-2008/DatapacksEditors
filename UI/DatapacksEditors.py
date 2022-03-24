# Form implementation generated from reading ui file 'F:\我的python\DatapacksEditors\UI\DatapacksEditors.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow.resize(773, 541)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/favicon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 0, 601, 490))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 181, 491))
        font = QtGui.QFont()
        font.setBold(True)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget_2.setElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.file_tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setBold(True)
        self.file_tab.setFont(font)
        self.file_tab.setToolTipDuration(3)
        self.file_tab.setObjectName("file_tab")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/file.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget_2.addTab(self.file_tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 773, 22))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.export_menu = QtWidgets.QMenu(self.file)
        self.export_menu.setObjectName("export_menu")
        self.new_project = QtWidgets.QMenu(self.file)
        self.new_project.setMouseTracking(True)
        self.new_project.setAcceptDrops(True)
        self.new_project.setObjectName("new_project")
        self.edit = QtWidgets.QMenu(self.menubar)
        self.edit.setObjectName("edit")
        self.run = QtWidgets.QMenu(self.menubar)
        self.run.setObjectName("run")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        self.MC = QtWidgets.QMenu(self.menubar)
        self.MC.setObjectName("MC")
        self.language = QtWidgets.QMenu(self.menubar)
        self.language.setObjectName("language")
        self.namel = QtWidgets.QMenu(self.menubar)
        self.namel.setObjectName("namel")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar_4 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_4.setObjectName("toolBar_4")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.BottomToolBarArea, self.toolBar_4)
        self.open_project = QtGui.QAction(MainWindow)
        self.open_project.setObjectName("open_project")
        self.export_zip = QtGui.QAction(MainWindow)
        self.export_zip.setObjectName("export_zip")
        self.undo = QtGui.QAction(MainWindow)
        self.undo.setObjectName("undo")
        self.redo = QtGui.QAction(MainWindow)
        self.redo.setObjectName("redo")
        self.find = QtGui.QAction(MainWindow)
        self.find.setObjectName("find")
        self.replace = QtGui.QAction(MainWindow)
        self.replace.setObjectName("replace")
        self.run_MC = QtGui.QAction(MainWindow)
        self.run_MC.setObjectName("run_MC")
        self.build_map = QtGui.QAction(MainWindow)
        self.build_map.setObjectName("build_map")
        self.about = QtGui.QAction(MainWindow)
        self.about.setObjectName("about")
        self.check_update = QtGui.QAction(MainWindow)
        self.check_update.setObjectName("check_update")
        self.ChineseSimplified = QtGui.QAction(MainWindow)
        self.ChineseSimplified.setCheckable(True)
        self.ChineseSimplified.setChecked(True)
        self.ChineseSimplified.setObjectName("ChineseSimplified")
        self.English = QtGui.QAction(MainWindow)
        self.English.setCheckable(True)
        self.English.setObjectName("English")
        self.open_MC = QtGui.QAction(MainWindow)
        self.open_MC.setObjectName("open_MC")
        self.save = QtGui.QAction(MainWindow)
        self.save.setCheckable(False)
        self.save.setEnabled(True)
        self.save.setObjectName("save")
        self.save_other = QtGui.QAction(MainWindow)
        self.save_other.setObjectName("save_other")
        self.full_pack = QtGui.QAction(MainWindow)
        self.full_pack.setObjectName("full_pack")
        self.create_ff = QtGui.QAction(MainWindow)
        self.create_ff.setObjectName("create_ff")
        self.create_load = QtGui.QAction(MainWindow)
        self.create_load.setObjectName("create_load")
        self.create_other = QtGui.QAction(MainWindow)
        self.create_other.setObjectName("create_other")
        self.actioncreate_tick = QtGui.QAction(MainWindow)
        self.actioncreate_tick.setObjectName("actioncreate_tick")
        self.actsave = QtGui.QAction(MainWindow)
        self.actsave.setObjectName("actsave")
        self.minBt = QtGui.QAction(MainWindow)
        self.minBt.setObjectName("minBt")
        self.maxBt = QtGui.QAction(MainWindow)
        self.maxBt.setObjectName("maxBt")
        self.closeBt = QtGui.QAction(MainWindow)
        self.closeBt.setObjectName("closeBt")
        self.export_menu.addAction(self.export_zip)
        self.new_project.addAction(self.full_pack)
        self.new_project.addSeparator()
        self.new_project.addAction(self.create_ff)
        self.new_project.addAction(self.create_load)
        self.new_project.addAction(self.create_other)
        self.file.addAction(self.new_project.menuAction())
        self.file.addAction(self.open_project)
        self.file.addAction(self.actsave)
        self.file.addAction(self.save_other)
        self.file.addSeparator()
        self.file.addAction(self.export_menu.menuAction())
        self.edit.addAction(self.undo)
        self.edit.addAction(self.redo)
        self.edit.addSeparator()
        self.edit.addAction(self.find)
        self.edit.addAction(self.replace)
        self.run.addAction(self.run_MC)
        self.run.addAction(self.build_map)
        self.help.addAction(self.about)
        self.help.addAction(self.check_update)
        self.MC.addAction(self.open_MC)
        self.language.addAction(self.ChineseSimplified)
        self.language.addAction(self.English)
        self.namel.addAction(self.minBt)
        self.namel.addAction(self.maxBt)
        self.namel.addSeparator()
        self.namel.addAction(self.closeBt)
        self.menubar.addAction(self.namel.menuAction())
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.run.menuAction())
        self.menubar.addAction(self.language.menuAction())
        self.menubar.addAction(self.help.menuAction())
        self.menubar.addAction(self.MC.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DatapackEditors"))
        self.file_tab.setToolTip(_translate("MainWindow", "文件管理器(Ctrl+Alt+1)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.file_tab), _translate("MainWindow", "文件"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.export_menu.setTitle(_translate("MainWindow", "导出"))
        self.new_project.setTitle(_translate("MainWindow", "新建..."))
        self.edit.setTitle(_translate("MainWindow", "编辑"))
        self.run.setTitle(_translate("MainWindow", "运行"))
        self.help.setTitle(_translate("MainWindow", "帮助"))
        self.MC.setTitle(_translate("MainWindow", "MC版本管理"))
        self.language.setTitle(_translate("MainWindow", "语言"))
        self.namel.setTitle(_translate("MainWindow", "ico"))
        self.toolBar_4.setWindowTitle(_translate("MainWindow", "toolBar_4"))
        self.open_project.setText(_translate("MainWindow", "打开项目"))
        self.export_zip.setText(_translate("MainWindow", "导出为zip"))
        self.undo.setText(_translate("MainWindow", "撤销"))
        self.redo.setText(_translate("MainWindow", "重做"))
        self.find.setText(_translate("MainWindow", "查找"))
        self.replace.setText(_translate("MainWindow", "替换"))
        self.run_MC.setText(_translate("MainWindow", "在MC中启动本项目"))
        self.build_map.setText(_translate("MainWindow", "生成蓝图"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.check_update.setText(_translate("MainWindow", "检查更新"))
        self.ChineseSimplified.setText(_translate("MainWindow", "简体中文"))
        self.English.setText(_translate("MainWindow", "English"))
        self.open_MC.setText(_translate("MainWindow", "打开MC版本管理页"))
        self.save.setText(_translate("MainWindow", "保存"))
        self.save.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">保存文件</span> (Ctrl+S)</p></body></html>"))
        self.save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.save_other.setText(_translate("MainWindow", "另存为..."))
        self.full_pack.setText(_translate("MainWindow", "完整数据包"))
        self.create_ff.setText(_translate("MainWindow", "mc函数文件"))
        self.create_load.setText(_translate("MainWindow", "json文件"))
        self.create_other.setText(_translate("MainWindow", "其他"))
        self.actioncreate_tick.setText(_translate("MainWindow", "create_tick"))
        self.actsave.setText(_translate("MainWindow", "保存"))
        self.minBt.setText(_translate("MainWindow", "minBt"))
        self.maxBt.setText(_translate("MainWindow", "maxBt"))
        self.closeBt.setText(_translate("MainWindow", "closeBt"))
