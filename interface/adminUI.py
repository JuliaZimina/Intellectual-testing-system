from interface.LogIn import *
from interface.Windows.adminWindow import *
from Classes.registration import *
from interface.userUI import *
from PyQt5 import QtWidgets
from interface.templateUserUI import *
from interface.questionWindowUI import QuestionWin


class AdminWin(Ui_AdminWindow, QtWidgets.QMainWindow):

    def __init__(self, user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user = user
        self.testing()
        self.userManager()
        self.statistics()
        # userInformation(self)
        # statistics(self)
        self.setFixedSize(650, 500)

    def userManager(self):
        self.userListLabel.setText(printUserInfo())



    def statistics(self):
        self.statisticLabel.setText(self.user.getStatistics())
        #подключить кнопку

    def testing(self):
        self.questionThemeComboBox.addItems(groups_of_questions)
        self.themeTestButton.clicked.connect(self.openThemeQuestionWindow)
        self.genetalTestButton.clicked.connect(self.openGeneralQuestionWindow)

    def openThemeQuestionWindow(self):
        self.Open = QuestionWin(str(self.questionThemeComboBox.currentText()))
        self.Open.show()

    def openGeneralQuestionWindow(self):
        self.Open = QuestionWin("general")
        self.Open.show()
class BanWin(Ui_AdminWindow, QtWidgets.QMainWindow):