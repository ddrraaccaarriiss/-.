""""  @property   """"

class Bank:
    def __init__(self, _name, koko):
        self._name = _name
        self.koko = koko

    def __str__(self):
        return f' name is: {self._name}\n' \


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name




aku = Bank("Aku",12)

aku.name
aku.name="beku"
aku.name
print(aku)











