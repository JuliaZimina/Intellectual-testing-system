# import urllib
# import json
# import time
# from email.massage import EmailMassage
import smtplib
from Classes.templateUser import *
from Classes.user import *
from Classes.analyst import *
from Classes.administrator import *

from dataProcessing import users, recovery_requests


EMAIL = "zeiwjfew@yandex.ru"
PASSWORD = "ooP123"

'''
def send_sms(phones, text, total_price=0):
    login = 'userlog'       # Логин в smsc
    password = 'myPas1'     # Пароль в smsc
    sender = 'Python'    # Имя отправителя
    # Возможные ошибки
    errors = {
        1: 'Ошибка в параметрах.',
        2: 'Неверный логин или пароль.',
        3: 'Недостаточно средств на счете Клиента.',
        4: 'IP-адрес временно заблокирован из-за частых ошибок в запросах. Подробнее',
        5: 'Неверный формат даты.',
        6: 'Сообщение запрещено (по тексту или по имени отправителя).',
        7: 'Неверный формат номера телефона.',
        8: 'Сообщение на указанный номер не может быть доставлено.',
        9: 'Отправка более одного одинакового запроса на передачу SMS-сообщения либо более пяти одинаковых запросов на получение стоимости сообщения в течение минуты. '
    }
    # Отправка запроса
    url = "http://smsc.ru/sys/send.php?login=%s&psw=%s&phones=%s&mes=%s&cost=%d&sender=%s&fmt=3" % (login, password, phones, text, total_price, sender)
    answer = json.loads(urllib.urlopen(url).read())
    if 'error_code' in answer:
        # Возникла ошибка
        return errors[answer['error_code']]
    else:
        if total_price == 1:
            # Не отправлять, узнать только цену
            print 'Будут отправлены: %d SMS, цена рассылки: %s' % (answer['cnt'], answer['cost'].encode('utf-8'))
        else:
            # СМС отправлен, ответ сервера
            return answer
'''


def sendMessage(text, mail):
    msg = EmailMassage()
    msg['Subject'] = "Подтверждение регистрации"
    msg['From'] = EMAIL
    msg['To'] = mail
    msg.set_content(text)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_massage(msg)



def registration(login, password, name, surname, father_name, date_of_birth, group, secret_question, answer, email, tel,
                 photo=""):

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

    users[login] = {'password': password, 'status': 'user', 'ban': 'False', 'name': name,
                    'date_of_birth': date_of_birth,
                    'tel': tel,
                    'father_name': father_name, 'surname': surname, 'group': group, 'secret_question': secret_question,
                    'secret_answer': answer, 'email': email, 'photo': photo}

    # sendMessage('вы подтвердили регистрацию', email)

    return User(login, password, name, surname, father_name, date_of_birth, group, secret_question, answer,
                email, tel)


def recoveryRequest(login, password, name, surname, father_name, date_of_birth, group, secret_question, answer, email,
                    tel,
                    photo=""):

    recovery_requests[login] = {'password': password, 'status': 'user', 'ban': 'True', 'name': name,
                                'date_of_birth': date_of_birth, 'tel': tel,
                                'father_name': father_name, 'surname': surname, 'group': group,
                                'secret_question': secret_question,
                                'secret_answer': answer, 'email': email}
    users[login]["ban"]="True"

    # sendMessage('ваш запрос на восстановление оптравлен', email)


def checkSecretAnswer(login, answer):
    if answer != users[login]['secret_answer']:
        raise Exception("secret answer is wrong")
    return True


def changePassword(login, new_password):
    if new_password == users[login]["password"]:
        raise Exception("New password shouldn't be equal to old one")
    if not checkPassword(new_password):
        raise Exception("Your password should be larger than 8")
    users[login]['password'] = new_password

    return True


def logIn(login, password):  # вход
    print("LG func")

    if login not in users:
        raise Exception("There are no such user")

    if users[login]['password'] != password:
        raise Exception("Wrong password")

    if users[login]['ban']=="True":
        raise Exception('The person is banned')

    if users[login]['status'] == 'user':
        print("userLG")
        return User(login, password, users[login]['name'], users[login]['surname'],
                    users[login]['father_name'], users[login]['date_of_birth'], users[login]['group'],
                    users[login]['secret_question'],
                    users[login]['secret_answer'], users[login]['email'], users[login]['tel'])

    if users[login]['status'] == 'analyst':
        return Analyst(login, password, users[login]['name'], users[login]['surname'],
                       users[login]['father_name'], users[login]['date_of_birth'], users[login]['group'],
                       users[login]['secret_question'],
                       users[login]['secret_answer'], users[login]['email'], users[login]['tel'])
    else:
        return Administrator(login, password, users[login]['name'], users[login]['surname'],
                             users[login]['father_name'], users[login]['date_of_birth'], users[login]['group'],
                             users[login]['secret_question'],
                             users[login]['secret_answer'], users[login]['email'], users[login]['tel'])


# временный вход, это не для смены пароля, это функция которая создает объект юзера по логину, т.е. принимать должна
# только логин
def tmpLogIn(login):  # временный вход
    if users[login]['status'] == 'user':
        return User(login, users[login]['password'], users[login]['name'], users[login]['surname'],
                    users[login]['father_name'], users[login]['date_of_birth'], users[login]['group'],
                    users[login]['secret_question'],
                    users[login]['secret_answer'], users[login]['email'], users[login]['tel'])
    elif users[login]['status'] == 'analyst':
        return Analyst(login, users[login]['password'], users[login]['name'], users[login]['surname'],
                       users[login]['father_name'], users[login]['date_of_birth'], users[login]['group'],
                       users[login]['secret_question'],
                       users[login]['secret_answer'], users[login]['email'], users[login]['tel'])
    else:
        return Administrator(login, users[login]['password'], users[login]['name'], users[login]['surname'],
                             users[login]['father_name'], users[login]['date_of_birth'], users[login]['group'],
                             users[login]['secret_question'],
                             users[login]['secret_answer'], users[login]['email'], users[login]['tel'])
