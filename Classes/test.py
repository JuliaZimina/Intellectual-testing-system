from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field, sum_right=0):
        self.field = field
        self.sum_right = sum_right
        self.ex_quest = []
        self.number_of_quest = 5
        self.end_of_test = False
        self.array_themes = []

#генерирует следующий вопрос
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

#пользователь отправляет свой ответ
    def sendAnswer(self, answer, time):

        pass

    def getResult(self):
        pass
test1=Test("История")
print(test1.getNextQuestion())
print(test1.getNextQuestion())
print(test1.getNextQuestion())
test2=Test("general")
print("start")
print(test2.getNextQuestion())
print(test2.getNextQuestion())
print(test2.getNextQuestion())
print(test2.getNextQuestion())
print(test2.getNextQuestion())
