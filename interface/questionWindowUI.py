from interface.Windows.questionWindow import *
from Classes.test import *

from PyQt5 import QtWidgets

from interface.Windows.resultWindow import *

from datetime import datetime
import time


class QuestionWin(QtWidgets.QMainWindow, Ui_questionWindow):

    def __init__(self, theme,user, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.theme = theme
        self.answers = ""
        self.current_test=Test(self.theme,user)
        self.start_time=datetime.now()
        self.answerButton.clicked.connect(self.sendAnswer)
        #self.setFixedSize(1200, 500)
        try:
            self.test()
        except Exception as e:
            print(str(e))
        #self.answerButton.clicked.connect(self.test)

    def test(self):
        #while not self.current_test.endTest():
        self.start_time = datetime.now()
        self.questionLabel.setText(self.getNextQuestion())
        #self.answerButton.clicked.connect(self.sendAnswer)


    def getNextQuestion(self):
        a = self.current_test.getNextQuestion()
        self.answers = [x for x in a[1]["ответ"]]
        import random
        random.shuffle(self.answers)
        answers_string = ""
        if len(self.answers) > 1:
            for i in range(len(self.answers)):
                answers_string = answers_string + str(i + 1) + "." + self.answers[i] + "\n"
        question = a[0] + "\n" + answers_string
        return question

    def sendAnswer(self):
        end_time = datetime.now()
        answer = self.answerlineEdit.text()
        if len(self.answers) > 1:
            if answer.isdigit():
                answer = int(answer)
                if answer > 0 and answer <= len(self.answers):
                    answer = self.answers[answer - 1]
        try:
            self.current_test.sendAnswer(str(answer), (end_time-self.start_time).total_seconds())
        except Exception as e:
            print(e)
        if self.current_test.endTest():
            self.close()
            self.Open = ResultWin(self.current_test)
            self.Open.show()
        else:
            self.test()



class ResultWin(QtWidgets.QMainWindow, Ui_ResultWindow):

    def __init__(self, test, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.test = test
        try:
            self.resultLabel.setText(test.getResult())
        except Exception as e:
            print(e)