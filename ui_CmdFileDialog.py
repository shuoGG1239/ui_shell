# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_CmdFileDialog.ui'
#
# Created: Mon Oct 23 23:35:49 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cmdFileDialog(object):
    def setupUi(self, cmdFileDialog):
        cmdFileDialog.setObjectName("cmdFileDialog")
        cmdFileDialog.resize(788, 324)
        self.plainTextEditCmds = QtWidgets.QPlainTextEdit(cmdFileDialog)
        self.plainTextEditCmds.setGeometry(QtCore.QRect(20, 10, 751, 271))
        self.plainTextEditCmds.setObjectName("plainTextEditCmds")
        self.pushButtonSave = QtWidgets.QPushButton(cmdFileDialog)
        self.pushButtonSave.setGeometry(QtCore.QRect(250, 290, 261, 23))
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.retranslateUi(cmdFileDialog)
        QtCore.QMetaObject.connectSlotsByName(cmdFileDialog)

    def retranslateUi(self, cmdFileDialog):
        _translate = QtCore.QCoreApplication.translate
        cmdFileDialog.setWindowTitle(_translate("cmdFileDialog", "Cmd JsonFile"))
        self.pushButtonSave.setText(_translate("cmdFileDialog", "Save"))

