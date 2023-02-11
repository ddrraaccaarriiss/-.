# : создать калькулятор на классах при помощи магических методов(
# add() – для операции сложения;
# sub() – для операции вычитания;
# mul() – для операции умножения;
# truediv() – для операции деления.... )

class Culculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return f'num one  is: {self.num1}\n' \
               f'num two  is: {self.num2}\n' \
               # f'resalt is {self.resalt}'
    def __add__(self):
        return print(f'{self.num1} + {self.num2} = {self.num1 + self.num2}')


    def __sub__(self):
        return print(f'{self.num1} - {self.num2} = {self.num1 - self.num2}')


    def __mul__(self):
        return print(f'{self.num1} * {self.num2} = {self.num1 * self.num2}')

    def __truediv__(self):
        return print(f'{self.num1} // {self.num2} = {self.num1 // self.num2}')


a = Culculator(10,2)
a.__add__()
a.__sub__()
a.__mul__()
a.__truediv__()

print(a)



