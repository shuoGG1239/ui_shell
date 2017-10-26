# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_SshWidget.ui'
#
# Created: Thu Oct 26 22:31:38 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SshWidget(object):
    def setupUi(self, SshWidget):
        SshWidget.setObjectName("SshWidget")
        SshWidget.resize(534, 385)
        self.label = QtWidgets.QLabel(SshWidget)
        self.label.setGeometry(QtCore.QRect(30, 23, 61, 16))
        self.label.setObjectName("label")
        self.lineEditServerIP = QtWidgets.QLineEdit(SshWidget)
        self.lineEditServerIP.setGeometry(QtCore.QRect(90, 20, 101, 20))
        self.lineEditServerIP.setObjectName("lineEditServerIP")
        self.lineEditPassword = QtWidgets.QLineEdit(SshWidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(400, 20, 101, 20))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.label_2 = QtWidgets.QLabel(SshWidget)
        self.label_2.setGeometry(QtCore.QRect(333, 23, 61, 16))
        self.label_2.setObjectName("label_2")
        self.frameCmd = QtWidgets.QFrame(SshWidget)
        self.frameCmd.setGeometry(QtCore.QRect(30, 60, 471, 91))
        self.frameCmd.setFrameShape(QtWidgets.QFrame.Box)
        self.frameCmd.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frameCmd.setObjectName("frameCmd")
        self.label_4 = QtWidgets.QLabel(self.frameCmd)
        self.label_4.setGeometry(QtCore.QRect(230, 20, 31, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditArgs = QtWidgets.QLineEdit(self.frameCmd)
        self.lineEditArgs.setGeometry(QtCore.QRect(270, 17, 181, 20))
        self.lineEditArgs.setObjectName("lineEditArgs")
        self.label_3 = QtWidgets.QLabel(self.frameCmd)
        self.label_3.setGeometry(QtCore.QRect(10, 21, 31, 16))
        self.label_3.setObjectName("label_3")
        self.pushButtonEdit = QtWidgets.QPushButton(self.frameCmd)
        self.pushButtonEdit.setGeometry(QtCore.QRect(250, 55, 101, 23))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.comboBoxCmd = QtWidgets.QComboBox(self.frameCmd)
        self.comboBoxCmd.setGeometry(QtCore.QRect(50, 16, 171, 22))
        self.comboBoxCmd.setObjectName("comboBoxCmd")
        self.pushButtonGo = QtWidgets.QPushButton(self.frameCmd)
        self.pushButtonGo.setGeometry(QtCore.QRect(140, 55, 101, 23))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.pushButtonRefresh = QtWidgets.QPushButton(self.frameCmd)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(360, 55, 101, 23))
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.label_5 = QtWidgets.QLabel(SshWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 54, 12))
        self.label_5.setObjectName("label_5")
        self.lineEditUser = QtWidgets.QLineEdit(SshWidget)
        self.lineEditUser.setGeometry(QtCore.QRect(236, 20, 91, 20))
        self.lineEditUser.setObjectName("lineEditUser")
        self.label_6 = QtWidgets.QLabel(SshWidget)
        self.label_6.setGeometry(QtCore.QRect(206, 23, 31, 20))
        self.label_6.setObjectName("label_6")
        self.pushButtonClear = QtWidgets.QPushButton(SshWidget)
        self.pushButtonClear.setGeometry(QtCore.QRect(430, 348, 71, 23))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.plainTextEditOutput = QtWidgets.QPlainTextEdit(SshWidget)
        self.plainTextEditOutput.setGeometry(QtCore.QRect(30, 180, 471, 161))
        self.plainTextEditOutput.setReadOnly(False)
        self.plainTextEditOutput.setObjectName("plainTextEditOutput")

        self.retranslateUi(SshWidget)
        QtCore.QMetaObject.connectSlotsByName(SshWidget)

    def retranslateUi(self, SshWidget):
        _translate = QtCore.QCoreApplication.translate
        SshWidget.setWindowTitle(_translate("SshWidget", "ShuoGG SSH"))
        self.label.setText(_translate("SshWidget", "ServerIP"))
        self.label_2.setText(_translate("SshWidget", "Password"))
        self.label_4.setText(_translate("SshWidget", "Args"))
        self.label_3.setText(_translate("SshWidget", "Cmd"))
        self.pushButtonEdit.setText(_translate("SshWidget", "Edit"))
        self.pushButtonGo.setText(_translate("SshWidget", "Go!"))
        self.pushButtonRefresh.setText(_translate("SshWidget", "Refresh"))
        self.label_5.setText(_translate("SshWidget", "Output:"))
        self.label_6.setText(_translate("SshWidget", "User"))
        self.pushButtonClear.setText(_translate("SshWidget", "Clear"))

