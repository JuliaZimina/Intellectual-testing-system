from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field,user):
        self.user=user
        self.field = field
        self.ex_quest = []
        self.number_of_quest = 5
        if self.field=="general":
            self.number_of_quest=len(tests.keys())*2
        self.array_themes = []
        self.answers = []
        self.general_penalty=False

    def updateStatistics(self):

        groupStat[self.user.getGroup()][self.field] = groupStat[self.user.getGroup()].get(self.field, ["0", "0"])
        groupStat[self.user.getGroup()][self.field][0] = str(int(groupStat[self.user.getGroup()][self.field][0])+len(self.ex_quest))
        groupStat[self.user.getGroup()][self.field][1] = str(int(groupStat[self.user.getGroup()][self.field][1])+self.answers.count(1))
        if self.user.getLogin() not in userStat.keys():
            userStat[self.user.getLogin()] = []
        userStat[self.user.getLogin()].append([self.field, str(self.getMark())])
        if self.user.getLogin() not in gradeStat.keys():
            gradeStat[self.user.getLogin()] = {}
        gradeStat[self.user.getLogin()].update({"group": self.user.getGroup(), self.field: str(self.getMark())})

        print(groupStat)
        print(userStat)
        print(gradeStat)

# генерирует следующий вопрос
    def getNextQuestion(self):
        if self.general_penalty and self.array_themes.count(self.array_themes[-1]) < 3:
            key=self.array_themes[-1]
            for j in tests[key]:
                if [j, tests[key][j]] in self.ex_quest:
                    continue
                self.ex_quest.append([j, tests[key][j]])
                self.general_penalty=False
                return [j, tests[key][j]]
        for key in tests:
            if self.field != "general":
                if key == self.field:
                    for j in tests[key]:
                        if [j,tests[key][j]] in self.ex_quest:
                            continue
                        self.ex_quest.append([j,tests[key][j]])
                        print("ex_q", self.ex_quest)
                        return [j,tests[key][j]]
            else:
                for j in tests[key]:
                    if [j, tests[key][j]] in self.ex_quest:
                        continue
                    elif self.array_themes.count(key) == 2:
                        break
                    self.array_themes.append(key)
                    #self.array_themes.append([j,tests[key][j]])
                    self.ex_quest.append([j,tests[key][j]])

                    return [j,tests[key][j]]


# пользователь отправляет свой ответ
    def sendAnswer(self, answer, time):
        print(time)
        d = self.ex_quest[-1][1]
        if answer != d['ответ'][0]:
            self.answers.append(0)
        else:
            self.answers.append(1)
        if (time > int(d['время']) or time <= 1 or answer != d['ответ'][0]) and self.number_of_quest < 5:
            self.number_of_quest += 1
            if self.field=="general":
                self.general_penalty=True



    def getResult(self):
        if users[self.user.getLogin()]['status']=="user":
            self.updateStatistics()

        st = ''
        for i in range(len(self.ex_quest)):
             if self.answers[i] == 0:
                 st = st + "Вопрос: " + str(i+1)+"."+self.ex_quest[i][0] + " отвечен неправильно\n"
             else:
                 st = st + "Вопрос " + str(i+1)+"."+self.ex_quest[i][0] + " отвечен правильно\n"
        st = st + "Количество правильных ответов: " + str(self.answers.count(1)) + " из " + str(len(self.answers)) + "\n" \
             + str(int(self.answers.count(1) / len(self.answers) * 100)) + " процентов отвечено верно"
        return st


    def endTest(self):
        if self.number_of_quest == len(self.ex_quest):
            return True

    def getMark(self):
        a = int(self.answers.count(1) / len(self.answers) * 100)
        if a >= 85:
            return 5
        elif 70 <= a < 85:
            return 4
        elif 45 <= a < 70:
            return 3
        else: return 2

#test1=Test("История")

#print(test1.getResult())
#test2=Test("general")
print("start")
#print(test2.getNextQuestion())
#print(test2.getNextQuestion())

