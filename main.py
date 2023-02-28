"""betfile"""
import random


class bet:
    def __init__(self, balance):
        self.balance = balance
        #self.history = history
        self.a = int
        self.b = int
        self.c = int

	#função para pegar o numero do aleatorio pra apostar
    def get_numbers(self):
        self.a = random.randrange(1, 9)
        self.b = random.randrange(1, 9)
        self.c = random.randrange(1, 9)
        return self.a, self.b, self.c


a = bet(1000)
b = a.get_numbers()
print(b)