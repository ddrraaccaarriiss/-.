# """Циклы: for, while"""
# # i - item, iterable
# # ghbdtn
# # пщщпду
# ######################################################################3333
# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#       word = input('\nвведите слово').lower()
#       for i in word:
#           if i in eng:
#               print(rus[eng.index(i)], end='')
#           else:
#               print(eng[rus.index(i)], end='')
############################################################################3

#
# rounds = 5+1
# while rounds != 0:
#     rounds -= 1
#     if rounds == 3:
#         break
#     print(f'кругов осталось: {rounds}')
####################################################################################################3
# c = 0
#
# while True:
#     print('hello', c)
#     if c == 100:
#         break
#     c += 1
#


##################################################################################################

#
# cash = 100
# years = 5
# percents = 0.05
#
# # cash += cash * percents
# counter = 1
# for year in range(years):
#     cash += cash * percents
#     print(f'год: {counter} - {cash}')
#     counter += 1

# print('python')

# amount = int(input('введите количество кругов: '))
# counter = 0
#
# for i in range(amount):
#     counter += 1
#     time = input(f'укажите время eng/rus: \nкруг: {counter}')
#     if time == 'exit':
#         print('программа завершена: ')
#         break
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('hello')


    # if temperature < 10:
    #     print('одевайся теплее')
    # else:
    #     print('оденься по легче')


# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)

# word = "programming"
#
# for letter in word:
#     if letter == 'm':
#         print('мы пропустили букву m')
#         continue
#     print(letter)

    # print(letter)
    # if letter == 'i':
    #     break

    # if letter == 'm':
    #     print(letter.title())

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# glassnye = "aeiouyаяуюоеэиы"
# soglasnye = "бвгджзйклмнпрстфхцчшщъьbcdfghjklmnpqrstvwxz"
# world = input('\nвведите слово')

##########################################################
# while True:
#      word = input('\nвведите слово').lower()
#      for i in word:
#          if i in eng:
#              print(rus[eng.index(i)], end='')
#          else:
#              print(eng[rus.index(i)], end='')
##########################################################33

# print(type(eng))
# while True:
#       word = input('\nвведите слово').lower()
# word = input('\nвведите слово').title()
# # word = "Python"
# gls = 0
# consonants = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels %i\nConsonants %i" % (vowels, consonants))
#############################################################################################################33
# while True:
# word = input('введите слово:').lower()
# glasnye = 0
# soglasnye = 0
# for i in word:
#     letter = i.lower()
#     if letter == "a" or letter == "e" or\
#        letter == "i" or letter == "o" or\
#        letter == "u" or letter == "y" or \
#        letter == "а" or letter == "я" or \
#        letter == "у" or letter == "ю" or \
#        letter == "о" or letter == "е" or \
#        letter == "ё" or letter == "э" or \
#        letter == "и" or letter == "ы":
#        glasnye += 1
#     else:
#         soglasnye += 1
#
# print(f'слово:{word}\n'
#       f'согласные буквы: {soglasnye}\n'
#       f'гласные буквы: {glasnye}\n')

#############################################################################33
