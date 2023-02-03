"""Логический тип данных, условные конструкции и операторы."""
# bool - boolean (логический)
# or, and, not - логические операторы
# [start:stop:step]

# word = '123456789'
# print(word[::4])


'''операторы назначения'''
# a = 10
# # a = a + 5
# a *= 7
# print(a)


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

# print('s' in 'python')

# nicknames = 'aaa'
# password = '123'
#
#
# input_nickname = input('укажите логин: ').lower()
# if input_nickname in nicknames:
#     input_password = input('введите пароль: ')
#     if input_password == password:
#         input_password2 = input('подтвердите пароль: ')
#         if input_password == input_password2:
#             print(
#                 f'Дорогой {input_nickname} вы успешно вошли в приложение!'
#             )
#         print('пароль не совпадают!')
#     else:
#         print('пароль неверный!')
# else:
#     print(
#         f" \"{input_nickname}\" не существует! "
#     )



# size = '40-46'
# start = int(size[:2])
# stop = int(size[3:])
# all_sizes = stop - start
# print(start, stop)
# print(all_sizes)

# word = 'geektech'
# first = word[:4]
# second = word[4:]
# print(first, second)
# print(word[0])
# print(word[3])

# print(not True)
# print(word.isalpha())
# print(word.isnumeric())
# print(not word.isalpha())

# time = 'утро'
# temperature = 25
#
#
# if time == 'morning' or time == 'утро':
#     print('good morning')
#     if temperature < 10:
#         print('одевайся теплее')
#     else:
#         print('оденься по легче')
# elif time == 'day' or time == 'день':
#     print('good afternoon')
# elif time == 'evening' or time == 'вечер':
#     print('good evening')
# else:
#     print('hello')
