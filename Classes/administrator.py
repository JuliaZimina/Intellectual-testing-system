#import ssms_su
from Classes.analyst import *
from dataProcessing import *


class Administrator(Analyst):
    def __init__(self):
    	pass
	#первый аргумент во всех методах класса всегда self
	# удаляет вопрос из test+удаляет его из всей статистики
	def deleteQuestion(self,group, question):
		pass

	# удаляет только из списка вопросов
	def hideQuestion(self,group, question):
		del tests[group][question]

	def hideGroup(self,group):
		del tests[group]

	# аналогично  с удалением вопроса
	def deleteGroup(self,group):
		pass
	#возьмем из genetalStatistics
	def getStatistics():
		pass
	#добавила поле с причиной, user-это будет не объект, а логин этого юзера
    def block_user(self,user,reason):
	ban = true
	'''smsapi = ssms_su.smsapi(user)
	smsapi.push_msg("Hello, you are in block!", user)'''
	msg = EmalMassage()
   	msg['Subject'] = "Hello! You are in block."
   	msg['From'] = EMAIL
    	msg['To'] = mail
   	msg.set_content("Hello! You are in block.")
	
	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        	smtp.login(EMAIL, PASSWORD)
        	smtp.send_massage(msg)
    def delete_question(question):
	del dictionary['question']
    def close_group(group):
	del dictionary['group'] 
	'''dictionary.popitem()'''
    def watch_questions(dictionary):
	for group in dictionary:
    		print "%s : %s" % (group, dictionary[group])
    def add_question(question):
	dictinary[group] = question
	dictionary[time] = time
	dictionary[varianti otveta] = varianti
	return dictinary
	#этот метод еще и в статистике должен менять вопрос
    def editQuestion(self,old_group,old_question,new_group,new_question,answer,incorrectAnswers,time):
		dictionary['question'] = question
		return dictionary
	#добавить вопрос в tests
	def addQuestion(self,new_group,new_question,answer,incorrectAnswers,time):
		pass
	#user-login,new_role="user"/"analyst"
    def roles(user,new_role):
	'''user = analyst
	user = user'''
	user-login,new_role="analyst"
    def return_access(user):
	users[user] = user
