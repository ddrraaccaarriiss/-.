class Bank:
    def __init__(self, name, balanse):
        self.name = name
        self.balanse = balanse

    def __str__(self):
        return f' name is: {self.name}\n' \
               f'balanse is: {self.balanse}'

    def moneyX(self):
        balanse = int(input("Введите сумму: "))
        self.balanse += balanse

    def _kill(self):
        self.balanse *= 0

    def kill(self):
        self._kill()

    def __jackpot(self):
        self.balanse *= 10

    def jackpot(self):
        self.__jackpot()

    def _take_balanse(self, other):
        self.balanse += other.balanse


aku = Bank("Aku", 100)
sake = Bank("Sake", 100)
take = Bank("Take", 100)
alina = Bank("Alina", 100)
dina = Bank("Dina", 100)

aku.moneyX()
print(aku)

sake._kill()
sake.kill()
print(sake)

take.jackpot()
take._Bank__jackpot()
print(take)


alina._take_balanse(dina)
print(alina)
#проверка комита
