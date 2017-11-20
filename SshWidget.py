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
        self.sshwidgetui.pushButtonGo.clicked.connect(self.__slot_execute_selmode)
        self.sshwidgetui.pushButtonGoSingle.clicked.connect(self.__slot_execute_sinmode)
        self.sshwidgetui.pushButtonEdit.clicked.connect(self.__slot_edit)
        self.sshwidgetui.pushButtonClear.clicked.connect(self.__slot_clear)
        self.sshwidgetui.pushButtonRefresh.clicked.connect(self.__slot_refresh_database)
        self.sshwidgetui.comboBoxCmd.currentIndexChanged.connect(self.__shot_cmd_selected)
        self.__init_userinfo()
        self.__init_cmdscombobox()
        self.update_userinfo()
        self.sshwidgetui.lineEditArgs.setPlaceholderText('eg: 999,abc,8080')

    @pyqtSlot()
    def __slot_execute_selmode(self):
        current_cmd_real = self.cmds_map.get(self.sshwidgetui.comboBoxCmd.currentText())
        resultlist = re.findall(r'{}', current_cmd_real)
        if len(resultlist) > 0:
            argstext = self.sshwidgetui.lineEditArgs.text()
            arglist = argstext.split(',')
            if len(resultlist) != len(arglist):
                print('参数数量不匹配')
                return
            else:
                current_cmd_real = current_cmd_real.format(*arglist)
        self.sshwidgetui.plainTextEditOutput.appendPlainText('EXE: ' + current_cmd_real)
        self.update_userinfo()
        responselist = PM.exec_onecmd(self.ip, self.user, self.password, current_cmd_real)
        for cmd in responselist:
            self.sshwidgetui.plainTextEditOutput.appendPlainText(cmd)

    @pyqtSlot()
    def __slot_execute_sinmode(self):
        current_cmd_real = self.sshwidgetui.lineEditCmd.text()
        self.update_userinfo()
        responselist = PM.exec_onecmd(self.ip, self.user, self.password, current_cmd_real)
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

    @pyqtSlot(int)
    def __shot_cmd_selected(self, index):
        cmd_name = self.sshwidgetui.comboBoxCmd.currentText()
        cmd_text = self.cmds_map[cmd_name]
        if cmd_text.find(r"{}") > 0:
            self.sshwidgetui.lineEditArgs.setEnabled(True)
        else:
            self.sshwidgetui.lineEditArgs.setEnabled(False)

    def __init_cmdscombobox(self):
        self.cmds_map = json.load(open('cmds.json'))
        self.sshwidgetui.comboBoxCmd.addItems(self.cmds_map.keys())

    def __init_userinfo(self):
        userinfo_map = json.load(open('userinfo.json'))
        self.sshwidgetui.lineEditServerIP.setText(userinfo_map.get('ServerIP'))
        self.sshwidgetui.lineEditUser.setText(userinfo_map.get('User'))
        self.sshwidgetui.lineEditPassword.setText(userinfo_map.get('Password'))

    def update_userinfo(self):
        self.ip = self.sshwidgetui.lineEditServerIP.text()
        self.user = self.sshwidgetui.lineEditUser.text()
        self.password = self.sshwidgetui.lineEditPassword.text()

    def __del__(self):
        usermap = {'ServerIP': self.sshwidgetui.lineEditServerIP.text(),
                   'Password': self.sshwidgetui.lineEditPassword.text(),
                   'User': self.sshwidgetui.lineEditUser.text(),
                   }
        with open("userinfo.json", 'w', encoding='utf8') as json_file:
            json.dump(usermap, json_file, ensure_ascii=False)
