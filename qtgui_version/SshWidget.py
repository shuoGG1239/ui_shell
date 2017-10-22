from ui_SshWidget import Ui_SshWidget
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from shuogg import shuogg_tool
from shuogg import paramiko_pack_module as PM
import json

class SshWidget(QWidget):
    def __init__(self):
        super(SshWidget, self).__init__()
        self.sshwidgetui = Ui_SshWidget()
        self.sshwidgetui.setupUi(self)
        self.sshwidgetui.pushButtonGo.clicked.connect(self.__slot_execute)
        self.sshwidgetui.pushButtonEdit.clicked.connect(self.__slot_edit)
        self.sshwidgetui.pushButtonClear.clicked.connect(self.__slot_clear)
        self.__init_userinfo()
        self.__init_cmdscombobox()
        self.ip = self.sshwidgetui.lineEditServerIP.text()
        self.user = self.sshwidgetui.lineEditUser.text()
        self.password = self.sshwidgetui.lineEditPassword.text()


    @pyqtSlot()
    def __slot_execute(self):
        current_cmd_real = self.cmds_map.get(self.sshwidgetui.comboBoxCmd.currentText())
        self.sshwidgetui.textBrowserOutput.append('EXE: '+current_cmd_real)
        responselist = PM.exec_onecmd(self.ip,self.user,self.password,current_cmd_real)
        for cmd in responselist:
            self.sshwidgetui.textBrowserOutput.append(cmd)

    @pyqtSlot()
    def __slot_edit(self):
        print('edit!')

    @pyqtSlot()
    def __slot_clear(self):
        self.sshwidgetui.textBrowserOutput.clear()

    def __init_cmdscombobox(self):
        self.cmds_map = json.load(open('cmds.json'))
        self.sshwidgetui.comboBoxCmd.addItems(self.cmds_map.keys())

    def __init_userinfo(self):
        userinfo_map = json.load(open('userinfo.json'))
        self.sshwidgetui.lineEditServerIP.setText(userinfo_map.get('ServerIP'))
        self.sshwidgetui.lineEditUser.setText(userinfo_map.get('User'))
        self.sshwidgetui.lineEditPassword.setText(userinfo_map.get('Password'))