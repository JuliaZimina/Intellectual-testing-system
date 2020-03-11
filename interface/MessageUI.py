
from interface.Windows.messageWindow import *

from PyQt5 import QtWidgets

class MessageWin(QtWidgets.QMainWindow, Ui_MessageWindow):
    def __init__(self, message,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.messageLabel.setText(str(message))
