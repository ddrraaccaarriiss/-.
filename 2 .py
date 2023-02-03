# 1 наследование
# 2 инкапсуляция
# 3 полиморфизм


cat = 'Beka'
cat = 'esdgf'


def may(a):
    print(f'{a} мяукает')


may(cat)


class Cat:
    xвост = True

    def may(self):
        print(self.name, 'мяукает')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'name is {self.name}\n' \
               f'age is {self.age}'

    def __len__(self):
        return len(self.name)

    def x2(self):
        self.age *= 2
        print(self)


# print(type(cat))
#
# class Str:...

if __name__ == '__main__':
    cat1 = Cat('болотбек', 4)
    cat1.name = 'Акылай'
    cat1.age = 3
    # print(cat1.name,cat1.age)
    print(len(cat1))
    cat1.may()
    print(cat1)
    cat1.x2()
    print(cat1)




k;l