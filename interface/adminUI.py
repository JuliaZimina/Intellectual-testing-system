from interface.LogIn import *
from interface.Windows.adminWindow import *
from interface.Windows.DialogWindows.banWindow import *
from interface.Windows.DialogWindows.statusWindow import *
from interface.Windows.DialogWindows.userRecoveryWindow import *
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
        self.questionManager()
        # self.statistics()
        # userInformation(self)
        # statistics(self)
        self.setFixedSize(650, 500)

    def userManager(self):
        self.userListLabel.setText(printUserInfo(users))
        self.changeStatusButton.clicked.connect(self.openStatusWindow)
        self.BlockButton.clicked.connect(self.openBanWindow)
        self.changePasswordButton.clicked.connect(self.openRecoveryWinow)

    def statistics(self):
        self.statisticLabel.setText(self.user.getStatistics())
        # подключить кнопку

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

    def openStatusWindow(self):
        self.Open = RoleWin()
        self.Open.show()

    def openBanWindow(self):
        self.Open = BanWin()
        self.Open.show()

    def openRecoveryWinow(self):
        self.Open = UserRecoveryWin()
        self.Open.show()

    def questionManager(self):
        self.groupsOfQuestionsBox.addItems(groups_of_questions)
        group = self.groupsOfQuestionsBox.currentText()
        self.questionsComboBox.addItems(tests[group].keys())
        self.groupsOfQuestionsBox.currentTextChanged.connect(self.changeQuestions)
        self.editQuestionButton.clicked.connect(self.openEditQuestionWindow)
        self.deleteQuestionButton.clicked.connect(users.)


    def changeQuestions(self):
        self.questionsComboBox.clear()
        group = self.groupsOfQuestionsBox.currentText()
        self.questionsComboBox.addItems(tests[group].keys())

    def openEditQuestionWindow(self):
        pass


class BanWin(Ui_BanWindow, QtWidgets.QMainWindow):
    def __init__(self, admin, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.admin = admin
        self.setupUi(self)
        self.loginBox.addItems(list(users.keys()))
        self.banButton.clicked.connect(admin.block_user(str(self.loginBox.currentText())), str(self.reasonLine.text()))


class RoleWin(Ui_updateRoleWindow, QtWidgets.QMainWindow):
    def __init__(self, admin, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.admin = admin
        self.loginBox.addItems(list(users.keys()))
        self.changeStatusButton.clicked.connect(admin.roles(str(self.loginBox.currentText())),
                                                str(self.statusBox.currentText()))


class UserRecoveryWin(Ui_UnblockUserWindow, QtWidgets.QMainWindow):
    def __init__(self, admin, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.admin = admin
        self.userListLabel.setText(printUserInfo(recovery_requests))
        self.loginBox.addItems(list(recovery_requests.keys()))
        self.changeStatusButton.clicked.connect(admin.return_access(str(self.loginBox.currentText())))
