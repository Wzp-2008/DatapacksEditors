# Form implementation generated from reading ui file 'F:\我的python\DatapacksEditors\UI\create_full.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_create_fullw(object):
    def setupUi(self, create_fullw):
        create_fullw.setObjectName("create_fullw")
        create_fullw.resize(609, 325)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(create_fullw.sizePolicy().hasHeightForWidth())
        create_fullw.setSizePolicy(sizePolicy)
        self.create_full_c = QtWidgets.QPushButton(create_fullw)
        self.create_full_c.setGeometry(QtCore.QRect(460, 260, 131, 41))
        self.create_full_c.setObjectName("create_full_c")
        self.label = QtWidgets.QLabel(create_fullw)
        self.label.setGeometry(QtCore.QRect(9, 220, 290, 21))
        self.label.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(create_fullw)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 581, 61))
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(create_fullw)
        self.widget.setGeometry(QtCore.QRect(310, 220, 281, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_116 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_116.setObjectName("checkBox_116")
        self.horizontalLayout_3.addWidget(self.checkBox_116)
        self.checkBox_118 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_118.setObjectName("checkBox_118")
        self.horizontalLayout_3.addWidget(self.checkBox_118)
        self.checkbox_117 = QtWidgets.QCheckBox(self.widget)
        self.checkbox_117.setObjectName("checkbox_117")
        self.horizontalLayout_3.addWidget(self.checkbox_117)
        self.checkBox_119 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_119.setObjectName("checkBox_119")
        self.horizontalLayout_3.addWidget(self.checkBox_119)
        self.widget1 = QtWidgets.QWidget(create_fullw)
        self.widget1.setGeometry(QtCore.QRect(9, 170, 581, 28))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.projectPath = QtWidgets.QLineEdit(self.widget1)
        self.projectPath.setObjectName("projectPath")
        self.horizontalLayout_2.addWidget(self.projectPath)
        self.btn_change_P = QtWidgets.QPushButton(self.widget1)
        self.btn_change_P.setObjectName("btn_change_P")
        self.horizontalLayout_2.addWidget(self.btn_change_P)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.widget2 = QtWidgets.QWidget(create_fullw)
        self.widget2.setGeometry(QtCore.QRect(9, 120, 581, 28))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.packPath = QtWidgets.QLineEdit(self.widget2)
        self.packPath.setObjectName("packPath")
        self.horizontalLayout.addWidget(self.packPath)
        self.btn_change_Pack = QtWidgets.QPushButton(self.widget2)
        self.btn_change_Pack.setObjectName("btn_change_Pack")
        self.horizontalLayout.addWidget(self.btn_change_Pack)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.widget3 = QtWidgets.QWidget(create_fullw)
        self.widget3.setGeometry(QtCore.QRect(10, 80, 581, 23))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget3)
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.packPath_2 = QtWidgets.QLineEdit(self.widget3)
        self.packPath_2.setObjectName("packPath_2")
        self.horizontalLayout_6.addWidget(self.packPath_2)

        self.retranslateUi(create_fullw)
        QtCore.QMetaObject.connectSlotsByName(create_fullw)

    def retranslateUi(self, create_fullw):
        _translate = QtCore.QCoreApplication.translate
        create_fullw.setWindowTitle(_translate("create_fullw", "创建新的数据包"))
        self.create_full_c.setText(_translate("create_fullw", "继续"))
        self.label.setText(_translate("create_fullw", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#000000;\">请选择您的数据包适用的minecraft版本:</span></p></body></html>"))
        self.label_4.setText(_translate("create_fullw", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:700;\">创建您的minecraft数据包</span></p></body></html>"))
        self.checkBox_116.setText(_translate("create_fullw", "1.16.x"))
        self.checkBox_118.setText(_translate("create_fullw", "1.18.x"))
        self.checkbox_117.setText(_translate("create_fullw", "1.17.x"))
        self.checkBox_119.setText(_translate("create_fullw", "1.19+"))
        self.label_3.setText(_translate("create_fullw", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#000000;\">您的数据包路径:</span></p></body></html>"))
        self.btn_change_P.setText(_translate("create_fullw", "更改"))
        self.label_2.setText(_translate("create_fullw", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#000000;\">您的项目路径:</span></p></body></html>"))
        self.btn_change_Pack.setText(_translate("create_fullw", "更改"))
        self.label_5.setText(_translate("create_fullw", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#000000;\">项目名称:</span></p></body></html>"))
