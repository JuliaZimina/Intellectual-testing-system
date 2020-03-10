# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\changePassword.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordWindow(object):
    def setupUi(self, ChangePasswordWindow):
        ChangePasswordWindow.setObjectName("ChangePasswordWindow")
        ChangePasswordWindow.resize(330, 305)
        self.centralwidget = QtWidgets.QWidget(ChangePasswordWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.passwordLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLine.setObjectName("passwordLine")
        self.verticalLayout.addWidget(self.passwordLine)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout.addWidget(self.errorLabel)
        self.resetPasswordButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetPasswordButton.setObjectName("resetPasswordButton")
        self.verticalLayout.addWidget(self.resetPasswordButton)
        ChangePasswordWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChangePasswordWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordWindow)

    def retranslateUi(self, ChangePasswordWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordWindow.setWindowTitle(_translate("ChangePasswordWindow", "Смена пароля"))
        self.label.setText(_translate("ChangePasswordWindow", "Введите новый пароль:"))
        self.resetPasswordButton.setText(_translate("ChangePasswordWindow", "Подтвердить"))
