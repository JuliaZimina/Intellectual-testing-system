# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\userRecovery.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UnblockUserWindow(object):
    def setupUi(self, UnblockUserWindow):
        UnblockUserWindow.setObjectName("UnblockUserWindow")
        UnblockUserWindow.resize(321, 292)
        self.centralwidget = QtWidgets.QWidget(UnblockUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.changeStatusButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeStatusButton.setObjectName("changeStatusButton")
        self.gridLayout.addWidget(self.changeStatusButton, 2, 1, 1, 2)
        self.loginBox = QtWidgets.QComboBox(self.centralwidget)
        self.loginBox.setObjectName("loginBox")
        self.gridLayout.addWidget(self.loginBox, 1, 1, 1, 2)
        self.userListLabel = QtWidgets.QLabel(self.centralwidget)
        self.userListLabel.setText("")
        self.userListLabel.setObjectName("userListLabel")
        self.gridLayout.addWidget(self.userListLabel, 0, 0, 1, 3)
        UnblockUserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UnblockUserWindow)
        QtCore.QMetaObject.connectSlotsByName(UnblockUserWindow)

    def retranslateUi(self, UnblockUserWindow):
        _translate = QtCore.QCoreApplication.translate
        UnblockUserWindow.setWindowTitle(_translate("UnblockUserWindow", "Запросы на смену пароля"))
        self.label.setText(_translate("UnblockUserWindow", "Логин"))
        self.changeStatusButton.setText(_translate("UnblockUserWindow", "Подтвердить"))
