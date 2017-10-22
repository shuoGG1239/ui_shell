from PyQt5.QtCore import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
import sys

app, browser = None, None


class BrowserScreen(QWebView):
    '''''主窗口'''
    def __init__(self):
        QWebView.__init__(self)
        self.resize(800, 600)
        self.show()
        self.setHtml(open('baidupan.html','rb').read().decode('utf8'))
        #self.load(QUrl(r'http://www.g.cn'))

    def showMessage(self, msg):
        print(msg)


class PythonJS(QObject):
    '''''供js调用'''
    # __pyqtSignals__ = ("contentChanged(const QString &)")
    contentChanged = pyqtSignal(str)

    @pyqtSlot()
    def shuogg(self):
        print('123123')

    @pyqtSlot()
    def send_js_signal(self):
        self.browser.page().mainFrame().evaluateJavaScript("test()")

    def close(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = BrowserScreen()
    # 供js调用的python对象
    pjs = PythonJS()
    # 绑定通信对象
    browser.setWindowTitle("Shell SSH")
    browser.page().mainFrame().addToJavaScriptWindowObject("python", pjs)
    # browser.settings().setAttribute(QWebSettings.LocalStorageEnabled, True)
    # browser.settings().setLocalStoragePath("static/")
    pjs.contentChanged.connect(browser.showMessage)
    pjs.browser = browser
    sys.exit(app.exec_())