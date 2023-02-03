
# from random import choice
#
# with open('materials.txt', 'r') as materials:
#     materials_list = materials.readlines()
#     with open('students.txt') as students:
#         students_list = students.readlines()
#         with open('results.txt', 'a') as results:
#             while students_list != 0:
#                 print("осталось студентов", len(students_list))
#                 random_student = choice(students_list)
#                 random_material = choice(materials_list)
#                 rate = int(input(f'отвечает:{random_student}\n'
#                                  f'тема: {random_material}\n'
#                                  f'оценка: '))
#                 results.write(f'студент: {random_student.rstrip()} '
#                               f'тема:  {random_material.split()[0]} '
#                               f'оценка: {rate}\n')
#                 students_list.remove(random_student)












"""Работа с файлами."""
# w - режим записи, перезаписи
# a - режим записи, дозаписи
# x - режим бесконфликтного записи файла
# r - режим чтения


# file = open('file.txt', 'w', encoding='UTF-8')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('file.txt', 'w', encoding='UTF-8') as file:
#     file.write('новая строка')

# with open('students.txt', 'x', encoding='UTF-8') as file:
#     file.write('новая строка')

import time

# with open('file.txt', 'r', encoding='utf-8') as file:
#     print(file.readlines()[4])
    # file.readline()
    # file.readline()
    # for i in file.readlines():
    #     time.sleep(1)
    #     print(i, end='')

a = 10
b = 3
s = a / b
print(round(s,2))
print(s)