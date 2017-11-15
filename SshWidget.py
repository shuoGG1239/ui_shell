import json
import re
from ui_SshWidget import Ui_SshWidget
from CmdFileDialog import CmdFileDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from shuogg import paramiko_pack_module as PM


class SshWidget(QWidget):
    def __init__(self):
        super(SshWidget, self).__init__()
        self.sshwidgetui = Ui_SshWidget()
        self.sshwidgetui.setupUi(self)
        self.sshwidgetui.pushButtonGo.clicked.connect(self.__slot_execute)
        self.sshwidgetui.pushButtonEdit.clicked.connect(self.__slot_edit)
        self.sshwidgetui.pushButtonClear.clicked.connect(self.__slot_clear)
        self.sshwidgetui.pushButtonRefresh.clicked.connect(self.__slot_refresh_database)
        self.__init_userinfo()
        self.__init_cmdscombobox()
        self.ip = self.sshwidgetui.lineEditServerIP.text()
        self.user = self.sshwidgetui.lineEditUser.text()
        self.password = self.sshwidgetui.lineEditPassword.text()
        self.sshwidgetui.lineEditArgs.setPlaceholderText('eg: 999,abc,8080')


    @pyqtSlot()
    def __slot_execute(self):
        current_cmd_real = self.cmds_map.get(self.sshwidgetui.comboBoxCmd.currentText())
        resultlist = re.findall(r"{}", current_cmd_real)
        if len(resultlist) > 0:
            argstext = self.sshwidgetui.lineEditArgs.text()
            arglist = argstext.split(',')
            if len(resultlist) != len(arglist):
                print('参数数量不匹配')
                return
            else:
                current_cmd_real = current_cmd_real.format(*arglist)
        self.sshwidgetui.plainTextEditOutput.appendPlainText('EXE: '+current_cmd_real)
        responselist = PM.exec_onecmd(self.ip,self.user,self.password,current_cmd_real)
        for cmd in responselist:
            self.sshwidgetui.plainTextEditOutput.appendPlainText(cmd)

    @pyqtSlot()
    def __slot_edit(self):
        cmdwindow = CmdFileDialog()
        # 如果是save进来的则更新droplist
        if cmdwindow.exec() == 1:
            self.__slot_refresh_database()

    @pyqtSlot()
    def __slot_clear(self):
        self.sshwidgetui.plainTextEditOutput.clear()

    @pyqtSlot()
    def __slot_refresh_database(self):
        self.cmds_map = json.load(open('cmds.json'))
        self.sshwidgetui.comboBoxCmd.addItems(self.cmds_map.keys())

    def __init_cmdscombobox(self):
        self.cmds_map = json.load(open('cmds.json'))
        self.sshwidgetui.comboBoxCmd.addItems(self.cmds_map.keys())

    def __init_userinfo(self):
        userinfo_map = json.load(open('userinfo.json'))
        self.sshwidgetui.lineEditServerIP.setText(userinfo_map.get('ServerIP'))
        self.sshwidgetui.lineEditUser.setText(userinfo_map.get('User'))
        self.sshwidgetui.lineEditPassword.setText(userinfo_map.get('Password'))