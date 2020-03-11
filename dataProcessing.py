import os

groups_of_questions = []


def file_is_empty(path):
    return os.stat(path).st_size == 0


def read_tests(file):
    data = {}
    if not file_is_empty(file):
        with open(file, encoding='utf-8') as f:
            for line in f:
                if len(line.split(';')) != 1:
                    a, *b = line.split(';')
                    c = []
                    for x in b:
                        if x != '' and x != ' ':
                            c.append(x.rstrip())
                    if a not in groups_of_questions:
                        groups_of_questions.append(a)
                    if a not in data.keys():
                        data[a] = {c[0]: {'время': c[1], 'ответ': c[2:]}}
                    else:
                        tmp=data[a]
                        tmp[c[0]]={'время': c[1], 'ответ': c[2:]}
                        data[a]=tmp
        # print(data)
        return data
    else:
        return data


def printIncorrectAnswers(group,question):
    answers=[tests[group][question]["ответ"][i] for i in range(1,len(tests[group][question]["ответ"]))]
    return ";".join(answers)


def read_users_statistics(file):
    data = {}
    if not file_is_empty(file):
        with open(file,encoding='utf-8') as f:
            for line in f:
                if len(line.split(';')) != 1:
                    a, *b = line.split(';')
                    b = [x.rstrip() for x in b]
                    c = []
                    for x in b:
                        c.append(x.split(':'))
                    data[a] = c
        # print(data)
        return data
    else:
        return data

def read_users_info(file):
    data = {}
    if not file_is_empty(file):
        with open(file, encoding='utf-8') as f:
            for line in f:
                if len(line.split(';')) != 1:
                    a, *b = line.split(';')
                    b = [x.rstrip() for x in b]
                    c = {}
                    key_words = "password;status;ban;name;surname;father_name;date_of_birth;group;secret_question;secret_answer;email;tel".split(
                        ";")
                    i = 0
                    for key_word in key_words:
                        c[key_word] = b[i]
                        i += 1
                    data[a] = c
        # print(data)
        return data
    else:
        return data

def printUserInfo(users):
    string = ""
    for key in users.keys():
        string = string + "login:" + key + ", " + str(users[key]).replace("{", "").replace("}", "").replace("'","")+"\n"
    return string

def read_general_statistics(file):
    data = {}
    if not file_is_empty(file):
        with open(file, encoding='utf-8') as f:
            for line in f:
                if len(line.split(';')) != 1:
                    dc = {}
                    a, *b = line.split(';')
                    b = [x.rstrip() for x in b]
                    c = []
                    for x in b:
                        if x != '' and x != ' ':
                            c.append(x.rstrip())
                    dc = {c[0]: c[1:]}
                    # print(dc)
                    if a not in data.keys():
                        data[a] = dc
                    else:
                        data[a].update(dc)
        return data
    else:
        return data


def read_group_statistic(file):
    data = {}
    if not file_is_empty(file):
        with open(file, encoding='utf-8') as f:
            for line in f:
                if len(line.split(';')) != 1:
                    a, *b = line.split(';')
                    b = [x.rstrip() for x in b]
                    c = []
                    for x in b:
                        if x != '' and x != ' ':
                            c.append(x.rstrip())

                    c = {c[0]: c[1:]}
                    if a not in data.keys():
                        data[a] = c
                    else:
                        data[a].update(c)

        return data
    else:
        return data

def read_grade_statistic(file):
    data={}
    firstLine=True
    themes=[]
    with open(file, encoding='utf-8') as f:
        for line in f:
            if len(line.split(';'))!=1:
                a, *b = line.split(';')
                b = [x.rstrip() for x in b]
                if firstLine:
                    themes=b[1:]
                data[a]={'group':b[0]}
                i=1
                for theme in themes:
                    data[a].update({theme:b[i]})
                    i+=1
    return data

def read_secret_questions(file):
    data=[]
    with open(file, encoding='utf-8') as f:
        for line in f:
            data.append(line.rstrip())
    return data


def write_standard(file, data):
    print("rewriting")
    f = open(file, 'w')
    for x, y in zip(data.keys(), data.values()):
        f.write(str(x) + ';' + str(y) + '\n')
    f.close()
def write_users_info(file,data):
    with open(file,'w', encoding='utf-8') as f:
        for user in data.keys():
            str=[]
            str.append(user)
            key_words = "password;status;ban;name;surname;father_name;date_of_birth;group;secret_question;secret_answer;email;tel".split(
                ";")
            for key_word in key_words:
                str.append(users[user][key_word])
            string=""
            for i in range(len(str)-1):
                string=string+str[i]+";"
            string=string+str[-1]
            f.write(string+"\n")
def write_group_stat(file,data):
    with open(file, 'w', encoding='utf-8') as f:
        for group in data.keys():
            string=group+";"
            for theme in data[group].keys():
                full_string=""
                full_string+=string+theme+";"+data[group][theme][0]+";"+data[group][theme][1]+"\n"
                f.write(full_string)
def write_tests(file,data):
    with open(file, 'w', encoding='utf-8') as f:
        for group in data.keys():
            for q in data[group].keys():
                string=group+";"+q+";"+data[group][q]["время"]+";"+";".join(data[group][q]["ответ"])+"\n"
                f.write(string)
def write_grade_stat(file,data):
    with open(file, 'w', encoding='utf-8') as f:
        for user in data.keys():
            string=user+";"+data[user]["group"]+";"
            if user=="логин":
                string+=";".join(groups_of_questions)+"\n"
                f.write(string)
                continue
            for theme in groups_of_questions:
                if theme in data[user].keys():
                    string+=data[user][theme]+";"
                else:
                    string += "не проходил"+";"
            f.write(string+"\n")


users = read_users_info('Data/UsersInfo/users.sys')
print(users)
recovery_requests=read_users_info('Data/UsersInfo/passwordRequests.sys')
tests = read_tests('Data/Content/tests.sys')
print(tests)
#genStat = read_general_statistics('Data/Ratings/generalQuestionsStatistics.sys')
#print(genStat)
groupStat = read_group_statistic('Data/Ratings/groupStatistics.sys')
print(groupStat)
userStat = read_users_statistics('Data/Ratings/usersPersonalStatistics.sys')
print(userStat)
print(groups_of_questions)
secret_questions = read_secret_questions('Data/Content/secretQuestions.sys')
print(secret_questions)
gradeStat=read_grade_statistic('Data/Ratings/usersGradeStatistics.sys')
print(gradeStat)



