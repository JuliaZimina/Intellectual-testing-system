from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field):
        self.field = field
        self.ex_quest = []
        self.number_of_quest = 5
        self.array_themes = []
        self.answers = []

# генерирует следующий вопрос
    def getNextQuestion(self):
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
                    self.array_themes.append([j,tests[key][j]])
                    self.ex_quest.append([j,tests[key][j]])

                    return [j,tests[key][j]]


# пользователь отправляет свой ответ
    def sendAnswer(self, answer, time):
        print("h")
        d = self.ex_quest[-1][1]
        print("hi")
        print(d)
        if answer != d['ответ'][0]:
            self.answers.append(0)
        if (time > int(d['время']) or time <= 5 or answer != d['ответ'][0]) and self.number_of_quest < 10:
            self.number_of_quest += 1
        else:
            self.answers.append(1)


    def getResult(self):
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
        elif 45 <= a <70:
            return 3
        else: return 2

test1=Test("История")
print(test1.getNextQuestion())
test1.sendAnswer("ggg",30)
print(test1.getResult())
test2=Test("general")
print("start")
#print(test2.getNextQuestion())
#print(test2.getNextQuestion())

