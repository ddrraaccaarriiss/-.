"""Функции, аргументы: *args, **kwargs."""
# DRY - don't repeat yourself
# print(sum([1, 2, 3, 4]))

# def is_mirror(string):

# word = 'довод'
# rev = word[::-1]

# def calculator(n1, operator, n2):

# students = {
#     "азамат": 10,
#     "мирлан": 9,
#     "сабина": 7
# }
#
#
# def add_student(name, rate):
#     students[name] = rate
#     return students
#
#
# add_student('ruslan', 10)
#
# print(students)


# def menu(**kwargs):
#     print(kwargs)
#     return kwargs
#
# menu(drink=['cola', 'tea'], eat='pizza', a=1, book='python')

# def plus(a, *args, b=0):
#     # print(type(args))
#     print(a, b, args)
#     return sum(args) + a
#
#
# print(plus(2, 5, 4.6, 6, 9, 11, 23))



# def len1(sequence: list) -> int:
#     """Принимает последовательность, возвращает количество элементов"""
#     counter = 0
#     for _ in sequence:
#         counter += 1
#     return counter
#
# print(len1.__doc__)
# print(help(len1))

# print(len('python'))
# print(len('python') + len1([2, 4, 5, 6]))

# print(help(len))
# print(len.__doc__)


# def greet(name, surname='unknown'):  # name required positional argument
#     print('name:', name, 'surname:', surname)  # surname not required positional argument
#
#
# greet('samat', 'abdykerimov')  # samat required positional argument
# greet('alina', 'kim')
# greet(surname='abylov', name='kerim')  # keyword argument

# def get_square(width: int, length: int):
#     return width * length
#
# a = int(input('введите длину '))
# b = int(input("введите ширину "))
# square_2 = get_square(a, b)
# print(square_2)



# square_hall = get_square(width=8, length=15)
# print(square_2, square_hall, sep='\n')


# width = 5
# length = 7
# square_2 = width * length
# print(square_2)
#
# width = 8
# length = 15
# square_hall = width * length
# print(square_hall)





