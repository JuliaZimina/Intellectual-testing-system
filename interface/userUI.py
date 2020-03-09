from dataProcessing import *
from interface.LogIn import *
from interface.templateUserUI import *
from interface.Windows.userWindow import *

from PyQt5 import QtWidgets

from interface.questionWindowUI import QuestionWin
from interface.templateUserUI import userInformation


# from interface.templateUserUI import testing

class UserWin(QtWidgets.QMainWindow, Ui_UserWindow):

    def __init__(self, current_user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.user = current_user
        self.setupUi(self)
        self.testing()
        # userInformation(self)
        # statistics(self)
        self.setFixedSize(650, 500)

    def testing(self):
        self.questionThemeComboBox.addItems(groups_of_questions)
        self.themeTestButton.clicked.connect(self.openThemeQuestionWindow)
        #if self.user.getGeneralTestCounter() >= 3:
        a=1
        if a==0:
            self.genetalTestButton.setDisabled(True)
        else:
            self.genetalTestButton.clicked.connect(self.openGeneralQuestionWindow)

    def openThemeQuestionWindow(self):
        self.Open = QuestionWin(str(self.questionThemeComboBox.currentText()))
        self.Open.show()

    def openGeneralQuestionWindow(self):
        self.Open = QuestionWin("general")
        self.Open.show()