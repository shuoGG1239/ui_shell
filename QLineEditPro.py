from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QFileInfo


class QLineEditPro(QLineEdit):
    """
    增强版QlineEdit: 能接收拖拽过来的文件并将文本set为路径
    """
    def __init__(self, *__args):
        super(QLineEditPro, self).__init__(*__args)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if (event.mimeData().hasUrls()):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if (event.mimeData().hasUrls()):
            event.acceptProposedAction()

    def dropEvent(self, event):
        if (event.mimeData().hasUrls()):
            urlList = event.mimeData().urls()
            fileInfo = QFileInfo(urlList[0].toLocalFile())
            self.setText(fileInfo.filePath())
            event.acceptProposedAction()
