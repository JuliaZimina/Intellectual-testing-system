# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pycharmworkspace\Intellectual-testing-system\interface\Windows\editQuestion.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditQuestionWindow(object):
    def setupUi(self, EditQuestionWindow):
        EditQuestionWindow.setObjectName("EditQuestionWindow")
        EditQuestionWindow.resize(398, 308)
        self.centralwidget = QtWidgets.QWidget(EditQuestionWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.themeLine = QtWidgets.QLineEdit(self.centralwidget)
        self.themeLine.setObjectName("themeLine")
        self.verticalLayout.addWidget(self.themeLine)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.questionLine = QtWidgets.QLineEdit(self.centralwidget)
        self.questionLine.setObjectName("questionLine")
        self.verticalLayout.addWidget(self.questionLine)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.answerLine = QtWidgets.QLineEdit(self.centralwidget)
        self.answerLine.setObjectName("answerLine")
        self.verticalLayout.addWidget(self.answerLine)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.incorrectAnswersLine = QtWidgets.QLineEdit(self.centralwidget)
        self.incorrectAnswersLine.setObjectName("incorrectAnswersLine")
        self.verticalLayout.addWidget(self.incorrectAnswersLine)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.timespinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.timespinBox.setObjectName("timespinBox")
        self.verticalLayout.addWidget(self.timespinBox)
        self.sendQuestionEdit = QtWidgets.QPushButton(self.centralwidget)
        self.sendQuestionEdit.setObjectName("sendQuestionEdit")
        self.verticalLayout.addWidget(self.sendQuestionEdit)
        EditQuestionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditQuestionWindow)
        QtCore.QMetaObject.connectSlotsByName(EditQuestionWindow)

    def retranslateUi(self, EditQuestionWindow):
        _translate = QtCore.QCoreApplication.translate
        EditQuestionWindow.setWindowTitle(_translate("EditQuestionWindow", "Редактировать вопрос"))
        self.label.setText(_translate("EditQuestionWindow", "Тема*"))
        self.label_2.setText(_translate("EditQuestionWindow", "Вопрос*"))
        self.label_3.setText(_translate("EditQuestionWindow", "Правильный ответ*"))
        self.label_4.setText(_translate("EditQuestionWindow", "Неправильные ответы,указать через ;"))
        self.label_5.setText(_translate("EditQuestionWindow", "Время выполнения в секундах*"))
        self.sendQuestionEdit.setText(_translate("EditQuestionWindow", "Подтвердить"))
