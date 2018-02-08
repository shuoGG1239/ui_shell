import json
import os
import re
import threading

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QFileDialog
from shuogg import ftp_util
from shuogg import ssh_util

from CmdFileDialog import CmdFileDialog
from ui_SshWidget import Ui_SshWidget


class SshWidget(QWidget):
    def __init__(self):
        super(SshWidget, self).__init__()
        self.sshwidgetui = Ui_SshWidget()
        self.sshwidgetui.setupUi(self)
        self.sshwidgetui.pushButtonGo.clicked.connect(self.__slot_execute_select_mode)
        self.sshwidgetui.pushButtonGoSingle.clicked.connect(self.__slot_execute_console_mode)
        self.sshwidgetui.comboBoxCmd.currentIndexChanged.connect(self.__slot_cmd_selected)
        self.sshwidgetui.progressBarFtp.setRange(0, 1)
        self.sshwidgetui.progressBarFtp.setValue(0)
        self.__init_userinfo()
        self.__init_ftpinfo()
        self.__init_cmdscombobox()
        self.update_userinfo()
        self.sshwidgetui.lineEditArgs.setPlaceholderText('eg: 999,abc,8080')
        self.setAcceptDrops(True)

    def closeEvent(self, e):
        """
        关闭窗口前保存用户信息和ftp文件路径信息
        :param e:
        :return:
        """
        self.update_userinfo()
        self.update_ftpinfo()
        open('userinfo.json', 'wb').write(bytes(json.dumps(self.userinfo_map, ensure_ascii=False), encoding='utf8'))
        open('ftpinfo.json', 'wb').write(bytes(json.dumps(self.ftpinfo_map, ensure_ascii=False), encoding='utf8'))

    @pyqtSlot()
    def __slot_execute_select_mode(self):
        """
        选择命令模式
        :return:
        """
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
        self.sshwidgetui.plainTextEditOutput.appendPlainText('EXE: ' + current_cmd_real)
        self.update_userinfo()
        responselist = ssh_util.exec_cmd(self.ip, self.user, self.password, current_cmd_real)
        for cmd in responselist:
            self.sshwidgetui.plainTextEditOutput.appendPlainText(cmd)

    @pyqtSlot()
    def __slot_execute_console_mode(self):
        """
        手动输入命令行模式
        :return:
        """
        current_cmd_real = self.sshwidgetui.lineEditCmd.text()
        self.update_userinfo()
        responselist = ssh_util.exec_cmd(self.ip, self.user, self.password, current_cmd_real)
        for cmd in responselist:
            self.sshwidgetui.plainTextEditOutput.appendPlainText(cmd)

    @pyqtSlot()
    def on_pushButtonEdit_clicked(self):
        """
        打开编辑命令界面
        :return:
        """
        cmdwindow = CmdFileDialog()
        # 如果是save进来的则更新droplist
        if cmdwindow.exec() == 1:
            self.__slot_refresh_database()

    @pyqtSlot()
    def on_pushButtonClear_clicked(self):
        """
        清除输出框
        :return:
        """
        self.sshwidgetui.plainTextEditOutput.clear()

    @pyqtSlot()
    def on_pushButtonRefresh_clicked(self):
        """
        刷新命令列表
        :return:
        """
        self.sshwidgetui.comboBoxCmd.clear()
        self.cmds_map = json.load(open('cmds.json'))
        self.sshwidgetui.comboBoxCmd.addItems(self.cmds_map.keys())

    @pyqtSlot(int)
    def __slot_cmd_selected(self, index):
        """
        下拉框被选择时触发
        :param index:
        :return:
        """
        cmd_name = self.sshwidgetui.comboBoxCmd.currentText()
        cmd_text = self.cmds_map[cmd_name]
        if cmd_text.find(r"{}") > 0:
            self.sshwidgetui.lineEditArgs.setEnabled(True)
        else:
            self.sshwidgetui.lineEditArgs.setEnabled(False)

    @pyqtSlot()
    def on_pushButtonOpen_clicked(self):
        """
        打开windows文件选择框
        :return:
        """
        url = QFileDialog.getOpenFileName(self)[0]
        if (url != ''):
            self.sshwidgetui.lineEditServerSrcFile.setText(url)

    @pyqtSlot()
    def on_pushButtonUpload_clicked(self):
        """
        开始上传
        :return:
        """
        src_file_path = self.sshwidgetui.lineEditServerSrcFile.text()
        dst_file_path = self.sshwidgetui.lineEditServerDstFile.text()
        self.t1 = threading.Thread(target=self.__upload_one, args=(src_file_path, dst_file_path, self.__ftp_callback))
        self.t1.start()

    def __upload_one(self, src_file_path, dst_file_path, ftp_callback):
        """
        上传一个文件
        :param src_file_path:
        :param dst_file_path:
        :param ftp_callback:
        :return:
        """
        if src_file_path == '' or dst_file_path == '':
            return
        src_dir, src_file_name = os.path.split(src_file_path)
        self.sshwidgetui.plainTextEditOutput.setPlainText('Start upload file:' + src_file_name)
        ftp = ftp_util.FTP(self.ip, self.user, self.password)
        ftp.upload_one(src_file_path, dst_file_path, self.__ftp_callback)
        ftp.close()

    def __ftp_callback(self, so_far, total):
        """
        Ftp回调,更新进度条
        :param so_far:
        :param total:
        :return:
        """
        self.sshwidgetui.progressBarFtp.setRange(0, total)
        self.sshwidgetui.progressBarFtp.setValue(so_far)

    def __init_cmdscombobox(self):
        self.cmds_map = json.load(open('cmds.json', encoding='utf8'))
        self.sshwidgetui.comboBoxCmd.addItems(self.cmds_map.keys())

    def __init_userinfo(self):
        self.userinfo_map = json.load(open('userinfo.json', encoding='utf8'))
        self.sshwidgetui.lineEditServerIP.setText(self.userinfo_map.get('ServerIP'))
        self.sshwidgetui.lineEditUser.setText(self.userinfo_map.get('User'))
        self.sshwidgetui.lineEditPassword.setText(self.userinfo_map.get('Password'))

    def __init_ftpinfo(self):
        self.ftpinfo_map = json.load(open('ftpinfo.json', encoding='utf8'))
        self.sshwidgetui.lineEditServerSrcFile.setText(self.ftpinfo_map.get('srcfile'))
        self.sshwidgetui.lineEditServerDstFile.setText(self.ftpinfo_map.get('dstfile'))

    def update_userinfo(self):
        self.ip = self.sshwidgetui.lineEditServerIP.text()
        self.user = self.sshwidgetui.lineEditUser.text()
        self.password = self.sshwidgetui.lineEditPassword.text()
        self.userinfo_map['ServerIP'] = self.ip
        self.userinfo_map['User'] = self.user
        self.userinfo_map['Password'] = self.password

    def update_ftpinfo(self):
        self.ftpinfo_map['srcfile'] = self.sshwidgetui.lineEditServerSrcFile.text()
        self.ftpinfo_map['dstfile'] = self.sshwidgetui.lineEditServerDstFile.text()
