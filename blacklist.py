# import ssms_su
from Classes.analyst import *
from dataProcessing import *


class Administrator(Analyst):
    def __init__(self, login, password, name, surname, father_name, date_of_birth, group, secret_question,
                 secret_answer, email, tel):
        super().__init__(login, password, name, surname, father_name, date_of_birth, group, secret_question,
                         secret_answer, email, tel)

    def getStatistics(self):
        return str(userStat)

        # первый аргумент во всех методах класса всегда self
        # удаляет вопрос из test+удаляет его из всей статистики
    def deleteQuestion(self, group, question):
        self.hideQuestion(group,question)
        del genStat[group][question]

    # удаляет только из списка вопросов
    def hideQuestion(self, group, question):
        del tests[group][question]

    def hideGroup(self, group):
        del tests[group]

    # аналогично  с удалением вопроса
    def deleteGroup(self, group):
        self.hideGroup(group)
        del genStat[group]



    # этот метод еще и в статистике должен менять вопрос
    def editQuestion(self, old_group, old_question, new_group, new_question, answer, incorrectAnswers, time):
        stats = genStat[old_group][old_question]
        self.deleteQuestion(old_group,old_question)
        genStat[new_group][new_question]=stats
        self.addQuestion(new_group,new_question,answer,incorrectAnswers,time)


        # добавить вопрос в tests
    def addQuestion(self, new_group, new_question, answer, incorrectAnswers, time):
        tests[new_group][new_question] = {'время': time, 'ответ': [answer] + incorrectAnswers}

    # добавила поле с причиной, user-это будет не объект, а логин этого юзера
    def block_user(self, login, reason):
        users[login]["ban"] = "True"
        # отправить сообщение

    # user-login,new_role="user"/"analyst"
    def roles(self,login, new_role):
        users[login]["status"]=new_role

    def return_access(self,login):
        users[login]['ban'] = "False"
        #отправить сообщение
