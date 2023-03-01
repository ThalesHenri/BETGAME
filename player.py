class Player:
    def __init__(self, balance, name, age):
        self.balance = balance
        self.name = name
        self.age = age


    # aqui vai colocar as apostas retornara uma tupla com a casa e a aposta em si
    def placebet(self):
        run = True
        while run:
            a = int(input("Por favor digite aonde voce vai apostar:\n1 para aposta em um unico número\n2 para aposta múltipla "))
            if a == 1:
                c = input("escolha o numero da casa que você irá apostar, podendo ser entre 1, 2 e 3")
                d = input("digite o quanto você quer apostar. R$ ")
                e = int(input(f"Você apostou R${d} na casa {c}, confirma?\n1 = sim\n2 = não"))
                if e == 1:
                    print("aposta confirmada!")
                    return c, d
                else:
                    pass 
                break


    def deposit(self):
        run = True
        while run:
            a = input("Por favor digite o quanto você vai depositar! R$> ")
            self.balance += int(a)
            print (f"Depósito completado com sucesso!\nSeu saldo é de {self.balance} reais")
            return self.balance
            run = False
    
    
    def withdraw(self):
        run = True
        while run:
            a = int(input("Por favor digite o quanto você vai sacar! R$> "))
            if self.balance > a:
                self.balance - a
                print(f"Saque completado com sucesso!\nSeu saldo é de {self.balance} reais")
                return self.balance
            else:
                print("Sem fundos suficientes para o saque!")
            run = False


    def show_balance(self):
        print(f"O seu saldo é de R$ {self.balance}")

"""player = Player(200, "Thales", 17)
player.show_balance()
player.deposit()
player.show_balance()
player.withdraw()
player.show_balance()"""