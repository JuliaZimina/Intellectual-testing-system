from interface.LogIn import *
from interface.Windows.adminWindow import *
from Classes.registration import *
from interface.userUI import *
from PyQt5 import QtWidgets


class AdminWin(QtWidgets.QMainWindow,Ui_AdminWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.setFixedSize(500, 500)
        #self.registerButton.clicked.connect(self.registrationUI)