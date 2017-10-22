from PyQt5.QtWidgets import QApplication
import SshWidget
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = SshWidget.SshWidget()
    mainWindow.show()
    sys.exit(app.exec_())