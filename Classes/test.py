from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field):
        self.field = field
        self.ex_quest = []
        self.number_of_quest = 5
        self.end_of_test = False
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
        d = self.ex_quest[-1]
        if answer != d['ответ'][0]:
            self.answers.append(0)
        if (time > int(d['время']) or time <= 5 or answer != d['ответ'][0]) and self.number_of_quest < 10:
            self.number_of_quest += 1
        else:
            self.answers.append(1)


    def getResult(self):
        st = ''
        for i in range(len(self.ex_quest)-1):
             if self.answers[i] == 0:
                 st = st + "Вопрос " + str(i) + " отвечен неправильно\n"
             else:
                 st = st + "Вопрос " + str(i) + " отвечен правильно\n"
        st = st + "Количество правильных ответов: " + str(self.answers.count(1)) + " из " + str(len(self.answers)) + "\n" \
             + str(int(self.answers.count(1) / len(self.answers * 100))) + " процентов отвечено верно"
        return st


    def endTest(self):
        if self.number_of_quest == len(self.ex_quest):
            return True


test1=Test("История")
print(test1.getNextQuestion())
test2=Test("general")
print("start")
print(test2.getNextQuestion())
print(test2.getNextQuestion())

