from dataProcessing import *

def printQuestion(file):
    lines = [line.strip() for line in file]
    for i in range(5):
        print(lines[i])

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
        if (self.field == "История"):
            f1 = open('tests.sys', 'r')
            printQuestion(f1)
            a = input()

test = Test("История России")
test.launch()