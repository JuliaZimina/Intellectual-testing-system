from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field, type, sum_right):
        self.field = field
        self.type = type
        self.sum_right = sum_right
        self.ex_quest = []
        self.number_of_quest = 5
        self.end_of_test = False

#генерирует следующий вопрос
    def getNextQuestion(self):
        data = read_tests("tests.sys")
        for key in data:
            if key == self.field:
                for i in self.ex_quest:
                    if i == data[key]:
                        continue
                self.ex_quest.append(data[key])
                return data[key]

#пользователь отправляет свой ответ
    def sendAnswer(self, answer, time):
        pass

    def getResult(self):
        pass
