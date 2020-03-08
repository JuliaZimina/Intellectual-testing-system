# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\question.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_questionWindow(object):
    def setupUi(self, questionWindow):
        questionWindow.setObjectName("questionWindow")
        questionWindow.resize(366, 320)
        self.verticalLayout = QtWidgets.QVBoxLayout(questionWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.questionLabel = QtWidgets.QLabel(questionWindow)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout.addWidget(self.questionLabel)
        self.answerlineEdit = QtWidgets.QLineEdit(questionWindow)
        self.answerlineEdit.setObjectName("answerlineEdit")
        self.verticalLayout.addWidget(self.answerlineEdit)
        self.answerButton = QtWidgets.QPushButton(questionWindow)
        self.answerButton.setObjectName("answerButton")
        self.verticalLayout.addWidget(self.answerButton)

        self.retranslateUi(questionWindow)
        QtCore.QMetaObject.connectSlotsByName(questionWindow)

    def retranslateUi(self, questionWindow):
        _translate = QtCore.QCoreApplication.translate
        questionWindow.setWindowTitle(_translate("questionWindow", "Dialog"))
        self.questionLabel.setText(_translate("questionWindow", "Вопрос"))
        self.answerButton.setText(_translate("questionWindow", "Ответить"))
