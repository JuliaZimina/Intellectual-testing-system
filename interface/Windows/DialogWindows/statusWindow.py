# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\status.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_updateRoleWindow(object):
    def setupUi(self, updateRoleWindow):
        updateRoleWindow.setObjectName("updateRoleWindow")
        updateRoleWindow.resize(340, 266)
        self.centralwidget = QtWidgets.QWidget(updateRoleWindow)
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
        self.statusBox = QtWidgets.QComboBox(self.centralwidget)
        self.statusBox.setObjectName("statusBox")
        self.statusBox.addItem("")
        self.statusBox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.statusBox)
        self.changeStatusButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeStatusButton.setObjectName("changeStatusButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.changeStatusButton)
        updateRoleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(updateRoleWindow)
        QtCore.QMetaObject.connectSlotsByName(updateRoleWindow)

    def retranslateUi(self, updateRoleWindow):
        _translate = QtCore.QCoreApplication.translate
        updateRoleWindow.setWindowTitle(_translate("updateRoleWindow", "Изменить статус"))
        self.label.setText(_translate("updateRoleWindow", "Логин"))
        self.label_2.setText(_translate("updateRoleWindow", "Статус"))
        self.statusBox.setItemText(0, _translate("updateRoleWindow", "user"))
        self.statusBox.setItemText(1, _translate("updateRoleWindow", "analyst"))
        self.changeStatusButton.setText(_translate("updateRoleWindow", "Подтвердить"))
