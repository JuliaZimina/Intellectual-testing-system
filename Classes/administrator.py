# import ssms_su
from Classes.analyst import *
from dataProcessing import *


class Administrator(Analyst):
    def __init__(self, login, password, name, surname, father_name, date_of_birth, group, secret_question,
                 secret_answer, email, tel):
        super().__init__(login, password, name, surname, father_name, date_of_birth, group, secret_question,
                         secret_answer, email, tel)




    def block_user(self, login, reason):
        users[login]["ban"] = "True"
        # отправить сообщение

    def roles(self,login, new_role):
        users[login]["status"]=new_role

    def return_access(self,login):
        users[login]['ban'] = "False"
        del recovery_requests[login]
        #отправить сообщение
