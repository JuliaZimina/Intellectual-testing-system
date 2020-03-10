from interface.Windows.questionWindow import *
from Classes.test import *

from PyQt5 import QtWidgets

from interface.Windows.resultWindow import *

from datetime import datetime
import time


class QuestionWin(QtWidgets.QMainWindow, Ui_questionWindow):

    def __init__(self, theme, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.theme = theme
        self.answers = ""
        try:
            self.test()
        except Exception as e:
            print(str(e))
        #self.answerButton.clicked.connect(self.test)

    def test(self):
        current_test = Test(self.theme)
        while not current_test.endTest():
            start_time = datetime.now()
            self.questionLabel.setText(self.getNextQuestion(current_test))
            self.answerButton.clicked.connect(self.sendAnswer(current_test, start_time))
        self.close()
        self.Open = ResultWin(current_test)
        self.Open.show()

    def getNextQuestion(self, test):
        a = test.getNextQuestion()
        self.answers = [x for x in a[1]["ответ"]]
        import random
        random.shuffle(self.answers)
        answers_string = ""
        if len(self.answers) > 1:
            for i in range(len(self.answers)):
                answers_string = answers_string + str(i + 1) + "." + self.answers[i] + "\n"
        else:
            answers_string = self.answers[0]
        question = a[0] + "\n" + answers_string
        return question

    def sendAnswer(self, test, start_time):
        end_time = datetime.now()
        answer = self.answerlineEdit.text()
        if len(self.answers) > 1:
            if answer.isdigit():
                answer = int(answer)
                if answer > 0 and answer <= len(answer):
                    answer = self.answers[answer - 1]
        test.sendAnswer(answer, start_time - end_time)


class ResultWin(QtWidgets.QMainWindow, Ui_ResultWindow):

    def __init__(self, test, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.test = test
        self.resultLabel.setText(test.getResult())
