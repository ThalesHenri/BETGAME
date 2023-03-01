"""betfile"""
import random
from player import Player

class Bet:
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
    

    def create_player(self):
        print('=' * 20)
        a = input("Digite seu nome ")
        b = input("Digite a sua idade ")
        c = input("Digite o seu saldo ")
        player = Player(c, a, b)
        print(f"Olá, {player.name} seja bem vindo ao jogo de apostas puramente aleatório")
        player.show_balance()    



a = Bet(1000)
b = a.get_numbers()
print(b)
a.create_player()