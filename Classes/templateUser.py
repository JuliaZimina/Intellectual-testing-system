
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


    def setLogin(self, new_login):
        if not checkLogin(new_login):
            raise Exception("Such name already exists")
        if not checkNames(new_login):
            raise Exception("Login shouldn`t be empty")
        users[self.login] = new_login
        self.login=new_login


    def setPassword(self, new_password):
        if not checkPassword(new_password):
            raise Exception("Пароль должен быть длинее 8 символов")
        if not checkNames(new_password):
            raise Exception("Password shouldn`t be empty")
        users[self.login]['password'] = new_password
        self.password=new_password

    def setName(self, new_name):
        if checkNames(new_name):
            users[self.login]['name'] = new_name
            self.name=new_name
        else:
            raise Exception("Name shouldn`t be empty")

    def setDateOfBirth(self, new_date_of_birth):
        if checkNames(new_date_of_birth):
            users[self.login]['date_of_birth'] = new_date_of_birth
            self.date_of_birth=new_date_of_birth
            raise Exception("Password shouldn`t be empty")
        else:
            raise Exception("Date of birth shouldn`t be empty")



    def setGroup(self, new_group):
        users[self.login]['group'] = new_group
        self.group=new_group


    def setSecretQuestion(self, new_secret_question):
        users[self.login]['secret_question'] = new_secret_question
        self.secret_question=new_secret_question


    def setSecretAnswer(self, new_secret_answer):
        if checkNames(new_secret_answer):
            users[self.login]['secret_answer'] = new_secret_answer
            self.secret_answer=new_secret_answer
        else:
            raise Exception("Secret answer shouldn`t be empty")

    def setEmail(self, new_email):
        if checkNames(new_email):
            users[self.login]['email'] = new_email
            self.email=new_email
        else:
            raise Exception("Email shouldn`t be empty")


    def setPhoneNumber(self, new_tel):
        users[self.login]['tel'] = new_tel
        self.tel=new_tel

    def setSurname(self, new_surname):
        if checkNames(new_surname):
            users[self.login]['surname'] = new_surname
            self.surname=new_surname
            
    def setFatherName(self, new_fname):
        users[self.login]['father_name'] = new_fname
        self.father_name=new_fname

    def getPassword(self):
        return self.password

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getFatherName(self):
        return self.father_name

    def getDateOfBirth(self):
        return self.date_of_birth

    def getSecretQuestion(self):
        return self.secret_question

    def getSecretAnswer(self):
        return self.secret_answer

    def getEmail(self):
        return self.email

    def getPhoneNumber(self):
        return self.tel

    def deleteUser(self):
        del users[self.login]
def checkLogin(login):
    if login in users:
        return False
    return True

def checkPassword(password):
    if len(password) < 8:
        return False
    return True
def checkNames(name):
    if name == '':
        return False
    return True