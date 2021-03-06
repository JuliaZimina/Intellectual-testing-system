from interface.LogIn import *
from interface.MessageUI import *
from interface.Windows.registrationWindow import *
from Classes.registration import *

from PyQt5 import QtWidgets


class RegistrationWin(QtWidgets.QMainWindow, Ui_RegistrationWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # self.setFixedSize(500, 500)
        try:
            self.registerButton.clicked.connect(self.registrationUI)
            self.question.clear()
            self.question.addItems(secret_questions)
        except Exception as e:
            print(str(e))

    def registrationUI(self):

        try:

            registration(login=self.loginLine.text(), password=self.passwordLine.text(), name=self.nameLine.text(),
                         surname=self.surnameLine.text(), father_name=self.faternityLine.text(),
                         date_of_birth=self.dateOfBirth.text(), group=self.group.currentText(),
                         secret_question=self.question.currentText(), answer=self.answerLine.text(),
                         email=self.emailLine.text(), tel=self.phoneLine.text())
            self.close()
            self.Open = MessageWin("Вы успешно зарегистрировались")
            self.Open.show()


        except Exception as e:
            self.errorLabel.setText(str(e))
            print(e)

    def closeEvent(self, event):
        write_users_info('Data/UsersInfo/users.sys', users)
