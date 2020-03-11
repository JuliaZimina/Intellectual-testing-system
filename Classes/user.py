from Classes.templateUser import *
from dataProcessing import userStat


class User(TemplateUser):
    def __init__(self, login, password, name,surname,father_name, date_of_birth, group, secret_question, secret_answer, email, tel):
        super().__init__(login, password, name,surname,father_name, date_of_birth, group, secret_question, secret_answer, email, tel)

    def getStatistics(self):
        if self.login in userStat.keys():
            return str(userStat[self.login])
        return "None"

    def getGeneralTestCounter(self):
        count = 0
        if self.login in userStat.keys():
            for test in userStat[self.login]:
                if "general" in test:
                    count += 1
        return count

