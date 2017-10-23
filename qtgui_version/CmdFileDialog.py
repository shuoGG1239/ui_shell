from ui_CmdFileDialog import Ui_cmdFileDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

class CmdFileDialog(QDialog):
    def __init__(self):
        super(CmdFileDialog, self).__init__()
        self.cmddialogui = Ui_cmdFileDialog()
        self.cmddialogui.setupUi(self)
        self.cmddialogui.pushButtonSave.clicked.connect(self.__slot_savefile)
        self.__init_plainedit()

    @pyqtSlot()
    def __slot_savefile(self):
        open('cmds.json', 'w').write(self.cmddialogui.plainTextEditCmds.toPlainText())
        self.accept()


    def __init_plainedit(self):
        cmdtext = open('cmds.json','r').read()
        self.cmddialogui.plainTextEditCmds.setPlainText(cmdtext)
