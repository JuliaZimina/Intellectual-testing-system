#from emal.massage import EmalMassage
import smtplib
from Classes.User import *

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



def sendMessage(text, mail):
    msg = EmalMassage()
    msg['Subject'] = "Подтверждение регистрации"
    msg['From'] = EMAIL
    msg['To'] = mail
    msg.set_content(text)
    
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
    
    if not checkNames(login):
        raise Exception("The login is requried")

    if not checkPassword(password):
         raise Exception("Your password should be larger than 8")
            
    if not checkNames(password):
        raise Exception("The password is requried")

    if not checkNames(name):
        raise Exception("The name is requried")

    if not checkNames(surname):
        raise Exception("The surname is requried")

    if not checkNames(answer):
        raise Exception("The answer is requried")

    if not checkNames(email):
        raise Exception("The email is requried")

    users[login] = {'password': password, 'status: 'user', 'ban': False, 'name' :  name, 'date_of_birth' : date_of_birth, 'tel':tel,
    'father_name' : father_name, 'surname' : surname, 'group' : group, 'secret_question' : secret_question, 'secret_answer' : answer, 'email' : email, 'photo' : photo}


    sendMessage('вы подтвердили регистрацию', email)


    return User(login, password, name, surname, father_name, date_of_birth, group, secret_question, secret_answer, email, tel)


def recoveryRequest(login, password, name, surname, father_name, date_of_birth, group, secret_question, answer, email, tel,
                 photo=""):

    recovery_requests[login] = {'password': password, 'status': 'regular_user', 'ban': False, 'name': name,
                    'date_of_birth': date_of_birth, 'tel': tel,
                    'father_name': father_name, 'surname': surname, 'group': group, 'secret_question': secret_question,
                    'secret_answer': answer, 'email': email, 'photo': photo}

    sendMessage('ваш запрос на восстановление оптравлен', email) 



    
       
def checkSecretAnswer(login, answer):
    
    if answer != users[login]['secret_answer']:
        raise Exception("secret answer is wrong")
    return True
  

  
def changePassword(login, new_password):
    if new_password == users[login]["password"]:
        raise Exception("New password shouldn't be equal to old one")
    if not checkPassword(new_password):
         raise Exception("Your password should be larger than 8")
    user[login]['password'] = new_password
    
    return True
 
 

def logIn(login, password): # вход

    
    if login not in users:
        raise Exception("There are no such user")
    
    if users[login]['password'] != password:
        raise Exception("Wrong password")
        
    if users[login]['ban']:
        raise Exception('The person is banned') 
  return User(login, password, users[login][name], users[login][surname], 
              users[login][father_name], users[login][date_of_birth], users[login][group], users[login][secret_question], 
              users[login][secret_answer], users[login][email], users[login][tel])


#временный вход, это не для смены пароля, это функция которая создает объект юзера по логину, т.е. принимать должна только логин
def tmpLogIn(login): #временный вход
    return User(login, password, users[login][name], users[login][surname], 
              users[login][father_name], users[login][date_of_birth], users[login][group], users[login][secret_question], 
              users[login][secret_answer], users[login][email], users[login][tel])
    





