"""Структуры данных: списки, срезы, кортежи."""
# list - список (изменямый тип данных)
# tuple - кортеж

# numbers = tuple('123')
# numbers_l = list(numbers)
# print(numbers_l)
#
# # tuple1 = ()
#
# print(type(tuple1))
# print(tuple1)

# print(type(tuple1))

# weekend_days = ('saturday', 'sunday')
#
# print(weekend_days)
# print(type(weekend_days))


# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# rus = "йцукенгшщзхъфывапролджэячсмитьбю"
#
data = [
     ['fpfvfn', 'азамат'],
    ['cfvfn', 'самат'],
   ['rfybn', 'канит'],
    ['rfqhfn', 'кайрат']
 ]
#
for row in data:
    print(f'{row[0]} ==> {row[1]} <== {row[1][::-1]}')


# while True:
#     word = input('\nвведите слово').lower()
#     if word == 'q':
#         break
#
#     converted = ''
#     for i in word:
#         if i in eng:
#             print(rus[eng.index(i)], end='')
#             converted += rus[eng.index(i)]
#         else:
#             print(eng[rus.index(i)], end='')
#             converted += eng[rus.index(i)]
#     data.append([word, converted])
#
# print(data)

# numbers = list(range(1, 4))
# objects = ['bekbolot', 'temirlan', 'urmat', 'erkin']
# new = objects.copy()
#
# print(id(objects))
# print(id(new))
#
# print(objects == new)
# print(objects is new)

# new[0] = 'nargiza'

# print(objects)
# print(new)

# for i in objects:
#     if i == 'urmat':
#         print('мы нашли Урмата')
#         break
# else:
#     print('поиск завершен, ничего не найдено')

# new = [name.upper() for name in objects if len(name) > 6]
# print(objects, new, sep='\n')

# objects.sort(key=len)
# objects.reverse()
# new = objects[::-1]
# print(new)

"""изменение"""
# objects[3:6] = ['room']
# objects[-1][1] += 5

"""удаление"""
# objects.remove('python')
# deleted = objects.pop(1)
# print(deleted)
# objects.clear()
# del objects[::2]

"""добавление"""
# objects.append(100)
# objects.insert(4, ['nurlan', 'timur', 'alina'])
#

# objects += numbers


# print(objects[4:-1])
# print(type(objects))
