from emal.massage import EmalMassage
import smtplib

from dataProcessing import users
from secretQuestions import secret_questions
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



def registration(login,password,name,surname,father_name,date_of_birth,group,secret_question,secret_answer,email,tel,photo=""):

    if not checkLogin(login):
        raise login_exception("Such name already exists")
        

    if not checkPassword(password):
         raise password_exception("Your password should be larger than 8")


    if not checkNames(name):
        raise name_exception("This field is requried")
    
    if not checkNames(surname):
        raise name_exception("This field is requried")
    
    
    if (group != '18би1') & (group != '18би2'):
         raise group_exception("There are only 2 types of group")
    
    
    if secret_question not in secret_questions:
        raise question_exception("There are no such question")
        

    if not checkNames(answer):
        raise name_exception("This field is requried")
    

    if not checkNames(mail):
        raise name_exception("This field is requried")
    
    users[login] = {'password': password, 'status': 'regular_user', 'ban' : False, 'name' :  name, 'date_of_birth' : date_of_birth, 'tel':tel, 
    'father_name' : father_name, 'surname' : surname, 'group' : group, 'secret_question' : secret_question, 'secret_answer' : answer, 'email' : email, 'photo' : photo}

    
    sendMessage(email)
    
    
    return templateUser()

    
       
def reestablishPassword_step1(login, answer):
    
    if answer != users[login]['secret_answer']:
        raise answer_exception("secret answer is wrong")
    return True
  

  
def reestablishPassword_step2(login, new_password):
    if new_password == users[login][password]:
        raise password_exception("New password shouldn't be equal to old one")
    
    return True
 
 

def logIn(login, password): # вход

    
    if login not in user:
        raise login_exception("There are no such user")
    
    if users[login]['password'] != password:
        raise password_exception("Wrong password")

    return True



def tmpLogIn(login, old_password, new_password): #временный вход
    if login not in users:
       raise login_exception("There are no such user")
    
    if users[login]['password'] != old_password:
        raise password_exception("Wrong password")
        
    users[login]['password'] = password
       
       
    return True
    




