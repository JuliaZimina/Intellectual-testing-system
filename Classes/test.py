from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field, sum_right=0):
        self.field = field
        self.sum_right = sum_right
        self.ex_quest = []
        self.number_of_quest = 5
        self.end_of_test = False

#генерирует следующий вопрос
    def getNextQuestion(self):

        for key in tests:
            if self.field != "general":
                if key == self.field:
                    for j in tests[key]:
                        for i in self.ex_quest:
                            if i == j:
                                continue
                    self.ex_quest.append(tests[key][j])
                    return tests[key][j]
            else:
                for j in tests[key]:
                    for i in self.ex_quest:
                        if i == j:
                            continue
                        else:
                            if len(self.ex_quest)%2 == 0:
                                break
                self.ex_quest.append(tests[key][j])
                return tests[key][j]

#пользователь отправляет свой ответ
    def sendAnswer(self, answer, time):
        pass

    def getResult(self):
        pass
test1=Test("История")
print(test1.getNextQuestion())
print(test1.getNextQuestion())
test2=Test("general")
print(test2.getNextQuestion())
print(test2.getNextQuestion())