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


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def seabornplot():
    g = sns.catplot(x="группа вопросов", y="количество отвечавших",
                    data=pd.read_csv('Data/Ratings/groupStatistics.sys', sep=";"), height=6, kind="bar",
                    hue='группа людей')

    return g.fig


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        # sc = MplCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        # self.setCentralWidget(sc)
        self.fig = seabornplot()
        plt.show()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.draw()
        #self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)


        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
