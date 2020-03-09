# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\ban.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BanWindow(object):
    def setupUi(self, BanWindow):
        BanWindow.setObjectName("BanWindow")
        BanWindow.resize(286, 245)
        self.centralwidget = QtWidgets.QWidget(BanWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.loginBox = QtWidgets.QComboBox(self.centralwidget)
        self.loginBox.setObjectName("loginBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.loginBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.banButton = QtWidgets.QPushButton(self.centralwidget)
        self.banButton.setObjectName("banButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.banButton)
        self.reasonLine = QtWidgets.QLineEdit(self.centralwidget)
        self.reasonLine.setObjectName("reasonLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reasonLine)
        BanWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BanWindow)
        QtCore.QMetaObject.connectSlotsByName(BanWindow)

    def retranslateUi(self, BanWindow):
        _translate = QtCore.QCoreApplication.translate
        BanWindow.setWindowTitle(_translate("BanWindow", "Заблокировать"))
        self.label.setText(_translate("BanWindow", "Логин"))
        self.label_2.setText(_translate("BanWindow", "Причина"))
        self.banButton.setText(_translate("BanWindow", "Подтвердить"))
