from Classes.registration import *


class TemplateUser:
    def __init__(self, login, password, name, date_of_birth, group, secret_question, secret_answer, email, tel):
        self.login = login
        self.password = password
        self.name = name
        self.date_of_birth = date_of_birth
        self.group = group
        self.secret_question = secret_question
        self.secret_answer = secret_answer
        self.email = email
        self.tel = tel

    def checkDateOfBirth(date_of_birth):
        if date_of_birth == '':
            return False
        return True

    def checkGroup(group):
        if group == '':
            return False
        return True

    def checkSecretQuestion(secret_question):
        if secret_question == '':
            return False
        return True

    def checkEmail(email):
        if email == '':
            return False
        return True

    def checkTel(tel):
        if tel == '':
            return False
        return True

    def setLogin(self, new_login):
        if checkLogin(new_login):
            users[login] = new_login
        return users

    def setPassword(self, new_password):
        if checkPassword(new_password):
            users[login]['password'] = new_password
        return users

    def setName(self, new_name):
        if checkNames(new_name):
            users[login]['name'] = new_name
        return users

    def setDateOfBirth(self, new_date_of_birth):
        if checkDateOfBirth(new_date_of_birth):
            users[login]['date_of_birth'] = new_date_of_birth
        return users

    def setGroup(self, new_group):
        if checkGroup(new_group):
            users[login]['group'] = new_group
        return users

    def setSecretQuestion(self, new_secret_question):
        if checkSecretQuestion(new_secret_question):
            users[login]['secret_question'] = new_secret_question
        return users

    def setSecretAnswer(self, new_secret_answer):
        if checkSecretAnswer(login, answer):
            users[login]['secret_answer'] = new_secret_answer
        return users

    def setEmail(self, new_email):
        if checkEmail(new_email):
            users[login]['email'] = new_email
        return users

    def setTel(self, new_tel):
        if checkTel(new_tel):
            users[login]['tel'] = new_tel
        return users