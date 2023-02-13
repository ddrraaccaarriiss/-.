# 1 наследование
# 2 инкапсуляция
# 3 полиморфизм




print(dir(SuperHero)) #позволяет узнать сколько методов есть
print(SuperHero.mro())# позволяет узнать от чего унаследованы классы
print(Sky_hero.mro())# позволяет узнать от чего унаследованы классы


def crit(self):
    Villain.crit(self)# perezapisat metody classa tipo nasledstvie


# cat = 'Beka'
# cat = 'esdgf'
#
#
# def may(a):
#     print(f'{a} мяукает')
#
#
# may(cat)
#

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
    print(cat1.name,cat1.age)
    print(len(cat1))
    cat1.may()
    print(cat1)
    cat1.x2()
    cat1.x2()
    print(cat1)
    print(cat1)
#########################################################################################################
class A1:
    p=True
    def a(self):
        print('A')


class A2(A1):
    def A1(self):
        super().a()
    def a(self):
        print('A2')


class A3(A2):...

# print(dir(A2)) позволяет узнать сколько методов есть
print(A1.mro())
print(A2.mro())

#########################################################################################################3

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
        self.age *= 9
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

#########################################################################################################################3

# 1 наследование
# 2 полиморфизм

class Person:
    people = 'people'
    head = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def prints(self):
        print(f'мое имя {self.name} мой возраст {self.age}')


per1 = Person('Ислам', 10)


# per1.prints()
# per1 = Person('Ислам', 10)
# per1.prints()
# per1 = Person('Ислам', 10)
# per1.prints()
# per1 = Person('Ислам', 10)
# per1.prints()


class Person2(Person):

    people = 'Monster in programing'

    def __init__(self, name, age, super_power):
        super().__init__(name, age)
        Person.__init__(self, name, age)
        self.power = super_power

    def prints(self):
        print(f'мое имя {self.name} мой возраст {self.age} и я умею {self.power}')

    def x(self):
        # super().prints()
        Person.prints(self)


per2 = Person2('Болотбек', 2, 'летать')
per2.prints()
per1.prints()
per2.x()
# print(per1.people, per2.people)

#######################################################################################################################

""" rabota s zashishennymi argumentami i metodami """

class Bank:
    def __init__(self, __name, balanse):
        self.__name = __name
        self.balanse = balanse
    def __str__(self):
        return f' name is: {self.__name}\n' \
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

    def _take_balanse(self):
        self.balanse += Bank(self.balanse)



aku = Bank("Aku",100)
sake = Bank("Sake",100)
take = Bank("Take",100)


# rabota s zashishennymi argumentami i metodami

print(take._Bank__name)
take._Bank__name = " take2"
take._Bank__jackpot()
print(take)


aku.moneyX()
print(aku)

sake._kill()
sake.kill()
print(sake)

take.jackpot()
take._Bank__jackpot()
print(take)

# a._take_balanse(s)



######################################################################################################3


""" Set i get .  set = izmenaet argument. get = pokazyvaet argumenty.  set mojet bez geta s print(). a get bez seta ne mojet  """

""'1 pervyi variant otdalno na kajdyi argument pishetsya otdelno '""

class Bank:
    def __init__(self, __name, balanse):
        self.__name = __name
        self.balanse = balanse
    def __str__(self):
        return f' name is: {self.__name}\n' \
               f'balanse is: {self.balanse}'



    def set_name(self,name):
        self.__name = name

    def get_name(self):
        print(self.__name)




    def set_balanse(self, balanse):

        self.balanse = balanse

    def get_balanse(self):
        print(self.balanse)




aku = Bank("Aku",100)
sake = Bank("Sake",100)
take = Bank("Take",100)

# aku.get_name()
# aku.set_name("beku")
# aku.get_name()
# print(aku)


sake.get_balanse()
sake.set_balanse(122)
sake.get_balanse()
print(sake)



""'2  variant vmeste pishetsya na vse argumenty  i prosit budet na kajdyi argument '""



class Bank:
    def __init__(self, __name, balanse):
        self.__name = __name
        self.balanse = balanse
    def __str__(self):
        return f' name is: {self.__name}\n' \
               f'balanse is: {self.balanse}'



    def set_name_balanse(self,name,balanse):
        self.__name = name
        self.balanse = balanse

    def get_name_balanse(self):
        print(self.__name)
        print(self.balanse)


aku = Bank("Aku",100)

aku.get_name_balanse()
aku.set_name_balanse("beku",333)
aku.get_name_balanse()
print(aku)

#####################################################################################################################3


""""  @property int1  """"

class Pers:
    def __init__(self, name, old):
        self.__name = name
        self._old = old

    def __str__(self):
        return f' name is: {self.__name}\n' \
               f' name is: {self._old}\n' \

    def get_old(self):
        return print(self._old)

    def set_old(self, old):
        self._old = old

    old = property(get_old,set_old)
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)

p = Pers("Aku", 20)

p.set_old(35)
p.get_old()

p.old=45
p.old

print(p)

###############################################################

""""  @property int2  """"


class Pers:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def __str__(self):
        return f' name is: {self.__name}\n' \
               f' name is: {self.__old}\n' \

    @property
    def old(self):
        return print(self.__old)

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old


p = Pers("Aku", 20)
del p.old # udalaet zashishennyi argumenta old __old

p.old=45 # obrato prisvaevaet snachenie old
p.old

print(p)

# p.get_old=35
# print(p.get_old)

#############################################################3

""""  @property int 2.1  """"

class Cat:
    xvost = True

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return print(self._name)


    @name.setter
    def name(self, name):
        self._name = name



    def __str__(self):
        return f'name is {self._name}\n' \
               f'age is {self.age}'


a = Cat("bek",12)

a.name= "www"
a.name
print(a)

###################################################################################################################################33

###########################################################################################################################################3

""" zadachi iz int """

#  Предположим, что отдел кадров от нас требует хранить следующие персональные данные:
#
# ФИО;
# возраст (целое число от 14 до 120);
# серию и номер паспорта в формате xxxx xxxxxx, где x – цифра (от 0 до 9);
# вес, в кг (вещественное число от 20 и выше).
# Первое, над чем задумывается программист, как описать эти данные на уровне программы. Я сделаю, следующим образом:
#
# ФИО – список из трех строк: фамилия, имя, отчество;
# возраст – целое число;
# паспорт – строка в нужном формате;
# вес – вещественное число.
# Запишем этот класс со следующим инициализатором:

from string import ascii_letters  # latinskie bukvy

class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight


# def __init__(self, fio, old, ps, weight):
#     self.verify_fio(fio)
#
#     self.__fio = fio.split()
#     self.old = old
#     self.passport = ps
#     self.weight = weight


    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат записи ФИО")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис")


    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне [14; 120]")


    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")


    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")


    @property
    def fio(self):
        return self.__fio


    @property
    def old(self):
        return self.__old


    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old


    @property
    def passport(self):
        return self.__passport


    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps


    @property
    def weight(self):
        return self.__weight


    @weight.setter
    def weight(self, w):
        self.verify_weight(w)
        self.__weight = w

p = Person('Дюшембиев Турат Рыскелдиевич', 25, '1234 567890', 70.0)
p.old = 28
p.passport = '4567 123456'
p.weight = 68.0
print(p.__dict__)
# {'_Person__fio': ['Дюшембиев', 'Турат', 'Рыскелдиевич'], '_Person__old': 28, '_Person__passport': '4567 123456', '_Person__weight': 68.0}

###################################################################################################################################33




###########################################################################################3
 """ Nujno dopolnit argumenty proporti """

class Cat:
    xвост = True

    def __init__(self, name, age):
        self._name = name
        self.age = age


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name, age):
        self._name = name
        self.age = age


    def __str__(self):
        return f'name is {self._name}\n' \
               f'age is {self.age}'


a = Cat("bek",12)

a.name="aka"
print(a.name)



# Проперти - это сущность, прикидывающаяся обычным полем класса. У обычного поля класса нет никаких именованных аргументов или значений по-умолчанию - есть только одно значение. Если вам нужно все это, то используйте просто метод класса. –
# insolor
#  25 апр 2020 в 11:58
# Показать ещё 1 комментарий
# 1 ответ
# Сортировка:
#
# Наивысший рейтинг (по умолчанию)
#
# 1
#
#
# Додумался до такого варианта с применением функции property():

class A:

    def __init__(self):
        self.__x = 12
        self.__y = 42

    def get_var(self):
        return f'X: {self.__x}, Y: {self.__y}'

    def set_var(self, val, val2=None):
        if val2 is not None:
            self.__y = val2

        self.__x = val

    var = property(get_var, set_var)

a = A()
print(a.var)  # X: 12, Y: 42
a.var = 678
print(a.var) # X: 678, Y: 42
a.set_var(3, 77)
print(a.var)  # X: 3, Y: 77




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




###########################################################################################3
