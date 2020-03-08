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
                    groups_of_questions.append(a)
                    data[a] = {c[0]: {'время': c[1], 'ответ': c[2:]}}
        # print(data)
        return data
    else:
        return data


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


# login;password;status;ban;name,surname;father_name;date_of_birth;group;secret_question;secret_answer;email;tel
users = read_users_info('Data/UsersInfo/users.sys')
print(users)
# группа;вопрос;время;правильный ответ;ответ;ответ
tests = read_tests('Data/Content/tests.sys')
print(tests)
genStat = read_general_statistics('Data/Ratings/generalStatistics.sys')
print(genStat)
groupStat = read_group_statistic('Data/Ratings/groupStatistics.sys')
print(groupStat)
userStat = read_users_statistics('Data/Ratings/usersStatistics.sys')
print(userStat)
print(groups_of_questions)
secret_questions = ["f", "g"]
