# from Classes.administrator import *
from interface.LogIn import *
from interface.Windows.adminWindow import *
from interface.Windows.DialogWindows.banWindow import *
from interface.Windows.DialogWindows.statusWindow import *
from interface.Windows.DialogWindows.userRecoveryWindow import *
from PyQt5 import QtWidgets

from interface.Windows.editQuestionWindow import *
from interface.templateUserUI import *
from interface.questionWindowUI import QuestionWin


class AdminWin(Ui_AdminWindow, QtWidgets.QMainWindow):

    def __init__(self, user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user = user
        self.testing()
        self.questionManager()
        self.statistics()
        self.userInformation()
        self.setFixedSize(650, 500)

    def userInformation(self):
        self.nameLine.setText(self.user.getName())
        self.surnameLine.setText(self.user.getSurname())
        self.faternityLine.setText(self.user.getFatherName())
        self.passwordLineEdit.setText(self.user.getPassword())
        date = self.user.getDateOfBirth()
        self.dateOfBirth.setDate(QtCore.QDate(date.day, date.month, date.year))
        question = [self.user.getSecretQuestion()]
        questions = question + [x for x in secret_questions if x != question[0]]
        self.question.addItems(questions)
        self.answerLine.setText(self.user.getSecretAnswer())
        self.emailLine.setText(self.user.getEmail())
        self.phoneLine.setText(self.user.getPhoneNumber())
        self.acceptChangesButton.clicked.connect(self.makeChanges)

    def makeChanges(self):
        try:
            self.user.setPassword(self.passwordLineEdit.text())
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


    def statistics(self):
        self.statisticLabel.setText(self.user.getStatistics())
        self.viewGraphicsButton.clicked.connect(self.openGraphicsWindow())

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


    def questionManager(self):
        self.groupsOfQuestionsBox.addItems(groups_of_questions)
        group = self.groupsOfQuestionsBox.currentText()
        self.questionsComboBox.addItems(tests[group].keys())
        self.groupsOfQuestionsBox.currentTextChanged.connect(self.changeQuestions)

        self.editQuestionButton.clicked.connect(self.openEditQuestionWindow)
        '''
        self.deleteQuestionButton.clicked.connect(
            self.user.deleteQuestion(self.groupsOfQuestionsBox.currentText(), self.questionsComboBox.currentText()))

        self.deleteGroupOfQuestionsButton.clicked.connect(self.user.deleteGroup(self.groupsOfQuestionsBox.currentText()))
        self.hideQuestionButton.clicked.connect(
            self.user.hideQuestion(self.groupsOfQuestionsBox.currentText(), self.questionsComboBox.currentText()))
        self.hideGroupOfQuestionsButton.clicked.connect(self.user.hideGroup(self.groupsOfQuestionsBox.currentText()))
        self.editQuestionButton.clicked.connect(self.openEditQuestionWindow)
        self.AddQuestionButton.clicked.connect(self.openAddQuestionWindow)
    '''

    def changeQuestions(self):
        self.questionsComboBox.clear()
        group = self.groupsOfQuestionsBox.currentText()
        self.questionsComboBox.addItems(tests[group].keys())

    def openEditQuestionWindow(self):
        self.Open = EditQuestionWin(True, self.user, self.group, self.question)
        self.Open.show()

    def openAddQuestionWindow(self):
        self.Open = EditQuestionWin(False, self.user, self.group, self.question)
        self.Open.show()

    def openGraphicsWindow(self):
        pass





class EditQuestionWin(Ui_EditQuestionWindow, QtWidgets.QMainWindow):
    def __init__(self, edit, admin, group="", question="", parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.admin = admin
        self.edit = edit
        self.group = group
        self.question = question
        self.setupUi(self)

        if edit:
            self.editQuestion()
        self.sendQuestionEdit.clicked.connect(self.sendEdit)

    def editQuestion(self):
        self.themeLine.setText(self.group)
        self.questionLine.setText(self.question)
        self.answerLine.setText(tests[self.group][self.question]["ответ"][0])
        self.incorrectAnswersLine.setText(printIncorrectAnswers())
        self.timespinBox.setValue(tests[self.group][self.question]["время"])

    def sendEdit(self):
        new_theme = self.themeLine.Text()
        new_question = self.questionLine.Text()
        answer = self.answerLine.Text()
        incorrectAnswers = self.incorrectAnswersLine.Text(printIncorrectAnswers()).split(";")
        time = str(self.timespinBox.Value())
        if self.edit:
            self.admin.editQuestion(self.group, self.question, new_theme, new_question, answer, incorrectAnswers, time)
        else:
            self.admin.addQuestion(new_theme, new_question, answer, incorrectAnswers, time)

