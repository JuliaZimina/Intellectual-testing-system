from interface.LogIn import *
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myapp = LogInWin()
    myapp.show()
    #write_standard("uses.sys",genStat)
    sys.exit(app.exec_())




