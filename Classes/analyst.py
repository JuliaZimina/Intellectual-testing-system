from Classes.templateUser import *
from dataProcessing import *


class Analyst(TemplateUser):
    def __init__(self, login, password, name, surname, father_name, date_of_birth, group, secret_question,
                 secret_answer, email, tel):
        super().__init__(login, password, name, surname, father_name, date_of_birth, group, secret_question,
                         secret_answer, email, tel)
    def getStatistics(self):
        return printUserInfo(userStat)


    def deleteQuestion(self, group, question):
        self.hideQuestion(group,question)
        #del genStat[group][question]


    def hideQuestion(self, group, question):
        del tests[group][question]

    def hideGroup(self, group):
        del tests[group]


    def deleteGroup(self, group):
        self.hideGroup(group)
        #del genStat[group]




    def editQuestion(self, old_group, old_question, new_group, new_question, answer, incorrectAnswers, time):
        #stats = genStat[old_group][old_question]
        self.deleteQuestion(old_group,old_question)
        #genStat[new_group][new_question]=stats
        self.addQuestion(new_group,new_question,answer,incorrectAnswers,time)
        print(tests[new_group])



    def addQuestion(self, new_group, new_question, answer, incorrectAnswers, time):
        if incorrectAnswers[0]=="":
            tests[new_group][new_question] = {'время': time, 'ответ': [answer]}
        else:
            tests[new_group][new_question] = {'время': time, 'ответ': [answer] + incorrectAnswers}

