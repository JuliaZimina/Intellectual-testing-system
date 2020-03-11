# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\message.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageWindow(object):
    def setupUi(self, MessageWindow):
        MessageWindow.setObjectName("MessageWindow")
        MessageWindow.resize(311, 223)
        self.centralwidget = QtWidgets.QWidget(MessageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setObjectName("messageLabel")
        self.verticalLayout_2.addWidget(self.messageLabel)
        MessageWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MessageWindow)
        QtCore.QMetaObject.connectSlotsByName(MessageWindow)

    def retranslateUi(self, MessageWindow):
        _translate = QtCore.QCoreApplication.translate
        MessageWindow.setWindowTitle(_translate("MessageWindow", "MainWindow"))
        self.messageLabel.setText(_translate("MessageWindow", "Hi"))
