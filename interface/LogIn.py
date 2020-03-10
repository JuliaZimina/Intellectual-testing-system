from interface.Windows.DialogWindows.changePasswordWindow import *
from interface.Windows.DialogWindows.recoveryRequestWindow import Ui_RecoveryRequest
from interface.Windows.DialogWindows.secretQuestionWindow import *
from interface.Windows.logInWindow import *
#from Classes.registration import *
from interface.adminUI import *
from interface.registrationUI import *

from PyQt5 import QtWidgets

from interface.userUI import *




class LogInWin(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_LogIn()
        self.ui.setupUi(self)
        self.setFixedSize(500, 500)
        self.attempts=0
        # кнопка входа
        self.ui.logInButton.clicked.connect(self.logInUI)
        # кнопка регистрации
        self.ui.unregisteredButton.clicked.connect(self.registrationUI)

    # обработка входа
    def logInUI(self):
        login = self.ui.loginLine.text()
        password = self.ui.passwordLine.text()
        try:
            #user = logIn(login, password)
            self.close()
            self.Open = UserWin("user")
            #self.Open = AdminWin("user")
            self.Open.show()
            # открыть следующее окно
        except Exception as e:
            self.ui.errorLabel.setText(str(e))
            self.attempts += 1
            if self.attempts > 3:
                user = tmpLogIn(login)
                self.close()
                self.Open=SecretQuestionWin(user)
                self.Open.show()


    def registrationUI(self):
        self.close()
        self.Open = RegistrationWin()
        self.Open.show()

class SecretQuestionWin(QtWidgets.QMainWindow,Ui_SecretQuestionWindow):


    def __init__(self,user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user=user
        self.secretQuestionLabel.setText(self.user.getSecretQuestion())
        self.answerButton.clicked.connect(self.checkSecretAnswer)

    def checkSecretAnswer(self):
        answer = self.answerLine.text()
        try:
            checkSecretAnswer(self.user.getLogin(), answer)
            self.openChangePasswordWindow()
        except Exception as e:
            self.openMakeRecoveryRequestWindow(self)

    def openMakeRecoveryRequestWindow(self):
        self.close()
        self.Open=RecoveryRequestWin(self.user)
        self.Open.show()

    def openChangePasswordWindow(self):
        self.close()
        self.Open = ChangePasswordWin(self.user)
        self.Open.show()



class RecoveryRequestWin(QtWidgets.QMainWindow,Ui_RecoveryRequest):
    def __init__(self,user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user=user
        self.registerButton.clicked.connect(self.sendRecovery())

    def sendRecovery(self):
        recoveryRequest(login=self.user.getLogin(), password=self.passwordLine.text(), name=self.nameLine.text(),
                     surname=self.surnameLine.text(), father_name=self.faternityLine.text(),
                     date_of_birth=self.dateOfBirth.text(), group=self.group.currentText(),
                     secret_question=self.question.currentText(), answer=self.answerLine.text(),
                     email=self.emailLine.text(), tel=self.phoneLine.text())
        self.close()


class ChangePasswordWin(QtWidgets.QMainWindow,Ui_ChangePasswordWindow):

    def __init__(self,user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user=user
        self.resetPasswordButton.clicked.connect(self.changePassword)

    def changePassword(self):
        try:
            changePassword(self.user.getLogin(),self.passwordLine.text())
            self.close()
            self.Open = LogInWin()
            self.Open.show()
        except Exception as e:
            self.errorLabel.setText(str(e))