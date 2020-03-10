#from emal.massage import EmalMassage
import smtplib

from dataProcessing import users,recovery_requests
#from secretQuestions import secret_questions
EMAIL = "zeiwjfew@yandex.ru"
PASSWORD = "ooP123"

def checkLogin(login):
    
    if login in users:
        return False
    return True
 

 
def checkPassword(password):

    if password < 8:
        return False
    return True



def sendMessage(mail):
    msg = EmalMassage()
    msg['Subject'] = "Подтверждение регистрации"
    msg['From'] = EMAIL
    msg['To'] = mail
    msg.set_content("Вы подтвердили регистрацию")
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_massage(msg)



def checkNames(name):
    if name == '':
        return False
    return True



def registration(login,password,name,surname,father_name,date_of_birth,group,secret_question,answer,email,tel,photo=""):

    if not checkLogin(login):
        raise Exception("Such name already exists")


    if not checkPassword(password):
         raise Exception("Your password should be larger than 8")


    if not checkNames(name):
        raise Exception("This field is requried")

    if not checkNames(surname):
        raise Exception("This field is requried")

    if not checkNames(answer):
        raise Exception("This field is requried")


    if not checkNames(email):
        raise Exception("This field is requried")

    users[login] = {'password': password, 'status': 'regular_user', 'ban' : False, 'name' :  name, 'date_of_birth' : date_of_birth, 'tel':tel,
    'father_name' : father_name, 'surname' : surname, 'group' : group, 'secret_question' : secret_question, 'secret_answer' : answer, 'email' : email, 'photo' : photo}


    sendMessage(email)


    return templateUser('...')


def recoveryRequest(login, password, name, surname, father_name, date_of_birth, group, secret_question, answer, email, tel,
                 photo=""):

    recovery_requests[login] = {'password': password, 'status': 'regular_user', 'ban': False, 'name': name,
                    'date_of_birth': date_of_birth, 'tel': tel,
                    'father_name': father_name, 'surname': surname, 'group': group, 'secret_question': secret_question,
                    'secret_answer': answer, 'email': email, 'photo': photo}

    sendMessage(email) #сообщение должно быть ваш запрос на восстановление оптравлен



    
       
def checkSecretAnswer(login, answer):
    
    if answer != users[login]['secret_answer']:
        raise Exception("secret answer is wrong")
    return True
  

  
def changePassword(login, new_password):
    if new_password == users[login]["password"]:
        raise Exception("New password shouldn't be equal to old one")
    if not checkPassword(new_password):
         raise Exception("Your password should be larger than 8")
    #в словаре изменить пароль еще нужно
    
    return True
 
 

def logIn(login, password): # вход

    
    if login not in user:
        raise Exception("There are no such user")
    
    if users[login]['password'] != password:
        raise Exception("Wrong password")
        
    if users[login]['status']:
        raise Exception('The person is banned') 
  #возвращать должен объект user, данные смотрятся по в словаре по лоину и с помощью них создается
    return True


#временный вход, это не для смены пароля, это функция которая создает объект юзера по логину, т.е. принимать должна только логин
def tmpLogIn(login, old_password, new_password): #временный вход
    if login not in users:
       raise Exception("There are no such user")
    
    if users[login]['password'] != old_password:
        raise Exception("Wrong password")
        
    users[login]['password'] = password
       
       
    return True
    




