# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\secretQuestionui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecretQuestionWindow(object):
    def setupUi(self, SecretQuestionWindow):
        SecretQuestionWindow.setObjectName("SecretQuestionWindow")
        SecretQuestionWindow.resize(284, 265)
        self.centralwidget = QtWidgets.QWidget(SecretQuestionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.secretQuestionLabel = QtWidgets.QLabel(self.centralwidget)
        self.secretQuestionLabel.setText("")
        self.secretQuestionLabel.setObjectName("secretQuestionLabel")
        self.gridLayout.addWidget(self.secretQuestionLabel, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.answerLine = QtWidgets.QLineEdit(self.centralwidget)
        self.answerLine.setObjectName("answerLine")
        self.gridLayout.addWidget(self.answerLine, 1, 1, 1, 1)
        self.answerButton = QtWidgets.QPushButton(self.centralwidget)
        self.answerButton.setObjectName("answerButton")
        self.gridLayout.addWidget(self.answerButton, 2, 1, 1, 1)
        SecretQuestionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecretQuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(SecretQuestionWindow)

    def retranslateUi(self, SecretQuestionWindow):
        _translate = QtCore.QCoreApplication.translate
        SecretQuestionWindow.setWindowTitle(_translate("SecretQuestionWindow", "Секретный вопрос"))
        self.label.setText(_translate("SecretQuestionWindow", "Секретный вопрос:"))
        self.label_3.setText(_translate("SecretQuestionWindow", "Ответ на вопрос:"))
        self.answerButton.setText(_translate("SecretQuestionWindow", "Ответить"))
