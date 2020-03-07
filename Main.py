import sys

from interface.LogIn import *
from PyQt5 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = LogInWin()
    myapp.show()
    sys.exit(app.exec_())