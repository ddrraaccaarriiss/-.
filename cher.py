"""Прожект новые знания"""



###################################################################################################################################3


"""      Functions       """


"""Opisanie funksii"""
print(help(len))# Opisanie funksii
"""Tolko dokumentasya"""
print(len.__doc__)# Tolko dokumentasya


a = [1,2,3,4]
b = max(a) +1
print(b)# 5
#5

# Функция в python - объект, принимающий аргументы и возвращающий значение.
# Обычно функция определяется с помощью инструкции def.

def get_func():
    return "Hello world" # bez retorna  None

print(get_func())
# Hello world
######################################
def multiply(a, b):
  return a * b

multiply(10, 19)
# 190
a = multiply(2,3)
print(a)
#6

########################################
# Допустим вы создали функцию, которая конкатенирует имя и фамилии и приветствует человека:
def welcome(name, lastname):
    return f"Hello, {name} {lastname}"
welcome("John", "Snow")# позиционные аргументы
# Hello, John Snow
welcome("Snow", "John")# pervyi eto vsegda zanimaet pervyi argument
# Hello, Snow John

# mojno spesialno ukazat
welcome(lastname="Snow", name="John") # dict(a=1, b=2)

# mojno ukazat posle glavnogo argumeta
welcome("John", lastname='Snow')
############################################################
# funk moduli
def find_power(number=2, power=2):
  return number ** power

find_power(5, 5)
# 3125

find_power(number=5)
#25

find_power()
#4

###########################################################33
# you can call function inside other function
def subtract(num1, num2):
  return num1 - num2

def add(num1, num2):
  return num1 + num2

def arithmetic(a, b):
  subtraction = subtract(a, b)
  addition = add(a, b)
  # print(f"Result of subtraction: {subtraction}\nResult of addition: {addition}")
  return subtraction, addition


var = arithmetic(b=5, a=2)
print(var)
# (-3, 7)

add(9, 10)
#19

subtract(15, 5)
#10



########################################################
# funk moduli
a = pow(3,3)
print(a)#27

############################################33

a = "HELLO".lower()
print(a)
#hello

##################################################33

# vstroennye funksii

#round()
# len()
# abs()
# sum(), max(), min()
# input("Enter number: ")
# zip()
# enumerate()

########################################################

users = []
def add_user(user) -> None:
  users.append(user)

add_user("John")
add_user("Raychel")
print(users)
# ['John', 'Raychel']

#############################################3

# mojem napisat komentarii nashemu funcsii
def func(num1: int, num2: int) -> float:
  """Return division
  operation num1 by num2
  """
  return num1 / num2

func(1, 2)
#0.5





















""" Primery """





""" Функция min переписали """

lst = [20, 5, 3, 10, 4]
def min1(iterable):

    min_value = iterable[0]
    for i in iterable:
        if i < min_value:
            min_value = i
    return min_value

print(min1((lst)))
print(min(lst))

""" Функция min переписали работает на лист """

lst = [20, 5, 3, 10, 4]
def min1(iterable):
    iterable.sort()
    return  iterable[0]

print(min1((lst)))
print(min(lst))

""" Функция min переписали работает на vseh """

kortej = 2,3,4,5
lst = [20, 5, 3, 10, 4]
def min1(iterable):
    iterable = sorted(iterable)
    return  iterable[0]

print(min1((lst)))
print(min(lst))
print(min1((34, 56, 87, 12)))
print(min1((kortej)))
print(type(kortej))







""" Отражение словo """

def is_mirror(string = 'hello'):
    if string == string[::-1]:
        return True
    elif string == string:
        return False


print(is_mirror('dovod'))
print(is_mirror('python'))
print(is_mirror())



"""funksiya len perepisali"""

def len1(sequence: list) -> int:
    """Принимает последовательность, возвращает количество элементов"""
    counter = 0
    for _ in sequence:
        counter += 1
    return counter
# a ='tyrat'
a = [1,2,3,4,]
print(len1(a))



"""Функции, аргументы: *args, **kwargs."""

"""primery  *args vozvrashaet v kortej"""
def plus(*args):
    print(type(args))

    return sum(args)
a = plus(1, 1, 1.6, 1, 1, 1, 1)
print(a)



"""primery  **kwargs vozvrashaet v slovar"""

def menu(**kwargs):
    print(kwargs)
    return kwargs
menu(drink=['cola', 'tea'], eat='pizza', a=1, book='python')



##############################
"""Okruglit i posle zapitoi 2"""
a = float(input('enter: '))
b = float(input('enter: '))
c = a + b
print(round(c,2))
#############################
"""primery funksii kak dobavlat v spisok"""


students = {
    "азамат": 10,
    "мирлан": 9,
    "сабина": 7
}
def add_student(name, rate):
    students[name] = rate
    return students
add_student('ruslan', 10)
print(students)


"""Функция калькулятор"""

def calculator(n1, operator, n2):
    if operator == '+':
        return n1 + n2
    elif operator == '-':
        return n1 - n2
    elif operator == '**':
        return n1 ** n2
    elif operator == '%':
        return n1 % n2
    elif operator == '/':
        return n1 / n2
    else:
        print('Непонятная команда')

print(calculator(2, '**' ,3))
print(calculator(5, '+' , 9.6))
print(calculator(20, '%' ,3))
print(calculator(30, '/' ,2))
print(calculator(10, '-' ,5))
print(calculator(10, 'плюс', 5))

""" Возвращает в список primery  """

def up_word(word: str):
    return word.title()
def show_word(func, *iterable):
    return [func(i) for i in iterable]

print(show_word(up_word,'oop','tut','bishkek'))
print(show_word(len, 'oop', 'bishkek', 'kgz'))



"""   Zadachi  """











####################################################################################################################################3


"""Экранирование"""

# Экранированные последовательности, также называемые escape-последовательности,
# могут состоять из одного или нескольких символов после обратной косой черты:
#
# \ в самом конце строки Игнорируется, строка продолжается на новой строке
# \ Сам символ обратного слеша (остается один символ )
# \' Апостроф (остается один ‘)
# \" Кавычка (остается один символ ")
# \n Новая строка (перевод строки)
# \t Горизонтальная табуляция
# \u… 16-битовый символ Юникода в 16-ричном представлении
# \U… 32-битовый символ Юникода в 32-ричном представлении
# \x… 16-ричное значение
# \o… 8-ричное значение







#################################################################################################################################3


""" List Comprehension """

# bez filtra budet polnyi obekt
# s filtrom ne vse

########################################################################3
# bez lk
list_ = []
for num in range(1, 20):
 list_.append(num)
print(list_)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# s LK
list_ = [i for i in range(1, 20)]
print(list_)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# Здесь конструкция [i for i in range(1,20)] является генератором списка.
# Вся конструкция заключается в квадратные скобки, что как бы говорит, что будет создан список.
# Внутри квадратных скобок можно выделить три части:
#
# 1) что делаем с элементом (в данном случае ничего не делаем, просто добавляем в список),
#
# 2) что берем (в данном случае элемент i),
#
# 3) откуда берем (здесь из объекта range).

# Части отделены друг от друга ключевыми словами for и in.

list_ = [str(i) for i in range(1, 20)]
print(list_)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

############################################################

# s lk
numbers = [2, 5, -5, 6, 7, 8]
list_ = [x**2 for x in numbers]
print(list_)
# bez lk
list_ = []
for num in numbers:
  list_.append(num ** 2)
print(list_)


#################################################################
# bez lk
list_ = list(range(1, 50))

new_list = []
for num in list_:
 if num % 3 == 0:
  new_list.append(num)
 else:
  continue
print(new_list)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# s lk
compr_list = [num for num in list_ if num % 3 == 0]
print(compr_list)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
##########################################################
# multiple conditions
list_1 = [10, 5, 8, -4, -8, 20, 3, 4]
list_2 = [num for num in list_1 if num % 2 == 0 and num > 0]
# берем те x, которые одновременно четные и больше нуля
print(list_2)
# [10, 8, 20, 4]

##################################################3

# отфильтровать список в котором только строки и вытащить строки в котором только цифры
strings = ['1997', '1997год', '1997г', '2001', '2002y', '2008']
filtered_list = [string for string in strings if string.isdigit()]
print(filtered_list)
# ['1997', '2001', '2008']


# получить список с длинами строк-имен
names = ['john', 'raychel', 'peter', 'jessica']
names2 = [len(name) for name in names if len(name) > 5]
print(names2)
# [7, 7]
# lengths = [4, 7, 5, 7]
###########################################################################3
# a)Условия ветвления пишутся не после, а перед итератором.
# b) If else не будет являться фильтром перед выполнением list comprehension ,
# проще говоря сначала срабатывает фильтр объекта итератора(переменная x прошла фильтр, который написан справа),
# но в зависимости от условия ветвления может быть обработана по разному, Показано на следующем примере:

list_1 = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
list_2 = [x if x < 0 else x**2 for x in list_1]
# Если x-отрицательное берем x, в остальных случаях берем квадрат x print(list_2) # [-5, -12, 0, 1, 4, 64, 16, 25, 49]
list_1 = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
list_2 = [x if x < 0 else x**2 for x in list_1 if x != 0]


# Тот же самый пример только с использованием условия ветвления и фильтра
# (условия ветвления) - слева перед итератором
# (условия фильтра) - справа
list_1 = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
list_2 = [x if x < 0 else x**2 for x in list_1 if x % 2 == 0]
# фильтруем объекты, если x делиться на 2 без остатка, то оставляем
# Если x-отрицательное берем x, в остальных случаях берем квадрат x print(list_2) # [-12, 0, 4, 64, 16]
#########################################################################33


names = ["raychel", "john", "peter", "jessica", "jill", "steven", "Catherine", "james", "steven123", "Kira123"]
filtered_names = [x.upper() if len(x) >= 5 else x.lower()
                  for x in names
                  if x.isalpha()]
print(filtered_names)
# ['RAYCHEL', 'john', 'PETER', 'JESSICA', 'jill', 'STEVEN', 'CATHERINE', 'JAMES']

########################################################################
#. Рассмотрим ситуацию максимально приближенную к реальности:
# Предположим мы получили данные о пользователей в виде словаря из стороннего ресурса(апи) и наша задача сделать статистику возраста юзеров.
# a) Сколько процентов юзеров возраста больше 18
# b) Сколько процентов юзеров возраста меньше 18

john = {'name': 'John', 'age': '22'}
raychel = {'name': 'Raychel', 'age': '23'}
peter = {'name': 'Peter', 'age': '17'}
alice = {'name': 'Alice', 'age': '15'}
tom = {'name': 'Tom', 'age': '31'}
users = [john, raychel, peter, alice, tom]
print(users)
# [{'name': 'John', 'age': '22'},
#  {'name': 'Raychel', 'age': '23'},
#  {'name': 'Peter', 'age': '17'},
#  {'name': 'Alice', 'age': '15'},
#  {'name': 'Tom', 'age': '31'}]
bigger = [user["name"] for user in users if int(user['age']) >= 18]
smaller = [user["name"] for user in users if int(user['age']) < 18]
print(bigger)
print(smaller)
# ['John', 'Raychel', 'Tom']
# ['Peter', 'Alice']

bigger_percent = len(bigger) * 100 / len(users)
smaller_percent = len(smaller) * 100 / len(users)
print(f"Percentage of users at age more than 18: {bigger_percent}%")
print(f"Percentage of users at age less than 18: {smaller_percent}%")

# 5 - 100%
# 3 - x%
# x = 3 * 100 / 5
Percentage of users at age more than 18: 60.0%
Percentage of users at age less than 18: 40.0%



# С помощью list comprehension можно сделать вложенные выражение, как и вложенные циклы
# bez lk s pomochu vlojennyx syklov
matrix = [
 [0, 1, 2, 3],
 [10, 11, 12],
 [20, 21, 22],
 [30, 31, 32],
]
uncompress = []
for row in matrix:
 for n in row:
  uncompress.append(n)
print(uncompress)
# [0, 1, 2, 3, 10, 11, 12, 20, 21, 22, 30, 31, 32]

# s lk
uncompress_compr = [n for row in matrix for n in row]
print(uncompress_compr)#[0, 1, 2, 3, 10, 11, 12, 20, 21, 22, 30, 31, 32]
###########################################################################

# Хочу затронуть еще одно отличие между List comprehension(генераторами списков) и создание с помощью цикла for
# List comprehension(генераторами списков) они быстрее генерируют список чем обычные цикл, покажу на примере:
# Для того, чтобы проверить и доказать нам нужно создать список с 100 тысяч чисел и проверить через модуль datetime
# loop
from datetime import datetime
start = datetime.now()
list_ = []
for i in range(10**6):
 list_.append(i)
print(datetime.now() - start)
# 0:00:00.149033

# list comprehension
from datetime import datetime
start = datetime.now()
list_ = [x for x in range(10**6)]
print(datetime.now() - start)
# 0:00:00.075552
########################################################################

# Создайте список имён. Далее создайте отфильтрованный список имён, где будут содержаться имена, начинающиеся с гласных букв.
# Используйте list comprehension.
names = ["John", "Alice", "Raychel", "Yunus", "Kate", "Robin", "Eric"]
vowels = tuple("aoeyiu")
print(vowels)#('a', 'o', 'e', 'y', 'i', 'u')

names = [name for name in names if name.lower().startswith(vowels)]
# ['Alice', 'Yunus', 'Eric']
#########################################################################

# Замените все буквы a на символ *
string = "Anuar is an amazing actor."
lst = ["*" if letter.lower() == 'a' else letter for letter in string]
print(lst)
''.join(lst)
# ['*', 'n', 'u', '*', 'r', ' ', 'i', 's', ' ', '*', 'n', ' ', '*', 'm', '*', 'z', 'i', 'n', 'g', ' ', '*', 'c', 't', 'o', 'r', '.']
# *nu*r is *n *m*zing *ctor.

####################################################################

# Дано предложение 'In 1984 there were 13 instances of a protest with over 1000 people attending'.
# Получите список чисел из этого предложения.
string = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
lst = string.split()
lst = [int(word) for word in lst if word.isdigit()]
# [1984, 13, 1000]







""" zadachi """






"""#3 list komprihej  (kopirovka) i uslovie"""

# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin','jetigen','tilek','bob']
# new = [name.upper() for name in objects if len(name) > 6]
# print(objects,new,sep='\n')




# 1. Создайте список из нечётных целых чисел в промежутке от 1 до 50.

lst = [i for i in range(1, 50) if not i % 2 == 0]
print(lst)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]


# 2. Дан список int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]. Запишите в новый список только четные числа, которые больше нуля.
int_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
lsst = [i for i in int_list if i % 2 == 0 and i > 0 ]
lsst
# [2, 4]


# 3. Создайте список из квадратов всех чисел от 1 до 25 (включительно).
# lls = [num * num if num  else num  for num in range(1,26) ]
lls = [i * i for i in range(1,26) ]
print(lls)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]



# 4. Объявите новый список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] и конвертируйте строковые данные в целочисленные.
str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
conv = [int(i) for i in str_list]
# conv = [ int(i) if i else i for i in str_list ]
conv
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 5. Пройдитесь по промежутку чисел от 1 до 10 (включительно), если число нечётное,
#  запишите в список само число, если же чётное,
#  то квадрат этого числа.

a = [ i * i if i % 2 == 0 else i  for i in range(1,11) ]
a
# [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]


# 6. Создайте список из 10 произвольных имён, затем пройдитесь по данному списку и если имя состоит меньше
# чем из 4 букв замените имя на 'shorter', а если больше на 'longer'.
names = ['Bob', 'Tim', 'Bill', 'Thomas', 'Michael', 'Robert']
lst = ["'shorter'" if len(i) <= 4 else 'longer'  for i in names]
lst
# ['shorter', 'shorter', 'shorter', 'longer', 'longer', 'longer']


# 7. Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
num1 = range(1,11)
num2 = range(1,11)
a1 = {key: val * val  for key, val in zip(num1,num2)}
a1
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}



# 10. Дан словарь, удалите из него все элементы с пустыми значениями.
# Например: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} -> {'b': 1, 'c': 2, 'e': 3}
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# a = {key: value for key, value in a.items() if value}
for key, value in list(a.items()):
  if value == None:
    a.pop(key)
print(a)
# cherez listcompriheng
a = {key: val for key, val in a.items() if val}
print(a)

##################################################################################################################################3



"""  Dictionary Comprehension  """




dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3, "e": 3}
dict_123 = {value: key for key, value in dict_abc.items()}
print(dict_123)
# {1: 'a', 2: 'b', 3: 'e'} #  ostalsa poslednyi

########################################################33

# изменить my_dict так, чтобы все значения были умножены на 2
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
doubled = {key: value * 2 for key, value in my_dict.items()}
print(doubled)
# {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

############################################################3

# В приведенном выше примере мы только изменили значения и передали ключи
# в новый словарь как есть, но мы могли бы изменить и ключи, и значения одновременно,
# если бы захотели. Например, если я хочу использовать заглавные буквы my_dict и умножить все числа на 3

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
my_dict = {key.upper(): value * 3 for key, value in my_dict.items()}
my_dict
# {'A': 3, 'B': 6, 'C': 9, 'D': 12, 'E': 15}


# Условные выражения в dict comprehension точно также как и в list comprehension
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': -4, 'e': -5}
new_dict = {key: val for key, val in my_dict.items() if val < 0}
print(new_dict)
my_dict.items()
# {'d': -4, 'e': -5}
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', -4), ('e', -5)])

#####################################################################3

# Дан список с именами студентов и список с их баллами
# Создать словарь, где ключи - имена этих студентов, а значения - их баллы, используя dict comprehension.
# Так же имена студетов должны начинаться с заглавной буквы
students = ["john", "pete", "cole", "melissa", "bob"]
scores = [78, 56, 90, 88, 73]
# zip() pozvalaet stroit slovar
#1
d = {key.capitalize(): value for key, value in list(zip(students, scores))}
d
# {'John': 78, 'Pete': 56, 'Cole': 90, 'Melissa': 88, 'Bob': 73}

#2
dict(zip([i.capitalize() for i in students], scores))
# {'John': 78, 'Pete': 56, 'Cole': 90, 'Melissa': 88, 'Bob': 73}

##########################################################################

# Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов,
# а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь,
# присвоив по 2 экстра балла каждому студенту по каждому предмету.
a = {'Sam':
      {'math': 95, 'literature': 88},
     'Alice':
      {'math': 70, 'literature': 98}
}

d = {key: {inner_key: inner_value + 2 for inner_key, inner_value in value.items()}
     for key, value in a.items()}
d
# {'Sam': {'math': 97, 'literature': 90},
 # 'Alice': {'math': 72, 'literature': 100}}
##########################################################################

# Дан словарь с продуктами, которые есть и нет в холодильнике.
# Получить список продуктов, которых нет в холодильнике
products = [
    {
        'title': 'Milk',
        'in_stock': True
    },
    {
        'title': 'Eggs',
        'in_stock': False
    },
    {
        'title': 'Cheese',
        'in_stock': False
    },
    {
        'title': 'Bread',
        'in_stock': True
    }
]
lst = [product["title"] for product in products if not product["in_stock"]]
lst
# ['Eggs', 'Cheese']

[product["title"].upper() if product["in_stock"]
 else product['title'].lower()
 for product in products]
# ['MILK', 'eggs', 'cheese', 'BREAD']




"""  zadachi  """




# 8. Запросите у пользователя ввод числа n значением от 1 до 10. Затем пройдитесь по промежутку чисел от 1 до 500 и
# запишите в словарь только те числа, которые кратны n. Ключом будет само число, а значением его квадрат.

num0= int(input('Введите число от 1 до 10: '))
num1 = range(1,500)
num2 = range(1,500)

dc = {key: value * value  for key, value in list(zip(num1, num2)) if key %num0 == 0 and value %num0 ==0 }
print(dc)
# {10: 100, 20: 400, 30: 900, 40: 1600, 50: 2500, 60: 3600, 70: 4900, 80: 6400, 90: 8100, 100: 10000





# 9. Дан словарь, в котором значениями являются целые числа. Пройдитесь по элементам и замените значениям списком чисел от 1 до данного числа.
# Например: a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} -> {'a': [1], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4], 'd': [1, 2, 3]}

a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
s = { key: list(range(1,value+1))   for key,value in a.items()}
s
# {'a': [1], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4], 'd': [1, 2, 3]}





# 10. Создайте словарь, где ключами будут строки, а значениями произвольные числа.
# Затем пройдитесь по элементам и запишите вместо значения строку 'even', если значение четное, а если нет то 'odd'.
my_dict = {'a': 10, 'b': 21, 'c': 3, 'd': 14, 'e': 5, 'f':74}
my_dict2= {key: 'even' if  value %2 == 0 else 'odd' for key, value in my_dict.items() }
my_dict2
# {'a': 'even', 'b': 'odd', 'c': 'odd', 'd': 'even', 'e': 'odd', 'f': 'even'}





# 10. Дан словарь, удалите из него все элементы с пустыми значениями.
# Например: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} -> {'b': 1, 'c': 2, 'e': 3}
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# a = {key: value for key, value in a.items() if value}
for key, value in list(a.items()):
  if value == None:
    a.pop(key)
print(a)
# {'b': 1, 'c': 2, 'e': 3}


# cherez listcompriheng
a = {key: val for key, val in a.items() if val}
print(a)
# {'b': 1, 'c': 2, 'e': 3}







#############################################################################################################################3


"""    Set comprehension    """

# Отличие от генераторов списков, генератор множеств возвращает уникальные элементы
# и неупорядочены остальное все похоже с list comprehension
# ot lk otlichaetsya s figurnymi skopkami

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_set = {i for i in list_a if i > 0}
print(my_set) # - порядок случаен
# {1, 2, 3, 4, 5}

###################################################3

# Создайте список чисел от 1 до 10. Создайте множество, в котором поместите квадраты этих чисел, если число делится на 2 без остатка,
# в противном случае поместите в список утроенные значения чисел.
numbers = list(range(1, 11))
numbers
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

set_ = {i ** 2 if i % 2 == 0 else i * 3 for i in numbers}
set_
# {3, 4, 9, 15, 16, 21, 27, 36, 64, 100}

############################################################################3

# Дана информация с постами и лайкнувшими их юзерами.
# 1. Определить самый популярный пост
# 2. Среди трех постов определить юзеров, которые лайкнули все три поста.
# 3. Среди этих пользователей случайно выбрать одного кандидата для выигрыша

users = {
    'post1': ['Aikol', 'Jannat', 'Madina', 'Atai', 'Nargiza', 'Ulan', 'Alibek', 'Bakyt'],
    'post2': ['Jannat', 'Ulan', 'Gulmira', 'Atai', 'Madina', 'Bayastan'],
    'post3': ['Aikol', 'Atai', 'Jannat', 'Nargiza', 'Ulan'],
}

# 1.
likes = {post: len(values) for post, values in users.items()}
likes
# {'post1': 8, 'post2': 6, 'post3': 5}

popular_post = None
popular_likes = 0
for key, value in likes.items():
  if value > popular_likes:
    popular_likes = value
    popular_post = key
print(popular_post)
# post1

# 2.
lst_ = [set(i) for i in users.values()]
lst_
# [{'Aikol', 'Alibek', 'Atai', 'Bakyt', 'Jannat', 'Madina', 'Nargiza', 'Ulan'},
#  {'Atai', 'Bayastan', 'Gulmira', 'Jannat', 'Madina', 'Ulan'},
#  {'Aikol', 'Atai', 'Jannat', 'Nargiza', 'Ulan'}]


lst_[0] & lst_[1] & lst_[2]  # start &=
# {'Atai', 'Jannat', 'Ulan'}


start = lst_[0]
for i in lst_:
  start &= i

start
# {'Atai', 'Jannat', 'Ulan'}

# 3
import random
winner = random.choice(list(start))
winner
# Jannat




##############################################################################################################################################

""" Исключения: Try-Except"""


# 6. Программа по конвертации курса валют

kurs = {
    'buy': {
        'dollar': 84.50,

        'euro': 98.20,
        'rub': 1.40
    },
    'sell': {
        'dollar': 84.90,
        'euro': 99.40,
        'rub': 1.70
    }
}



while True:
  try:
    operation = input("Choose operation (buy, sell): ").lower() # buy
    data = kurs[operation]
    # print(data)
  except KeyError:
    print("Enter correct operation")
    continue
  else:
    valuta = input("Choose currency (dollar, euro, rub): ").lower() # dollar
    try:
      exchange = data[valuta]
      summa = int(input("Enter amount: "))
      if summa <= 0:
        print("Amount should be positive number and more than zero!")
        continue
      else:
        if operation == "buy":
          result = summa * exchange
          print(f"Your money: {result} som")
        else:
          result = summa / exchange
          print(f"Your money: {round(result, 2)} {valuta}")

    except KeyError:
      print("Enter correct currency!")
      continue
    except ValueError:
      print("Enter correct amount!")
      continue
    else:
      to_continue = input("Do you want to continue? (yes/any symbol): ").lower()
      if to_continue == "yes":
        continue
      else:
        break
print("Thank you! The End.")










#ZeroDivisionError: division by zero
number_a = 0
number_b = 42
result = number_b / number_a
print("The end of the program.")

number_a = 0
number_b = 42
result = 0
try:
 result = number_b / number_a
except ZeroDivisionError:
 print("Division by zero")

print(result)



#«Голое» исключение
try:
 "a" / 1
 # 0/42
except:
 print("You cannot divide by zero!")


#except KeyError:
my_dict = {"a": 1, "b": 2, "c": 3}
try:
 value = my_dict["d"]
except KeyError:
 print("That key does not exist!")

#except IndexError:
my_list = [1, 2, 3, 4, 5]
try:
 my_list[6]
except IndexError:
 print("That index is not in the list!")



# Import Error module ili fail error mojet byt
try:
  from main import greetings
  print(greetings)
except ImportError:
  print("Greetings not found")

#Кроме того, если вы хотите проверить несколько исключений,
# вы можете повторить except операторы для разных типов ошибок.
# Вот пример блоков try / исключением, которые ищут NameError:
try:
 1 / 0
 print(ourVariable)
except NameError:
 print('ourVariable is not defined')
except ZeroDivisionError:
 print('Division by zero')

#Точно так же, если ваш код работает правильно, вы можете добавить else ключевое слово.
# Используя предложение else, вы можете определить код, который будет запускаться в случае,
# если исключений нет. Вот пример:

num1 = 5
num2 = 0
try:
  result = num1 / num2
except ZeroDivisionError:
  print("Can't divide zero")

print(f"Result: {result}")

try:
  r = 1 / 0
except ZeroDivisionError:
  print('Zero ...')
else:
  print(r)

#Но что, если мы хотим, чтобы сообщение печаталось как в случае возврата ошибки,
# так и в случае отсутствия ошибки? Вот где finally приходит блок. Если вы определите предложение finally,
# его содержимое будет выполнено независимо от того, выдает ли блок try / exc ошибку. Вот пример:

num1 = 5
num2 = 0
try:
  result = num1 / num2
except ZeroDivisionError:
  print("Can't divide zero")
else:
  print(f"Result: {result}")
finally:
  print("Program finised!")
# Can't divide zero
# Program finised!




# multiple exceptions with tuple
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) + int(num2)
except (ValueError, TypeError):
  print("Something went wrong")
except (ZeroDivisionError, ArithmeticError):
  print("Mathematica error")
except (ImportError, ModuleNotFoundError):
  print('Import error')
except:
  print("Unknown error")
else:
  print(result)
finally:
  print("The end of the program")
# Enter first number: 5
# Enter second number: d
# Something went wrong
# The end of the program



# find the exception description
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) + int(num2)
  print(result)
except Exception as e:
  print(e)



#1 find the exception name
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) + int(num2)
  print(result)
except ValueError:
  result = num1 + num2
  print(result)
except Exception as e:
  print(type(e))


#2
a = 10
try:
  if a > 9:
    print(a)
except Exception as e:
  print(e)





#except AttributeError: tuple ne imeet takogo metoda
try:
  (1, 2, 3).append(4)
except AttributeError:
  print("Ошибка атрибута")


# prinuditelnyi vyzov error
age = 16
if age < 18:
  raise ImportError("Доступ несовершеннолетним запрещен")



#Assertion Error opisanie ochipki

number = "100"
assert type(number) == int, "This is string"
print("Continue")
#AssertionError: This is string

# find the exception name esli ochipka to mojno sdelat drugoe uslovie
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) + int(num2)
  print(result)
except ValueError:
  result = num1 + num2# esli ochipka srabotaet eto
  print(result)
except Exception as e:
  print(type(e))
# Enter first number: 8
# Enter second number: hello
# 8hello




# 1. Напишите программу, которая будет запрашивать ваш возраст.
# Если пользователь вводит отрицательное число либо 0, программа должна выдать исключение: “Ваш возраст должен быть больше 0 ”.


age = input("Enter your age: ")
try:
  if int(age) <= 0:
    raise Exception("Ваш возраст должен быть больше 0")
except ValueError:
  print("Enter digit, not a letter!!!")






# 2. Есть список с продуктами. Программа должна получать названия продуктов и удалять их из списка.
# Если введенного продукта нет, программа не должна ломаться. В конце если список пустой, программа завершается и выдает "Список пуст"
products = [
    "milk",
    "bread",
    "eggs",
    "potato"
]


while products:
  item = input("Enter item: ").lower()
  try:
    products.remove(item)
  except ValueError:
    # print(type(e))
    print("Такого продукта нет в списке")
  finally:
    continue
else:
  print("Список пуст")



# 3. Создайте программу, которая предлагает выбрать размер вашего списка. Затем ждет от пользователя ввод чисел через пробел и заполняет этот список.
# Если количество чисел больше размера списка, программа выдает исключение MemoryError("Не достаточно памяти")
# Если количество чисел меньше размера списка, то остальное пространство заполняется нулями.

size = input("Choose list size: ")
numbers = input("Enter your numbers with space: ")
numbers_list = numbers.split()
if len(numbers_list) > int(size):
  raise MemoryError("Не достаточно памяти")
elif len(numbers_list) < int(size):
  empty_space = int(size) - len(numbers_list)
  zeros = [0] * empty_space
  numbers_list.extend(zeros)
  print(numbers_list)

# разширение с ноль
lst = list(range(1, 5))
lst.extend([0] * 5)
print(lst)


# 4. Напишите программу, которая требует ввода двух чисел. Если хотя бы одно из не число, выполните конкатенацию.
# В остальных случаях возвращается сумма чисел

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) + int(num2)
except ValueError:
  result = num1 + num2
finally:
  print(result)



# 5. Создайте словарь, в котором ключами будут ID, а значениями - пользовательские имена (username).
# Напишите программу, которая запрашивает у вас юзернейм и выдает ID этого юзера.
# Если же данного юзернейма нет, то программа выдает вам исключение, которое содержит следующее сообщение:
# ”Введенного юзера нет в базе данных”. Если исключение не выявилось (т.е. Данный юзернейм существует)
# программа должна приветствовать юзера по юзернейму.
# Также в любом случае программа должна в конце выдавать сообщение: “Спасибо!”
users = {
    42309: "johnsnow777",
    97050: "alice0101",
    64934: "ramylife",
    12043: "locky$$$"
}

users_reverse = {}
for key, val in users.items():
  users_reverse[val] = key
  # users_reverse.update({val: key})
  # users_reverse.setdefault(val, key)
print(users_reverse)

username = input("Enter username: ")
try:
  id_ = users_reverse[username]
  print(id_)
except KeyError:
  print("Такого юзернейма не существует")
else:
  print(f"Welcome, {username}!")
finally:
  print("Спасибо!")







""" zadachi """







# 2. Напишите программу которая будет получать два числа через input и делить одно на другое.
# Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) // int(num2)
except ZeroDivisionError:
  print("Can't divide zero")
else:
  print(f"Result: {result}")


# 3. Напишите программу, которая будет получать через инпут 2 числа и будет печатать их сумму.
# Обработайте ошибку, которая возникнет, если пользователь введёт что-то кроме числа и выведите сообщение.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
  result = int(num1) + int(num2)
except ValueError:
  print("invalid literal ")
else:
  print(f"Result: {result}")
# ValueError: invalid literal for int() with base 10: 'e'



# 4. Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если такого ключа нет.

s = {
    1: "111",
    2: "222",
    3: "333",
    4: "444"
}

try:
    print(s[5])
except KeyError:
    print(" don't find this key")

# 5. Дан список. Обработайте исключение при попытке обращения к несуществующему элементу.
a = [1, 2, 3, 4]
try:
  print(a[4])
except IndexError:
  print("index out of range")


# 6. Попытайтесь в блоке try принять 2 числа и разделить их между собой.
# В блоке except обработайте сразу 2 возможных исключения (при конвертации в int и при делении на ноль)


a = 4
b = 0
try:
  print( a  //  b)
except (TypeError,ZeroDivisionError):
  print("Mathematica error or TypeError ")


# 7. Запросите у пользователя сумму, которая у него сейчас есть в бумажнике.
# Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
# Hint: use raise
cash = 100
your = int(input(" Ведите сумму: "))

age = 16
if your < 0:
  raise ImportError("Сумма не может быть отрицательной!")
else:
  print(f' у вас на кашелке имеется: {your} сомов. ')







###############################################################################################################################
""" bool while for"""

a = 10
b = 5
print(a + b > 14) # True
print(a < 14 - b) # False
print(a <= b + 5) # True
print(a != b) # True
print(a == b) # False
c = a == b
print(a, b, c) #(10, 5, False)
s = 2
s1 = 2
print( s == s1)# здесь он сравнивает значение
print(s is s1)# здесь он проверает сылается ли он на одну ячейку в памяти


print(not 13 < 15) # False
a = 5
b = 0
print(not a)
print(not b)


# 10. Дан словарь, удалите из него все элементы с пустыми значениями.
# Например: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} -> {'b': 1, 'c': 2, 'e': 3}

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
for key, value in list(a.items()):
  if value == None:
    a.pop(key)
print(a)



# 10. Дан словарь, удалите из него все элементы с пустыми значениями.
# Например: a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} -> {'b': 1, 'c': 2, 'e': 3}
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# a = {key: value for key, value in a.items() if value}
for key, value in list(a.items()):
  if value == None:
    a.pop(key)
print(a)
# cherez listcompriheng
a = {key: val for key, val in a.items() if val}
print(a)








# 4. Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.(input:1, 5, 2, 4, 3 output: 5, 4)
numbers = [5, 4, 0, -1, 24, -89, -9, 56, 103, -56]
greater = []
index_=0
for i in numbers:
  # if index_ == 0:
  #   index_ +=1
  if i >  numbers[index_ -1]:
    greater.append(numbers[index_])
    index_+= 1
  else:
    index_ += 1
print(greater)


# 6. Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
prices = {'apple': 2, 'orange': 5, 'banana': 10}

for key, value in prices.copy().items():
  if value % 2 == 0:
    print(prices[key])
    prices.pop(key)
  else:
    continue
  print(prices)



# 7. Напишите калькулятор, который должен принимать последовательно два числа и знак операции (+, -, *, /, %).
# При этом калькулятор должен работать (принимать и выдавать результат) до тех пор пока пользователь сам не захочет остановать программу.
# Например:
# Введите первое число: 2
# Введите второе число: 5
# Выберите операция: +
# Результат: 7
# Хотите продолжить? yes -> Введите первое число ....
# Хотите продолжить? no -> Программа завершена


while True:
  n1 = int(input("Введите первое число: "))
  n2 = int(input("Введите второе число: "))
  op = input("Выберите операцию: ")

  if op == "+":
    print("Результат: ", n1 + n2)
  elif op == "-":
    print("Результат: ", n1 - n2)
  elif op == "*":
    print("Результат: ", n1 * n2)
  elif op == "//":
    print("Результат: ", n1 // n2)
  end = input("Хотите продолжить? ")
  if end == "yes":
    True
  elif end == "no":
    print("Программа завершена ")
    break





  # 5. Петя перешел в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это сделать.
# Дан список с ростом его одноклассников [165, 163, 160, 160, 157, 157, 155, 154]. Рост Пети 162. Какое место в строю он должен занять?
heights = [165, 163, 160, 160, 157, 157, 155, 154]
petya_height = 162
heights.insert(2,petya_height)
heights.sort(reverse=True)
print(heights)


# dvoinaya iterasia
message = "Hello"
for i in range(len(message)-1): # [0, 1, 2, 3]
  first_letter = message[i]
  second_letter = message[i+1]
  print(f"{first_letter} + {second_letter}") # H + e, e + l
# H + e
# e + l
# l + l
# l + o



"""Вложенные циклы"""
# tablisa umnojenia
i = 1
j = 1
while i < 10: # True
    while j < 10: # True
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

# 1	 2	3	4	5	6	7	8	9
#
# 2	 4	6	8	10	12	14	16	18
#
# 3	 6	9	12	15	18	21	24	27
#
# 4	 8	12	16	20	24	28	32	36
#
# 5	 10	15	20	25	30	35	40	45
#
# 6	 12	18	24	30	36	42	48	54
#
# 7	 14	21	28	35	42	49	56	63
#
# 8	 16	24	32	40	48	56	64	72
#
# 9	 18	27	36	45	54	63	72	81



# 1. Исходный список содержит положительные и отрицательные числа. Требуется положительные поместить в один список, а отрицательные - в другой.
numbers = [5, 4, 0, -1, 24, -89, -9, 56, 103, -56]
pos = []
neg = []
for num in numbers:
  if  num > 0:
    pos.append(num)
  elif num < 0:
    neg.append(num)
print(pos)
print(neg)

#######################################################################################################################
""" if else"""


# 9. Записать в список все числа в диапазоне от 54 до 9184 кратные 5.

num = list(range(54,9184,5))
print(num)


# 8. Вводятся два целых числа. Проверить делится ли первое на второе.
# Вывести на экран сообщение об этом, частное (в любом случае), а также остаток от деления (если он есть).

x = 10
y = 3

if y == 0:
  print("x не делится на y")
elif x // y:
  print("частное:", x // y )
  if  x % y:
    print("остаток:", x % y)

# x не делится на y
# Частное: 3
# Остаток: 1

# 7. Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).
n1 = 1
n2 = 2
n3 = 2
if n1 == n2 and n1 == n3:
  print("3")
elif n1 == n2 or n2 == n3 or n3 == n1:
  print("2")
else:
  print("0")

# 6. Даны три целых числа. Выведите значение наименьшего из них.
t = 8
o = 5
p = 2
min(t,o,p)

# 5. Даны два целых числа. Выведите значение наименьшего из них.
s = 5
f = 2
min(s,f)

# 4. Проверить введенное пользователем число если оно отрицательное то вывести “negative”,
# если положительное то “positive”, если оно равно 0 то вывести “Zero”

a = int(input('enter number: '))
if a < 0:
  print("negative")
elif a == 0:
  print("Zero")
else:
  print("positive")


# 3. Проверить введенное пользователем значение если оно больше или равно 90, вывести “Отлично ваша оценка 5”,
# если значение больше или равно 80, вывести “Здорово ваша оценка 4”, если значение больше или равно 70,
# вывести “Хорошо ваша оценка 3”, если значение больше или равно 60, вывести “Вам стоит подучить материал",
# в других случаях “вы не сдали экзамен”.

a = int(input('Введите баллы от 0 до 100: '))
if a >= 90:
  print("Отлично ваша оценка 5")
elif a >= 80:
  print("Здорово ваша оценка 4")
elif a >= 70:
  print("Хорошо ваша оценка 3")
elif a >= 60:
  print("Вам стоит подучить материал")
else:
  print("вы не сдали экзамен")




# 2. Проверить введенные пользователем данные и если длина строки больше или равна 5 символам вывести “True” иначе “False”.
a = input('enter word: ')
if len(a) >= 5:
  print(True)
else:
  print(False)


# 1. Проверить введенное пользователем число и если оно больше 5 то вывести “True”, иначе “False”.

a = int(input('enter number: '))
if a > 5:
  print(True)
else:
  print(False)

##############################################################################################################################

# 8. Дан словарь a = {'1': 1, '2': 2, '3': 3}
# Создайте новый словарь, в котором ключи и значения поменяются местами. Распечайте полученный результат.
# Hint: используйте цикл for
a = {'one': 1, 'thoo': 2, '3': 3}
b = dict([(value, key) for key, value in a.items()])
print(b)



"""# 11. Дана строка. Обменяйте местами первый и последний символы и выведите результат. Например: "Hello" -> "oellH"""
""" №1 """
# s = "Hello"
# s = s.replace("o","H")
# s = s.replace("H","o",1)
# print(s)
""" №2 """
# s = "Hello"
# s = list(s)
# s[0], s[4] = s[4], s[0]
# ''.join(s)

""" №3 """
s = "Hello"
print(s[-1]+s[1:-1]+s[0])



""" импорт встроенных функций"""
#1
#первый способ он имплортирует все функции
import math
print(math.sqrt(25))# квадратный корень = pokaz 5.0
#2
#второй импортирует отдельно
from math import sqrt,pi
print(sqrt(25))# квадратный корень = pokaz 5.0

""" Zadachi"""

#round
a = 10
b = 3
s = a / b
print(round(s,2))
print(s)



# divmod(x, y) Пара (x // y, x % y) делит на целый и делит на остоток
print(divmod(6, 2))# pokaz (3, 0)


# 3. Объявите переменные num и string. Переменной num присвойте числовое значение, а переменной string присвойте строку.
# Умножьте переменную string при помощи переменной num.
num = 2
string = "tuk"
num * string



# 6. Даны две переменные со значением типа int. Одно положительное, второе отрицательное.
# Распечатайте модуль (абсолютное значение) каждой из переменной.

n3 = 2
n4 = -3
print(abs(n3))
print(abs(n4))


# 7. Дано целое число. Возведите его в куб с помощью встроенной функции и распечатайте результат.
f = 5
pow(f,3)

# 9. Дано целое число. Возведите его в квадрат, а затем найдите остаток от деления на 5 и распечатайте результат.
# Подсказка: Для всего этого понадобиться одна функция.
# pow(x, y[, z]) x ** y % z
num1 = 10
num2 = 2
pow(num1,num2,5)

# 10. Дано десятичное число. Найдите и распечатайте его квадрат, куб, квадратный корень.
s = 5
print(s**2)
print(s**3)
import math
print(math.sqrt(s))




