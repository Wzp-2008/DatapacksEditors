# Form implementation generated from reading ui file 'J:\DatapacksEditors\UI\Management.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(257, 271)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.minecrafts = QtWidgets.QListWidget(Form)
        self.minecrafts.setObjectName("minecrafts")
        self.verticalLayout.addWidget(self.minecrafts)
        self.downloadInfo = QtWidgets.QLabel(Form)
        self.downloadInfo.setObjectName("downloadInfo")
        self.verticalLayout.addWidget(self.downloadInfo)
        self.download_progress = QtWidgets.QProgressBar(Form)
        self.download_progress.setProperty("value", 24)
        self.download_progress.setObjectName("download_progress")
        self.verticalLayout.addWidget(self.download_progress)
        self.download = QtWidgets.QPushButton(Form)
        self.download.setObjectName("download")
        self.verticalLayout.addWidget(self.download)
        self.done = QtWidgets.QPushButton(Form)
        self.done.setObjectName("done")
        self.verticalLayout.addWidget(self.done)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.downloadInfo.setText(_translate("Form", "下载进度："))
        self.download.setText(_translate("Form", "下载"))
        self.done.setText(_translate("Form", "确定"))
