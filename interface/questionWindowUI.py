from interface.Windows.questionWindow import *
from Classes.test import *

from PyQt5 import QtWidgets

from interface.Windows.resultWindow import *


class QuestionWin(QtWidgets.QMainWindow, Ui_questionWindow):

    def __init__(self, theme, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.theme = theme
        self.answerButton.clicked.connect(self.test)

    def test(self):
        current_test = Test(self.theme)
        while not current_test.end_of_test:
            self.questionLabel.set(current_test.getNextQuestion())
            answer = self.answerlineEdit.text()
            self.answerButton.clicked.connect(current_test.sendAnswer(answer))
        self.close()
        self.Open = ResultWin(current_test)
        self.Open.show()


class ResultWin(QtWidgets.QMainWindow, Ui_ResultWindow):

    def __init__(self, test, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.test = test
        self.resultLabel.setText(test.getResult())
