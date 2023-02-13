###888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888



"""Работа с файлами."""

# w - режим записи, перезаписи
# a - режим записи, дозаписи
# x - режим бесконфликтного записи файла
# r - режим чтения

#1
# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close()
#2
# with open('file.txt', 'a', encoding='UTF-8') as file:
#     file.write('\nновая строка')
#3
# with open('file2.txt', 'x', encoding='UTF-8') as file:
#     file.write('новая строка 2')
#4
# 4,1   rejim chtenie pokazyvaet v ran
# with open('file.txt', 'r', encoding='UTF-8') as file:
#     file.readline()# propuskaet stroku odnu
#     print(file.read())

# 4.2 # pokaz s podskazkoi i dobavlaet v spisok
# with open('file.txt', 'r', encoding='UTF-8') as file:
    # print(file.readlines())# pokaz obshyi
    # print(file.readlines()[-2:])# pokaz poslednye dve stroki
    # print(file.readlines()[:3])  # pokaz pervye dve stroki



# 4,3 Proitis po syklu for
# 4,3,1
# import time# 1 esli hotim pokaz po vremeni
# with open('file.txt', 'r', encoding='UTF-8') as file:
#     for i in file.read():
#         time.sleep(1)# odin sekund odna BUKVA
#         print(i, end='')# pokaz gorizantali
#         ## print(i)# Pokaz vertikali
# 4,3,2
# import time# 2 esli hotim pokaz po vremeni
# with open('file.txt', 'r', encoding='UTF-8') as file:
#     for i in file.readlines():
#         time.sleep(1)# odin sekund odna STROKA
#         print(i, end='')# pokaz gorizantali

# 4,4 Proverka vyvoda po indeksu

# with open('file.txt', 'r', encoding='UTF-8') as file:
#     # print(file.readlines()[2])# pokaz tretei stroki vyzov po indeksu
#     print(file.readlines()[1])# pokaz vtoroi stroki vyzov po indeksu

############ PRIMERY  ####################

# # Read data from results.txt
# with open('results.txt', 'r',encoding='UTF-8') as f:
#     data = f.readlines()
#
# # Create a dictionary with student name and surname as key and topic and grade as value
# students = {}
# for line in data:
#     name, surname, topic, grade = line.strip().split(':')
#     fullname = name + ' ' + surname
#     students[fullname] = {'topic': topic, 'grade': int(grade)}
#
# # Sort the dictionary by grade in descending order
# sorted_students = dict(sorted(students.items(), key=lambda x: x[1]['grade'], reverse=True))
#
# # Print the top 3 students with the highest grades
# for student in list(sorted_students)[:3]:
#     print('В Топ лучших:',student, sorted_students[student])
#
# # Create a new text file sorted_results.txt and write the sorted dictionary to it
# with open('sorted_results.txt', 'w',encoding='UTF-8') as f:
#     for student in sorted_students:
#         f.write(student + ':' + sorted_students[student]['topic'] + ':' + str(sorted_students[student]['grade']) + '\n')
#
# # Print the contents of sorted_results.txt
# with open('sorted_results.txt', 'r',encoding='UTF-8') as f:
#     print(f.read())




###########################################################################################################################3
"""list Камприхенж """

# def show_word(func, *iterable):
#     return [func(i) for i in iterable]
# print(show_word(len, 'oop', 'bishkek', 'kgz'))

""" с лист комприхендж """

# numbers = list(range(1, 11))
# filtered = [i for i in numbers if i < 5]
# print(filtered)
# print(type(filtered))

"""#3 list komprihej  (kopirovka) i uslovie"""

# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin','jetigen','tilek','bob']
# new = [name.upper() for name in objects if len(name) > 6]
# print(objects,new,sep='\n')

#####################################################################################################################################3
##7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

"""Urok 7 """
"""lambda, и работа с исключениями"""





""" работа с исключениями"""
# try:
#     some code
# except:
#     some code
# finally:
#     some code

# работа с ошибками типо таких
# print(34 / 0)
# print(name)
# print('123'[5])
# print(int('defg'))
# print('34' + 23)

""" работа с исключениями"""

# тут работает с 2 ошибкой
# word = 'python'
# while True:
#     try:
#         index_object = int(input('введите индекс: '))
#         print(word[index_object])
#     except ValueError:
#         print('вводите только числа!')
#     except IndexError:
#         print("введите правильный индекс")

""" работа с исключениями"""
# тут работает только с одной ошибкой
# word = 'python'
# while True:
#     try:
#         index_object = int(input('введите индекс: '))
#         print(word[index_object])
#     except :
#         print('вводите только числа')
#     finally:
#         print(" Проверка завершена")

""" Пример MAP использует функцию внутри функции здесь он преобразовал страку в число """

# numbers = ['23', '56', '67']
# numbers = list(map(float, numbers))
# print(numbers)
# print(sum(numbers))



""" пример использование  lambda внутри  sorted 
    отфильтровали словарь по ключу """

# dct = {
#     'one': 1,
#     'three': 3,
#     'seven': 7,
#     'two': 2
# }
#
# sort_dict = dict(sorted(dct.items(), key=lambda item: item[1]))
# print(sort_dict)



""" Пример MAP использует функцию внутри функции"""

# numbers = list(range(1, 11))
# print(numbers)
#
# mapped = tuple(map(lambda x: x**2, numbers))
# print(mapped)


""" пример использование фильтра и lambda"""
# #1
# ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda n: n % 2 == 0, ten))
# print(evens)
# #2
# ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda n: n > 5, ten))
# print(evens)
#3
""" Тоже самое только с лист комприхендж """

# numbers = list(range(1, 11))
# filtered = [i for i in numbers if i < 5]
# print(filtered)
# print(type(filtered))


# lambda arguments: expression

# plus = lambda number1, number2: number1 + number2
# print(plus(2,3))
# print(type(plus))
#
# def plus_def(n1, n2):
#     return n1 + n2
# print(plus_def(2,3))
# print(type(plus_def))

"""Замена лямды на  функцию"""

# def up_word(word: str):
#     return word.title()
#
#
# def show_word(func, *args):
#     return [func(i) for i in args]
#     new_list = []
#     for i in args:
#         new_list.append(func(i))
#     return new_list
#
# print(show_word(lambda word: word.title(), 'oop', 'bishkek', 'kgz'))
# print(show_word(up_word, 'oop', 'bishkek', 'kgz'))


"""Функция выивление часто встречающегося обьекта 1"""

# kortej = 2, 3, 4, 5, 3
# lst = [20,3, 5,  2, 3, 10, 4]
# print(sorted(kortej, key=kortej.count)[-1])
# print(sorted(lst, key=lst.count)[-1])
# print(sorted(lst, key=lst.count))# vstroienaya funksiya


"""Функция выивление часто встречающегося обьекта 2"""

# kortej = 2, 3, 4, 5, 3
# lst = [20,3, 5,  2, 3, 10, 4]
#
# def most_frequent(List):
#     counter = 0
#     num = List[0]
#     for i in List:
#         curr_frequency = List.count(i)
#         if (curr_frequency > counter):
#             counter = curr_frequency
#             num = i
#     return num
#
# print(most_frequent(lst))
# print(most_frequent(kortej))


""" Способы узнавать типы данных """

# kortej = 2, 3, 4, 5
# lst = [20, 5, 3, 10, 4]
# print(type(lst))
# print(type(lst) == list) # list ravno na list
# # print(isinstance(lst, list,tuple))# eto ivlaietsya listom mojno paru


""" Функция min переписали """

# lst = [20, 5, 3, 10, 4]
# def min1(iterable):
#
#     min_value = iterable[0]
#     for i in iterable:
#         if i < min_value:
#             min_value = i
#     return min_value
#
# print(min1((lst)))
# print(min(lst))

""" Функция min переписали работает на лист """

# lst = [20, 5, 3, 10, 4]
# def min1(iterable):
#     iterable.sort()
#     return  iterable[0]
#
# print(min1((lst)))
# print(min(lst))

""" Функция min переписали работает на vseh """

# kortej = 2,3,4,5
# lst = [20, 5, 3, 10, 4]
# def min1(iterable):
#     iterable = sorted(iterable)
#     return  iterable[0]
#
# print(min1((lst)))
# print(min(lst))
# print(min1((34, 56, 87, 12)))
# print(min1((kortej)))
# print(type(kortej))


"""list Камприхенж """

# def show_word(func, *iterable):
#     return [func(i) for i in iterable]
# print(show_word(len, 'oop', 'bishkek', 'kgz'))

""" Возвращает в список primery  """

# def up_word(word: str):
#     return word.title()
# def show_word(func, *iterable):
#     return [func(i) for i in iterable]
#
# print(show_word(up_word,'oop','tut','bishkek'))
# print(show_word(len, 'oop', 'bishkek', 'kgz'))

""" primery 1"""

# def up_word(word: str): # str zdes podsrazka dlya word chtoby podskazala posle tochki
#     return word.title()

# def show_word(iterable ,func):
#   for i in iterable:
#       print(func(i))

# show_word([ 'oop', 'bishkek', 'kgz'],up_word)
# show_word([ 'oop', 'bishkek', 'kgz'],len)

""" primery 2"""

# def up_word(word: str):
#     return word.title()
#
# def show_word(func, *args):
#     new_list = []
#     for i in args:
#         new_list.append(func(i))
#     return new_list
# print(show_word(up_word, 'oop', 'bishkek', 'kgz'))







###6666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666
"""Urok 6"""

"""Функция умножения"""
# def sum_numbers(numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total
# print(sum_numbers([2, 3, 4, 5]))
# def multiply(*args):
#     return sum_numbers(args)
# print(multiply(2, 3, 4, 5))
#
"""Функция калькулятор"""

# def calculator(n1, operator, n2):
#     if operator == '+':
#         return n1 + n2
#     elif operator == '-':
#         return n1 - n2
#     elif operator == '**':
#         return n1 ** n2
#     elif operator == '%':
#         return n1 % n2
#     elif operator == '/':
#         return n1 / n2
#     else:
#         print('Непонятная команда')
#
# print(calculator(2, '**' ,3))
# print(calculator(5, '+' , 9.6))
# print(calculator(20, '%' ,3))
# print(calculator(30, '/' ,2))
# print(calculator(10, '-' ,5))
# print(calculator(10, 'плюс', 5))

"""primery funksii kak dobavlat v spisok"""


# students = {
#     "азамат": 10,
#     "мирлан": 9,
#     "сабина": 7
# }
# def add_student(name, rate):
#     students[name] = rate
#     return students
# add_student('ruslan', 10)
# print(students)


#################################################33
"""Функции, аргументы: *args, **kwargs."""

"""primery  *args vozvrashaet v kortej"""
# def plus(*args):
#     print(type(args))
#
#     return sum(args)
# print(plus(1, 1, 1.6, 1, 1, 1, 1))

#######################################3####33

"""primery  **kwargs vozvrashaet v slovar"""

# def menu(**kwargs):
#     print(kwargs)
#     return kwargs
#
# menu(drink=['cola', 'tea'], eat='pizza', a=1, book='python')




##############################
"""Okruglit i posle zapitoi 2"""
# a = float(input('1'))
# b = float(input('1'))
# c = a + b
# print(round(c,2))
#############################
# print(help(len))# Opisanie funksii
# print(len.__doc__)# Tolko dokumentasya


###########################################3
"""funksiya len perepisali"""

# def len1(sequence: list) -> int:
#     """Принимает последовательность, возвращает количество элементов"""
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter
# # a ='tyrat'
# a = [1,2,3,4,]
# print(len1(a))





#######################    primery   #################
# def greet(name, surname='unknown'):  # name required positional argument
#     print('name:', name, 'surname:', surname)  # surname not required positional argument
#
#
# greet('samat', 'abdykerimov')  # samat required positional argument
# greet('alina', 'kim')
# greet(surname='abylov', name='kerim')  # keyword argument
# greet('tyrat' )

#

#######################    primery   #################
## rechenie kvadratnogo metra
#
# def get_square(width: int, length: int):
#     return width * length
#
# a = int(input('введите длину '))
# b = int(input("введите ширину "))
# square_2 = get_square(a, b)
# print(square_2)
#
#









####################################################################################################################
"""СТРОКА."""

# word = 'geektech'
# print(word[0]) # pokaz po indeksy
# print(word[3]) # pokaz po indeksy

'''  СРЕЗЫ  ''' # srezaet po indeksu
# #1 START
# word = 'geektech'
# print(word[:4])# srezaet kones

"""2 STOP"""
# word = 'geektech'
# print(word[4:])# srezaet nachalo

"""3  Oni umeut vozvrashat"""
# word = 'geektech'
# first = word[:4]# srezaet kones
# second = word[4:]# srezaet nachalo
# print(first)
# print(second)

"""3 STEP"""
# word = '123456789'
# print(word[::2])# step через срезает



#######2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
"""Логический тип данных, условные конструкции и операторы."""
# bool - boolean (логический)
# or, and, not - логические операторы
# [start:stop:step] srezy


'''операторы назначения'''
# a = 10
# # a = a + 5
# a *= 7
# print(a)

'''bool - boolean (логический)'''
# word = 'python'
# print(word.isalpha())# вопрос буквы из алфавита?
# print(word.startswith('p'))# vopros nachinaetsya s???
# print(word.endswith('n'))# vopros kachinaetsya s???

'''операторы сравнения'''
# print(2 > 3)
# print(2 < 3)
# print(2 == 3)
# print(2 != 3)
# print(2 >= 1)
# print(2 <= 3)
# print(2 < 3 or 2 == 3)
# print(2 > 1 and 2 < 3)
# print(1 < 2 < 3)
########################################################################################################################

###########   split ponimaet probelov

# names = 'samat azamat erkin'
# names = names.split()#ponimaet probelov
# names1 = 'samat/azamat/erkin'
# names1 = names1.split('/')# ili ponimaet po sleshu
# print(names)
# print(names1)



###########################################################################################################################

"""Tema     sum, min, max rabotaet so spiskom"""
#
# numbers = [23, 45, 67, 2.8, 1.4, 1, 0.7, 89]
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# print(type(numbers))

#########333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

# urok-3

   """for"""
#
# word = 'programming'
# for letter in word:
#     print(letter)

##########################################
#####################перебирать
# word = 'programming'
# for letter in word:
#     if letter == 'm':
#         print(letter.title())
#########################################
######################остановить
# word = 'programming'
# for letter in word:
#     print(letter)
#     if letter == 'i':
#         break
#########################################
#пропустить с помощью continue
# word = 'programming'
# for letter in word:
#     if letter == 'm':
#         print('мы пропустили букву m')
#         continue
#     print(letter)
###############################################

# диапазон рейнж
#
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)
###############################################
#установка счетчика

# amount = int(input('ведите количество кругов:'))
# counter = 0
# for i in range(amount):
#     counter += 1
#     time = input(f'укажите время eng/rus: \nкруг: {counter}')
#     if time == 'exit':
#         print('программа завершена')
#         break
#
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello')
##############################################

#установка счетчика с циклом for
# cash = 100
# years = 5
# percents = 0.05
# counter = 1
# for year in range(years):
#     cash += cash * percents
#     print(f' год: {counter} - {cash}')
#     counter += 1
##########################################################################################################################################################3
 """Цикл while"""

# c = 0
# while True:
#     print('hello',c)
#     if c == 100:
#         break
#     c += 1
#####################################
#  установка счетчика на while
# rounds = 5
# while rounds != 0:
#     print(f'кругов осталось: {rounds}')
#     rounds -= 1
######################################
#  установка счетчика на while пропустить
# rounds = 5+1
# while rounds != 0:
#     rounds -= 1
#     if rounds == 3:
#         continue
#     print(F'кругов осталось: {rounds}')

# rounds = 5+1
# while rounds != 0:
#     rounds -= 1
#     if rounds == 3:
#         break
#     print(F'кругов осталось: {rounds}')

##################################################
################### for внутри другого for
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
#########################################
# ###########3пример как работает while
#
# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#     word = input('\nвведите слово').lower()
#     for i in word:
#         if word == 'stop':
#             break
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         elif i in rus:
#             print(eng[rus.index(i)], end='')
#         else:
#             print((' '), end='')
###################################################
#############33while цикль будет работать пока оно True
# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#      word = input('\nвведите слово').lower()
#      for i in word:
#          if i in eng:
#              print(rus[eng.index(i)], end='')
#          else:
#              print(eng[rus.index(i)], end='')
######44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
##  urok  4
"""  Списки (это изменяемый тип данных) """

##      написание списка

# objects1 = []
# numbers2 = list()
# objects3 = list('geekteck')
# objects4 = list(range(1,11))
# objects = [25, 12, 4.7, 8.3, 'python',oop, True, False]
# print(objects1, numbers2,objects3,objects,objects4, sep='\n')
# print(type(objects))
#print(objects[4:-1]) # обращение по индексу

##############################
#         добавление

# objects = [25, 12, 4.7, 8.3, 'python','oor', True, False]

# #1  добавление
# objects.append(100) #добавляет в конец списка и только один обьект

# #2  добавление
# objects.insert(4,'nurlan') #если в начало или конец то инсерт надо индекс а потом обьект только один обьект

# #3  добавление
# objects.insert(4,['timur',11, True])# если надо вставить несколько обьектов то список внутри другого списка

# #4  добавление
# numbers = list(range(1,4))
# numbers1 = [10,20,30,'okay']
# numbers2 = 40,50,60
# objects.append(numbers)# можно добавить другие числа переменных

#5  добавление

# objects = [25, 12, 4.7, 8.3, 'python','oor', True, False]
# numbers = list(range(1,4))
# objects.extend(numbers)#можно разширить на конец списка

#6  добавление

# objects = [25, 12, 4.7, 8.3, 'python','oor', True, False]
# numbers = list(range(1,4))
# numbers1 = 11,22,33
# objects += numbers # также можно и так  разширить на конец списка
# print(objects)

####                 УДАЛЕНИЕ                    №№№№№№№№№№№№№№№№№№№№

# objects = [25, 12, 4.7, 8.3, 'python','oor', True, False]

##  1 udalenie
# objects.remove('python')# nado priamo propisat etot obiekt
# objects.remove(8.3)# nado priamo propisat etot obiekt
# print(objects)

##  2 udalenie
# objects.pop(1) # eto uje po indeksu nado ukazat indeks

##  3 udalenie
# deleted = objects.pop(1) # pop ehse mojet vernut udalennoe obratno
# print(objects)
# print(deleted)
#
# ##  4 udalenie

# objects = [25, 12, 4.7, 8.3, 'python','oor', True, False]
##del objects[4:6]# 1 srezaet  neskolko obektov
#del objects[::2]# 2 cherez odin srezaet  neskolko obektov
#print(objects)


# ##  5 udalenie
# objects = [25, 12, 4.7, 8.3, 'python','oor', True, False]
# objects.clear()# udalaet vse chisto
# print(objects)

##############   ИЗМЕНЕНИЕ   №№№№№№№№№№№№№№№
# objects = [25, 12, 4.7, 8.3, 'python', 'oor', True, False]
# 1 izmenenie
# objects[3] = 10  # pishem indeks i izmenaem
# objects[3] = 'turat' # pishem indeks i izmenaem
# objects[3:6] = 'room' # izmenim neskolko obektov
# objects[1:3] = ['room'] # izmenim neskolko obektov uje so skopkami razshirenie
# print(objects)

## 2 izmenenie spisok vnutri spiska
# numbers = list(range(1,4))
# objects = [25, 12, 4.7, 8.3, 'python', 'oor', True, False, numbers]
# # objects[-1][1] = 7
# objects[-1][1] += 5
# print(objects)

##### Sortirovka dlya etogo oni doljny byt odnogo tipa  ############33

# objects = [25, 12, 4.7, 8.3,]
##1
# objects.sort() # Sortirovka ot malenkogo k bolshomu
##2
# objects.sort(reverse=True) # # Sortirovka ot bolshogo k malenkomu
##3
# objects.reverse() # kak oni stoiat tolko v obratnuiu storonu
##4
# new = objects[::-1]# vozvrashaet v obratnuiu storonu
# print(new)


#3###########3 sortirovka str #########33


# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin','jetigen','tilek','bob']
#1
# objects.sort()#  sortirovka po alfavitu
#2
# objects.sort(key=len)#  sortirovka po kolichestvu bukv

"""#3 list komprihej  (kopirovka) i uslovie"""

# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin','jetigen','tilek','bob']
# new = [name.upper() for name in objects if len(name) > 6]
# print(objects,new,sep='\n')

#3#########  sykl for po spisku  ###########
#1
# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin', 'jetigen', 'tilek', 'bob']
# for i in objects:
#     print(i)
# else:
#     print('poisk zavershen nichego ne naideno')


#2
# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin', 'jetigen', 'tilek', 'bob']
#
# for i in objects:
#     if i == 'urmat':
#         print('my nashli imya')
#         break
# else:
#     print('poisk zavershen nichego ne naideno')

#############  kopirovanie  ###########
##1
# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin', 'jetigen', 'tilek', 'bob']
# new = objects.copy() ## kopirovanie
# # new[0] = 'nargiza'
# print(objects)
# print(new)
# print(objects == new)
# print(objects is new)
# print(id(objects))
# print(id(new))
#2
# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin', 'jetigen', 'tilek', 'bob']
# new = objects  # ssylka na list
# new[0] = 'nargiza'
# # print(objects)
# # print(new)
#
# print(objects == new)
# print(objects is new)
# print(id(objects))
# print(id(new))
### primery

# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
# data = []
# while True:
#     word = input('\nвведите слово:').lower()
#     if word == 'r':
#         break
#     data.append(word)
#
#     for i in word:
#
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         elif i in rus:
#             print(eng[rus.index(i)], end='')
# print(data)

###############################################################################################################################

"""  КОРТЕЖЫ tuple ne izmenaemyi     """

# weekend_days = 'saturday', 'sunday'  # kortej esli est zapitaya
# weekend_days = ('saturday', 'sunday') # luche pisat s kruglymi skopkami
# tuple1 = () #pustoi kortej
# tuple1 = (23,) # obizatelno nujen zajpitaya
# print(tuple1)
# print(type(tuple1))
#
# numbers = tuple('123') #mojno prevratit v kortej
# numbers = list(numbers)# mojno privratit v spisok
# print(numbers)# skopki kruglye to kortej
# print(type(numbers))
#
#
########55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
## urok 5
"""  СЛОВАРЬ     dict     """

# {key : value} dict - dictionary  kluch ne izmenaemyi a znachenie menaietsya
# student = {}# pustoi slovar
# new = dict() # novyi slovar
# new = dict([[1, 'one'], [2, 'two']])# mojno takie danyie privratit v slovar
# new = dict(name='azamat',age = 21)# mojno i tak tipo kak peremennyie
# student = {
#     'name': 'john',
#     'age': 20,
#     'height': 1.71,
#     'hobby': ['chess', 'golf', 'programming'],
#     123: 0,
#     3.6: 45,
#
# }
# print(new)
# print(student)
# print(student['name'])# pokaz po kluchu
# print(type(student))

############### DOBAVLENIE ###########
# #1
# student = {
#     'name': 'john',
#     'age': 20,
#     'height': 1.71,
#     'hobby': ['chess', 'golf', 'programming'],
#     123: 0,
#     3.6: 45,
#
# }

#1
# student["married"] = True
#
# print(student)
#2
# student['hobby'].append('drive') # mojno dobavit ewe znacheni
# print(student)
#3
# # new = dict([[1, 'one'], [2, 'two']])# mojno dobavit ewe slovar
# new = dict(name='azamat',age = 21, wess= 65)# mojno dobavit ewe slovar esli kluch pohoj to obnovlaetsya
# student.update(new)# mojno dobavit ewe slovar
# print(student)

#4
# student['hobby'].insert(0, 'IOS')
# print(student)

##################333   UDALENIE  ################
# student = {
#     'name': 'john',
#     'age': 20,
#     'height': 1.71,
#     'hobby': ['chess', 'golf', 'programming'],
#     123: 0,
#     3.6: 45,
#  }
# #1
# # student.pop('age')# udalenie po kluchu
# #2
# deleted = student.pop('age')# pop vozvrashaet udalennye
# print(student)
# print(deleted)
# #3
# del student['height']# toje udalaet po kluchu
##4
# del student['hobby'][0]# udalayet ot kluchu cherez index
# print(student)
# print(student)
##############3  IZMENENIE  , edit  ###########33
# student = {
#     'name': 'john',
#     'age': 20,
#     'height': 1.71,
#     'hobby': ['chess', 'golf', 'programming'],
#     123: 0,
#     3.6: 45,
#
# }

##1
# student['height'] = 1.8 # izmenayet po kluchu
##2
# student['height'] += 0.07##dobovlaiet  na kluch
##3
# student['hobby'][1] = 'boxing'# izmenayet ot kluchu cherez index
# print(student)



##4 pokaz  ################3


# print(student)#1 obychnyi
# print(student.keys())#2 tolko kluchi
# print(student.values())#3 tolko znachenie
# print(student.items())#4 po param razdelaet
# for i in student:
#     print(f'{i} ==> {student[i]}')#5 otdelno po param rezdelaet

# for k,v  in student.items():
#      print(f'{k} ==> {v}')#6 otdelno po param rezdelaet toje

# print(student['name'])#7 pokaz otdelno
# print(student.get('nam', 'net takogo klucha'))#8 bezopasnyi sposob vytyagivanie iz slovarya

""" Сортировка пример использование  lambda внутри  sorted 
    отфильтровали словарь по ключу """

# dct = {
#     'one': 1,
#     'three': 3,
#     'seven': 7,
#     'two': 2
# }
#
# sort_dict = dict(sorted(dct.items(), key=lambda item: item[1]))
# print(sort_dict)




####           primer 1

# regions = ["чуй", "нарын", "талас", "ош", "баткен", "ыссык-куль", "джалал-абад"]
# regions_data = {}
# regions_data = {i: float(input(f'введите температуру в {i}')) for i in regions}
# print(round(sum(regions_data.values()) / len(regions_data), 2))

####          primer 2


#
# data = {
#     'cola': 40,
#     'snickers': 70,
#     'lays': 65
# }
#
# result = {}
# sum_bill = 0
#
# for name, price in data.items():
#     amount = int(input(f'укажите количество {name} ({price}): '))
#     result[name] = f'{price} x {amount} = {price * amount}'
#     sum_bill += int(result[name].split()[-1])
#
# print(result)
# print("итого:", sum_bill)


###############################################################################################################################33

"""Mnojestva  = set  {}  udalaet pohojie obiekty - izmenaiemyi tip dannyh i ne indexiruetsya"""

#
# numbers_a = [1,2,3,4,3,'okay','okay',True,True]# list (spisok)
# numbers_s = {1,2,3,4,3,'okay','okay',}# set (mnojestva) True on ne pokazyvaet
#
#
# print(numbers_a)
# print(numbers_s)
# print(type(numbers_a))
# print(type(numbers_s))

# new = set('programming')# privrawenie v set
# print(new)
# print(len(new))
# print(type(new))

#####  DOBAVLENIE
#1
# numbers = {1,2,3,4,3}
# numbers.add(6)
# print(numbers)


#####  UDALENIE
#1
# numbers.remove(6)
# print(numbers)
######################################  metody sravnenie s set
# lagman = {'мясо', 'лапша',  'перец'}
# manty = {'тесто',  'мясо',  'лук'}
#
# print(lagman.union(manty))# obedenaet tolko ne pohojyh
# print(lagman | manty)# obedenaet tolko ne pohojyh
# #
# print(lagman.difference(manty))# chto est u lagmana chto est u manty
# print(lagman - manty)# chto est u lagmana chto est u manty
#
# print(lagman.intersection(manty))# ih peresechenie
# print(lagman & manty)# ih peresechenie
# #
# print(lagman.symmetric_difference(manty))# ubiraet to chto ih obedinaet
# print(lagman ^ manty)# ubiraet to chto ih obedinaet

##################  PRIMERY ####
# menu = {
#     'lagman': {'мясо', "лапша", "перец"},
#     'manty': {"тесто", "мясо", "лук"},
#     'rolls': {"рис", "нори", "рыба"},
#     "греческий": {"фитакса", "оливки", "помидоры"}
# }
# print(type(menu))
#

# while True:
#     command = input('выберите команду: \n1) поиск по имени'
#                     '\n2) поиск по ингридиенту'
#                     '\n3) выход')
#     if command == '2':
#         user = input('введите ингридиент блюда! ')
#         for name, ingrs in menu.items():
#             if user in ingrs:
#                 print(name)
#     elif command == '1':
#         user = input('введите название блюда! ')
#         if user in menu:
#             print(menu[user])
#         else:
#             print(f'блюда "{user}" нет!\n'
#                   f'возможно вас заинтересует:\n\t'
#                   f'{tuple(menu.keys())}')
#     elif command == '0':
#         break
#     else:
#         print('нет такой команды')










