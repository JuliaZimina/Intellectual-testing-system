from Classes.registration import *

#login;password;status;ban;name,surname;father_name;date_of_birth;group;secret_question;secret_answer;email;tel
class TemplateUser:
    def __init__(self, login, password, name,surname,father_name, date_of_birth, group, secret_question, secret_answer, email, tel):
        self.login = login
        self.password = password
        self.name = name
        self.surname=surname
        self.father_name=father_name
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

    def checkSecretAnswer(secret_answer):
        if secret_answer == '':
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
        if not checkLogin(new_login):
            raise Exception("Such name already exists")
        if not checkNames(new_login):
            raise Exception("Login shouldn`t be empty")
        users[self.login] = new_login
        self.login=new_login


    def setPassword(self, new_password):
        if checkPassword(new_password):
            users[self.login]['password'] = new_password
        return users

    def setName(self, new_name):
        if checkNames(new_name):
            users[self.login]['name'] = new_name
        return users

    def setDateOfBirth(self, new_date_of_birth):
        if checkNames(new_date_of_birth):
            users[self.login]['date_of_birth'] = new_date_of_birth


    def setGroup(self, new_group):
        if checkNames(new_group):
            users[self.login]['group'] = new_group


    def setSecretQuestion(self, new_secret_question):
        if checkNames(new_secret_question):
            users[self.login]['secret_question'] = new_secret_question


    def setSecretAnswer(self, new_secret_answer):
        if checkNames(new_secret_answer):
            users[self.login]['secret_answer'] = new_secret_answer

    def setEmail(self, new_email):
        if checkNames(new_email):
            users[self.login]['email'] = new_email


    def setPhoneNumber(self, new_tel):
        if checkNames(new_tel):
            users[self.login]['tel'] = new_tel

    def setSurname(self, new_surname):
        if checkNames(new_surname):
            users[self.login]['surname'] = new_surname
            
    def setFatherName(self, new_fname):
        if checkNames(new_fname):
            users[self.login]['father_name'] = new_fname

    def getPassword(self):
        pass

    def getName(self):
        pass

    def getSurname(self):
        pass

    def getFatherName(self):
        pass

    def getDateOfBirth(self):
        pass

    def getSecretQuestion(self):
        pass

    def getSecretAnswer(self):
        pass

    def getEmail(self):
        pass

    def getPhoneNumber(self):
        pass
    
