from interface.LogIn import *
from interface.Windows.registrationWindow import *
from interface.Windows.userWindow import *
from Classes.registration import *

from PyQt5 import QtWidgets


class UserWin(QtWidgets.QMainWindow, Ui_UserWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.setFixedSize(500, 500)
        #self.registerButton.clicked.connect(self.registrationUI)