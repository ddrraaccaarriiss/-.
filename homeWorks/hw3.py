class Bank:
    def __init__(self, _name, _balanse):
        self._name = _name
        self._balanse = _balanse

    def __str__(self):
        return f' name is: {self._name}\n' \
               f'balanse is: {self._balanse}'

    def moneyX(self):
        balanse = int(input("Введите сумму: "))
        self._balanse += balanse

    def _kill(self):
        self._balanse *= 0

    def kill(self):
        self._kill()

    def __jackpot(self):
        self._balanse *= 10

    def jackpot(self):
        self.__jackpot()

    def _balanse_from(self, other):
        self._balanse += other._balanse


aku = Bank("Aku", 100)
sake = Bank("Sake", 100)
take = Bank("Take", 100)
alina = Bank("Alina", 100)
dina = Bank("Dina", 100)

aku.moneyX()
print(aku)

# sake._kill()
sake.kill()
print(sake)

take.jackpot()
# take._Bank__jackpot()
print(take)


alina._balanse_from(dina)
print(alina)

