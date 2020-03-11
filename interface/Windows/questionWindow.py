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
        questionWindow.resize(360, 330)
        questionWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget = QtWidgets.QWidget(questionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout_2.addWidget(self.questionLabel)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.answerlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.answerlineEdit.setObjectName("answerlineEdit")
        self.verticalLayout.addWidget(self.answerlineEdit)
        self.answerButton = QtWidgets.QPushButton(self.centralwidget)
        self.answerButton.setObjectName("answerButton")
        self.verticalLayout.addWidget(self.answerButton)
        questionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(questionWindow)
        QtCore.QMetaObject.connectSlotsByName(questionWindow)

    def retranslateUi(self, questionWindow):
        _translate = QtCore.QCoreApplication.translate
        questionWindow.setWindowTitle(_translate("questionWindow", "Вопрос"))
        self.questionLabel.setText(_translate("questionWindow", "Вопрос"))
        self.answerButton.setText(_translate("questionWindow", "Ответить"))
