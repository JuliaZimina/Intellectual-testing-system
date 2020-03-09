from dataProcessing import *
class Test:
    """Test model"""

    def __init__(self, field):
        self.field = field
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

test = Test("История России")
test.launch()