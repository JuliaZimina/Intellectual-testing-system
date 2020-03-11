# from Classes.administrator import *
from interface.LogIn import *
from interface.Windows.adminWindow import *
from interface.Windows.DialogWindows.banWindow import *
from interface.Windows.DialogWindows.statusWindow import *
from interface.Windows.DialogWindows.userRecoveryWindow import *
from dataProcessing import *

from interface.Windows.editQuestionWindow import *
from interface.questionWindowUI import QuestionWin


class AdminWin(Ui_AdminWindow, QtWidgets.QMainWindow):

    def __init__(self, user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user = user
        print("there")
        try:
            self.testing()
            self.userManager()
            self.questionManager()
            self.statistics()
            self.userInformation()
        except Exception as e:
            print("mistake")
            print(str(e),"d")

        self.setFixedSize(650, 500)

    def userInformation(self):
        print("here")
        self.passwordLineEdit.setText(self.user.getPassword())
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
        self.acceptChangesButton.clicked.connect(self.makeChanges)


    def makeChanges(self):
        try:
            self.user.setPassword(self.passwordLineEdit.text())
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

    def userManager(self):
        self.userListLabel.setText(printUserInfo(users))
        self.changeStatusButton.clicked.connect(self.openStatusWindow)
        self.BlockButton.clicked.connect(self.openBanWindow)
        self.changePasswordButton.clicked.connect(self.openRecoveryWinow)

    def statistics(self):
        self.statisticLabel.setText(self.user.getStatistics())
        self.viewGraphicsButton.clicked.connect(self.openGraphicsWindow)


    def testing(self):
        self.questionThemeComboBox.addItems(groups_of_questions)
        self.themeTestButton.clicked.connect(self.openThemeQuestionWindow)
        self.genetalTestButton.clicked.connect(self.openGeneralQuestionWindow)

    def openThemeQuestionWindow(self):
        self.Open = QuestionWin(str(self.questionThemeComboBox.currentText()),self.user)
        self.Open.show()

    def openGeneralQuestionWindow(self):
        self.Open = QuestionWin("general",self.user)
        self.Open.show()

    def openStatusWindow(self):
        try:
            self.Open = RoleWin(self.user)
            self.Open.show()
        except Exception as e:
            print(str(e))

    def openBanWindow(self):
        self.Open = BanWin(self.user)
        self.Open.show()

    def openRecoveryWinow(self):
        self.Open = UserRecoveryWin(self.user)
        self.Open.show()

    def questionManager(self):

        self.groupsOfQuestionsBox.addItems(groups_of_questions)

        group = self.groupsOfQuestionsBox.currentText()
        self.questionsComboBox.addItems(tests[group].keys())

        self.groupsOfQuestionsBox.currentTextChanged.connect(self.changeQuestions)
        self.editQuestionButton.clicked.connect(self.openEditQuestionWindow)

        self.deleteQuestionButton.clicked.connect(self.deleteQuestion)

        self.deleteGroupOfQuestionsButton.clicked.connect(self.deleteGroupOfQuestions)
        
        self.hideQuestionButton.clicked.connect(self.hideQuestion)
        self.hideGroupOfQuestionsButton.clicked.connect(self.hideGroupOfQuestions)
        self.editQuestionButton.clicked.connect(self.openEditQuestionWindow)
        self.AddQuestionButton.clicked.connect(self.openAddQuestionWindow)
    def reload(self):
        self.Open = AdminWin(self.user)
        self.close()
        self.Open.show()
    def deleteQuestion(self):
        self.user.deleteQuestion(self.groupsOfQuestionsBox.currentText(), self.questionsComboBox.currentText())
        self.reload()
    def deleteGroupOfQuestions(self):
        self.user.deleteGroup(self.groupsOfQuestionsBox.currentText())
        self.reload()
    def hideQuestion(self):
        self.user.hideQuestion(self.groupsOfQuestionsBox.currentText(), self.questionsComboBox.currentText())
        self.reload()
    def hideGroupOfQuestions(self):
        self.user.hideGroup(self.groupsOfQuestionsBox.currentText())
        self.reload()


    def changeQuestions(self):
        self.questionsComboBox.clear()
        group = self.groupsOfQuestionsBox.currentText()
        self.questionsComboBox.addItems(tests[group].keys())

    def openEditQuestionWindow(self):
        self.Open = EditQuestionWin(True, self.user, self.groupsOfQuestionsBox.currentText(), self.questionsComboBox.currentText())
        self.Open.show()

    def openAddQuestionWindow(self):
        self.Open = EditQuestionWin(False, self.user)
        self.Open.show()

    def openGraphicsWindow(self):
        pass


class BanWin(Ui_BanWindow, QtWidgets.QMainWindow):
    def __init__(self, admin, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.admin = admin
        self.setupUi(self)
        self.loginBox.addItems(list(users.keys()))
        self.banButton.clicked.connect(self.ban)
    def ban(self):
        self.admin.block_user(str(self.loginBox.currentText()), str(self.reasonLine.text()))
        self.reload()
    def reload(self):
        self.Open = AdminWin(self.admin)
        self.close()
        self.Open.show()


class RoleWin(Ui_updateRoleWindow, QtWidgets.QMainWindow):
    def __init__(self, admin, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.admin = admin
        self.loginBox.addItems(list(users.keys()))
        self.changeStatusButton.clicked.connect(self.changeStatus)
    def changeStatus(self):
        self.admin.roles(str(self.loginBox.currentText()),
                        str(self.statusBox.currentText()))
        self.reload()
    def reload(self):
        self.Open = AdminWin(self.admin)
        self.close()
        self.Open.show()



class UserRecoveryWin(Ui_UnblockUserWindow, QtWidgets.QMainWindow):
    def __init__(self, admin, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.admin = admin
        self.userListLabel.setText(printUserInfo(recovery_requests))
        self.loginBox.addItems(list(recovery_requests.keys()))
        self.changeStatusButton.clicked.connect(self.returnAccess)
    def returnAccess(self):
        self.admin.return_access(str(self.loginBox.currentText()))
        self.reload()
    def reload(self):
        self.Open = AdminWin(self.admin)
        self.close()
        self.Open.show()




class EditQuestionWin(Ui_EditQuestionWindow, QtWidgets.QMainWindow):
    def __init__(self, edit, admin, group="", question="", parent=None):
        try:
            QtWidgets.QWidget.__init__(self, parent)
            self.admin = admin
            self.edit = edit
            self.group = group
            self.question = question
            self.setupUi(self)
            if edit:
                self.editQuestion()
            self.sendQuestionEdit.clicked.connect(self.sendEdit)
        except Exception as e:
            print(str(e))


    def editQuestion(self):
        self.themeLine.setText(self.group)
        self.questionLine.setText(self.question)
        self.answerLine.setText(tests[self.group][self.question]["ответ"][0])
        self.incorrectAnswersLine.setText(printIncorrectAnswers(self.group,self.question))
        self.timespinBox.setValue(int(tests[self.group][self.question]["время"]))

    def sendEdit(self):
        new_theme = self.themeLine.text()
        new_question = self.questionLine.text()
        answer = self.answerLine.text()
        incorrectAnswers = self.incorrectAnswersLine.text().split(";")
        time = str(self.timespinBox.value())
        try:
            if self.edit:
                self.admin.editQuestion(self.group, self.question, new_theme, new_question, answer, incorrectAnswers, time)
            else:
                self.admin.addQuestion(new_theme, new_question, answer, incorrectAnswers, time)
        except Exception as e:
            print(str(e))
