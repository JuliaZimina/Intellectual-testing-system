
from interface.Windows.questionWindow import  *

from PyQt5 import QtWidgets


class QuestionWin(QtWidgets.QMainWindow, Ui_questionWindow):

    def __init__(self,theme,parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.theme=theme
        self.answerButton.clicked.connect(self.test)
    def test(self):
        pass

