# time='day'
# if time=='morning':
#     print('good morning')
# elif time=='day':
#     print('good afternoon')
# elif time == 'evening':
#     print('good evening')
# else:
#     print('hello')
# ############################################################################################33
#
# калькулятор
while True:
    n1 = float(input('введите первое число:'))
    action = input('введите действие:')
    n2 = float(input('введите второе число:'))

    if action == '+':
        ans = n1 + n2
        print(ans)

    elif action == '-':
        ans = n1 - n2
        print(ans)



    elif action == '*':
        ans = n1 * n2
        print(ans)
    elif action == '/' and n2 == 0:
        print('на ноль делить нельзя!!!')
    elif action == '/':
        ans = n1 / n2
        print(ans)
    else:
        print('Неопознанная операция')
# ############################################################################################33
#
# # пробел в клавиатуре
# # s = input()
# # l = s.split()
# # s1 = '*'.join(l)
# # print(s1)
# #№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№33№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№333№№№№№№№№№№№№№№№3
#
#
# # преобразование клавиатуры
# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#     word = input('\nвведите слово:').lower()
#
#     for i in word:
#
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         elif i in rus:
#             print(eng[rus.index(i)], end='')
#
# ########################################################################################################33
#
# # преобразование клавиатуры + пробел
#
# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
# while True:
#     word = input('\nвведите слово:').lower()
#     l = word.split()
#     s1 = '*'.join(l)
#
#     for i in word:
#
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#         elif i in rus:
#             print(eng[rus.index(i)], end='')
#         elif i in word:
#             print(' ', (s1))
# #№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
#
#                                 #счет клавиатуры глассных и согласных
# glaa = 0
# soog = 0
# while True:
#     word = input('введите слово:').lower()
#     if word == 'stop':
#         break
#     for i in word:
#         letter = i.lower()
#         if letter == "a" or letter == "e" or \
#                 letter == "i" or letter == "o" or \
#                 letter == "u" or letter == "y" or \
#                 letter == "а" or letter == "я" or \
#                 letter == "у" or letter == "ю" or \
#                 letter == "о" or letter == "е" or \
#                 letter == "ё" or letter == "э" or \
#                 letter == "и" or letter == "ы":
#             glaa += 1
#
#         else:
#             soog += 1
#
#     b = soog + glaa  # вычесление количество слов
#
#     print(f'слово: {word}\n'
#           f'согласные буквы: {soog}\n'
#           f'гласные буквы: {glaa}\n'
#           f'количество букв: {soog + glaa}\n')
#     glaa = round(glaa / len(word) * 100, 2)  # вычесление гласных букв
#
#     print("гласные/согласные:", glaa, "% /",round(100 - glaa, 2), "%")  # вычесление согласных букв
#
#
# ################################################################################################################################3
#
# #######################################################################################################################3
#
# # счет клавиатуры глассных и согласных
#
#
# glaa = 0
# soog = 0
# while True:
#     word = input('введите слово:').lower()
#     if word == 'stop':
#         break
#     for i in word:
#         letter = i.lower()
#         if letter == "a" or letter == "e" or \
#                 letter == "i" or letter == "o" or \
#                 letter == "u" or letter == "y" or \
#                 letter == "а" or letter == "я" or \
#                 letter == "у" or letter == "ю" or \
#                 letter == "о" or letter == "е" or \
#                 letter == "ё" or letter == "э" or \
#                 letter == "и" or letter == "ы":
#             glaa += 1
#
#         else:
#             soog += 1
#
#     sum_of_letter = soog + glaa  # вычесление количество слов
#     percent1 = round((glaa / sum_of_letter) * 100, 2)  # вычесление процента гласных букв
#     percent2 = round((soog / sum_of_letter) * 100, 2)  # вычесление процента согласных букв
#
#     print(f'слово: {word}\n'
#           f'согласные буквы: {soog}\n'
#           f'гласные буквы: {glaa}\n'
#           f'количество букв: {sum_of_letter}\n'
#           f'гласные/согласные: {percent1} % / {percent2} % ')
#
# #################################################################################################################
# # счет клавиатуры глассных и согласных NERO
#
# vowels ='аоыуиэеAEIOU'
# consonants ="BCDFGHJKLMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
# a = 0
# b = 0
# while True:
#     word = input('введите слово:')
#     if word == 'stop':
#         print('вы вышли из праграмы.')
#         break
#     for i in word.upper():
#         for v in vowels:
#             if i == v:
#                 a += 1
#         for c in consonants:
#             if i == c:
#                 b += 1
#     vowels_percent = round(100/len(word)*a,2)
#     consonants_percent = round(100 /len(word)*b,2)
#
#     print(f'слово: {word}\nколичество букв:{len(word)}\nгласные букв:{a}\nсогласные букв: {b}\n'
#           f'гласные / согласные:{vowels_percent}% / {consonants_percent}% ')


######################################################################################################################3

# # преобразование клавиатуры

eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = "йцукенгшщзхъфывапролджэячсмитьбю"

while True:
    word = input('\nвведите слово:').lower()

    for i in word:

        if i in eng:
            print(rus[eng.index(i)], end='')
        elif i in rus:
            print(eng[rus.index(i)], end='')
        else:
            print((' '), end='')
###########################################################################################################################
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
###########################################################################################################################

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

##########################################################################################################################