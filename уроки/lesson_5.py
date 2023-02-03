"""словари, множества."""
# dict - dictionary (словарь) изменяемый тип данных
# set - set (множество) изменяемый тип данных
# {key: value}

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


# new = set('programming')
# print(len(new))

# print(lagman.union(manty))
# print(lagman | manty)
#
# print(lagman.difference(manty))
# print(lagman - manty)
#
# print(lagman.intersection(manty))
# print(lagman & manty)
#
# print(lagman.symmetric_difference(manty))
# print(lagman ^ manty)

# numbers_l = [1, 2, 3, 2, 4, 3]
# numbers_s = {1, 2, 3, 2, 4, 3}
#
# numbers_s.add(6)
# numbers_s.remove(2)
#
# print(numbers_l)
# print(numbers_s)
# print(type(numbers_s))


# names = 'samat/azamat/erkin'
# names = names.split('/')
# print(names)

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


# sum, min, max

# numbers = [23, 45, 67, 2.8, 1.4, 1, 0.7, 89]
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))

# regions = ["чуй", "нарын", "талас", "ош", "баткен", "ыссык-куль", "джалал-абад"]
# regions_data = {}
# regions_data = {i: float(input(f'введите температуру в {i}')) for i in regions}
# print(round(sum(regions_data.values()) / len(regions_data), 2))


# new = dict([[1, 'one'], [2, 'two']])
# new = dict(name='azamat', age=21, weight=65)
#
# # print(new)
#
# student = {
#     'name': 'john',
#     'age': 20,
#     'height': 1.71,
#     'hobby': ['chess', 'golf', 'programming']
# }



# print(student['nam'])
# print(student.get('name', 'нет такого ключа'))

# for k, v in student.items():
#     print(f'{k}: {v}')

# for i in student:
#     print(f'{i} ==> {student[i]}')

# print(student.keys())
# print(student.values())
# print(student.items())

"""edit"""
# student['height'] += 0.07
# student['hobby'][1] = 'boxing'

"""delete"""
# del student['height']
# deleted = student.pop('age')
# print(deleted)
# del student['hobby'][0]

"""добавление"""
# student['married'] = True
# student['hobby'].append('drive')
# student.update(new)

# print(type(student))
