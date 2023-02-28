class Player:
    def __init__(self, balance):
        self.balance = balance
        self.wage = []

    def placebet(self):
        pass

    
    def deposit(self):
        run = True
        while run:
            a = input("Por favor digite o quanto você vai depositar! R$> ")
            self.balance += int(a)
            print(f"Depósito completado com sucesso!\nSeu saldo é de {self.balance} reais")
            return self.balance
            run = False
    
    
    def withdraw(self):
        run = True
        while run:
            a = input("Por favor digite o quanto você vai sacar! R$> ")
            if self.balance > a:
                self.balance - a
                print(f"Saque completado com sucesso!\nSeu saldo é de {self.balance} reais"
                return self.balance
            else:
                print("Sem fundos suficientes para o saque!")
            run = False


