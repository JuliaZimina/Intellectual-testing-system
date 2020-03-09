from dataProcessing import *

class Test:
    """Test model"""

    def __init__(self, field, number_of_quest, type, sum_right):
        self.field = field
        self.number_of_quest = number_of_quest
        self.type = type
        self.sum_right = sum_right
        self.end_of_test = False
        pass

#генерирует следующий вопрос
    def getNextQuestion(self):

        pass

#пользователь отправляет свой ответ
    def sendAnswer(self, answer):
        pass

    def getResult(self):
        pass

    def launch(self):
        print("Вы выбрали тест по теме: " + self.field)

test = Test("История")
test.launch()