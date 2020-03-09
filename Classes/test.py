from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field, sum_right):
        self.field = field
        self.sum_right = sum_right
        self.ex_quest = []
        self.number_of_quest = 5
        self.end_of_test = False

#генерирует следующий вопрос
    def getNextQuestion(self):
        data = read_tests("tests.sys")
        for key in data:
            if self.field != "general":
                if key == self.field:
                    for j in data[key]:
                        for i in self.ex_quest:
                            if i == j:
                                continue
                    self.ex_quest.append(data[key][j])
                    return data[key][j]
            else:
                for j in data[key]:
                    for i in self.ex_quest:
                        if i == j:
                            continue
                        else:
                            if len(self.ex_quest)%2 == 0:
                                continue
                self.ex_quest.append(data[key][j])
                return data[key][j]

#пользователь отправляет свой ответ
    def sendAnswer(self, answer, time):
        pass

    def getResult(self):
        pass
