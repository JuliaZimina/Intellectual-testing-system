from Classes.templateUser import *
from dataProcessing import userStat


class User(TemplateUser):
    def __init__(self, login, password, name,surname,father_name, date_of_birth, group, secret_question, secret_answer, email, tel):
        super().__init__(login, password, name,surname,father_name, date_of_birth, group, secret_question, secret_answer, email, tel)

    def getStatistics(self):
        return str(userStat[self.login])
    def getGeneralTestCounter(self):
        count = 0
        for test in userStat[self.login]:
            if "generall" in test:
                count += 1

