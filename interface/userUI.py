import datetime

from Classes.templateUser import TemplateUser
from interface.Windows.userWindow import *
from PyQt5 import QtWidgets
from dataProcessing import *
from interface.questionWindowUI import QuestionWin


# from interface.templateUserUI import testing

class UserWin(QtWidgets.QMainWindow, Ui_UserWindow):

    def __init__(self, current_user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        print("use win")
        self.user = current_user
        self.setupUi(self)
        self.testing()
        self.userInformation()
        self.statistics()
        self.setFixedSize(650, 500)

    def testing(self):
        self.questionThemeComboBox.addItems(groups_of_questions)
        self.themeTestButton.clicked.connect(self.openThemeQuestionWindow)

        if self.user.getGeneralTestCounter() >= 3:
            self.genetalTestButton.setDisabled(True)
        else:
            self.genetalTestButton.clicked.connect(self.openGeneralQuestionWindow)

    def openThemeQuestionWindow(self):
        self.Open = QuestionWin(str(self.questionThemeComboBox.currentText()))
        self.Open.show()

    def openGeneralQuestionWindow(self):
        self.Open = QuestionWin("general")
        self.Open.show()


    def userInformation(self):
        self.passwordlineEdit.setText(self.user.getPassword())
        self.nameLine.setText(self.user.getName())
        self.surnameLine.setText(self.user.getSurname())
        self.faternityLine.setText(self.user.getFatherName())
        self.dateOfBirthLine.setText(self.user.getDateOfBirth())
        question = [self.user.getSecretQuestion()]
        questions = question + [x for x in secret_questions if x != question[0]]
        self.question.addItems(questions)
        self.answerLine.setText(self.user.getSecretAnswer())
        self.emailLine.setText(self.user.getEmail())
        self.phoneLine.setText(self.user.getPhoneNumber())
        self.accceptChangesButton.clicked.connect(self.makeChanges)
        self.deleteUserButton.clicked.connect(self.deleteUser)

    def statistics(self):
        self.statisticsLabel.setText(self.user.getStatistics())


    def deleteUser(self):
        self.user.deleteUser()
        self.close()

    def makeChanges(self):
        try:

            self.user.setPassword(self.passwordlineEdit.text())
            self.user.setName(self.nameLine.text())
            self.user.setSurname(self.surnameLine.text())
            self.user.setFatherName(self.faternityLine.text())
            self.user.setDateOfBirth(self.dateOfBirthLine.text())
            self.user.setGroup(self.group.currentText())
            self.user.setSecretQuestion(self.question.currentText())
            self.user.setSecretAnswer(self.answerLine.text())
            self.user.setEmail(self.emailLine.text())
            self.user.setPhoneNumber(self.phoneLine.text())

        except Exception as e:
            self.errorChangesLabel.setText(str(e))

