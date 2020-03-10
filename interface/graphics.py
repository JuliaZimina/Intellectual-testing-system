import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from interface.Windows.graphicsWindow import *

class GraphicsWin(Ui_Form, QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.fig = seabornplot()
        self.plotWidget = FigureCanvas(self.fig)
        lay = QtWidgets.QVBoxLayout(self.content_plot)
        lay.addWidget(self.plotWidget)
def seabornplot():
    g = sns.catplot(x="группа вопросов", y="количество отвечавших",
                    data=pd.read_csv('../Data/Ratings/groupStatistics.sys', sep=";"), height=6, kind="bar",
                    hue='группа людей')

    return g.fig
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window=GraphicsWin()
    window.show()
    sys.exit(app.exec_())