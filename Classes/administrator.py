import ssms_su
from Classes.analyst import *


class Administrator(Analyst):
    def __init__(self):
        pass
    def block_user(user):
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
    def edit_question(question):
	dictionary['question'] = question
	return dictionary
    def roles():
	user = analyst
	user = user
