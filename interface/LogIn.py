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
                # открыть окно восстановления пароля


    # обработка восстановления пароля
    def processPasswordRecovery(self):
        print("1")
        pass

    def registrationUI(self):
        self.close()
        self.Open = RegistrationWin()
        self.Open.show()

class SecretQuestionWin(QtWidgets.QMainWindow,Ui_SecretQuestionWindow):


    def __init__(self,user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui.setupUi(self)
        self.user=user
        self.secretQuestionLabel.setText(self.user.getSecretQuestion())


        self.answerButton.clicked.connect(self.checkSecretAnswer)

    def checkSecretAnswer(self):
        answer = self.answerLine.text()
        try:
            checkSecretAnswer(self.user.getLogin(), answer)
            self.openChangePasswordWindow()
        except Exception as e:
            self.openMakeRecoveryRequestWindow()

    def openMakeRecoveryRequestWindow(self):
        pass

    def openChangePasswordWindow(self):
        pass



