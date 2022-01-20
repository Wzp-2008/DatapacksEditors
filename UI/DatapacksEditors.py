# Form implementation generated from reading ui file 'J:\DatapacksEditors\UI\DatapacksEditors.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.export_menu = QtWidgets.QMenu(self.file)
        self.export_menu.setObjectName("export_menu")
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.new_project = QtGui.QAction(MainWindow)
        self.new_project.setObjectName("new_project")
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
        self.export_menu.addAction(self.export_zip)
        self.file.addAction(self.new_project)
        self.file.addAction(self.open_project)
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
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())
        self.menubar.addAction(self.run.menuAction())
        self.menubar.addAction(self.language.menuAction())
        self.menubar.addAction(self.help.menuAction())
        self.menubar.addAction(self.MC.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.export_menu.setTitle(_translate("MainWindow", "导出"))
        self.edit.setTitle(_translate("MainWindow", "编辑"))
        self.run.setTitle(_translate("MainWindow", "运行"))
        self.help.setTitle(_translate("MainWindow", "帮助"))
        self.MC.setTitle(_translate("MainWindow", "MC版本管理"))
        self.language.setTitle(_translate("MainWindow", "语言"))
        self.new_project.setText(_translate("MainWindow", "新建项目"))
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
