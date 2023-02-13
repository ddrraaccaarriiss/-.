
class Cat:

    def __init__(self):
        self.__name = "Tom"
        self.__age = 3

    def get_all(self):
        return f'name: {self.__name}, age: {self.__age}'

    def set_all(self, val, val2=None):
        if val2 is not None:
            self.__age = val2
        self.__name = val

    all = property(get_all, set_all)

a = Cat()
print(a.all)

a.all = "Barsik"
print(a.all)

a.set_all("Sary", 5)
print(a.all)


