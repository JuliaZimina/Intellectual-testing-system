from dataProcessing import *
from interface.LogIn import *
from interface.questionWindowUI import QuestionWin
def testing(self):
    self.questionThemeComboBox.addItems(groups_of_questions)
    self.themeTestButton.clicked.connect(openThemeQuestionWindow(self))
    self.genetalTestButton.clicked.connect(openGeneralQuestionWindow(self))

def userInformation(self):
    self.nameLine.setText(self.user.getName())
    self.surnameLine.setText(self.user.getSurname())
    self.faternityLine.setText(self.user.getFatherName())
    date = self.user.getDateOfBirth()
    self.dateOfBirth.setDate(QtCore.QDate(date.day, date.month, date.year))
    question = [self.user.getSecretQuestion()]
    questions = question + [x for x in secret_questions if x != question[0]]
    self.question.addItems(question)
    self.answerLine.setText(self.user.getSecretAnswer())
    self.emailLine.setText(self.user.getEmail())
    self.phoneLine.setText(self.user.getPhoneNumber())
    self.accceptChangesButton.clicked.connect(self.makeChanges)
    self.deleteUserButton.clicked.connect(self.delteUser)


def statistics(self):
    self.statisticsLabel.setText(self.user.getStatistics())


def openQuestionWindow(self, theme):
    question = QuestionWin()
    question.show()


def delteUser(self):
    del self.user
    self.close()


def makeChanges(self):
    try:
        self.user.setName(self.nameLine.text())
        self.user.setSurname(self.surnameLine.text())
        self.user.setFatherName(self.faternityLine.text())
        self.user.setDateOfBirth(self.dateOfBirth.text())
        self.user.setGroup(self.group.currentText())
        self.user.setSecretQuestion(self.question.currentText())
        self.user.setSecretAnswer(self.answerLine.text())
        self.user.setEmail(self.emailLine.text())
        self.user.setPhoneNumber(self.phoneLine.text())
    except Exception as e:
        self.errorChangesLabel.setText(str(e))

def openThemeQuestionWindow(self):
    self.Open = QuestionWin(str(self.questionThemeComboBox.currentText()))
    self.Open.show()


def openGeneralQuestionWindow(self):
    self.Open = QuestionWin("general")
    self.Open.show()
