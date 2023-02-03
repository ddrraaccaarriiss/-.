"""lambda, и работа с исключениями"""
# lambda arguments: expression
# try:
#     some code
# except:
#     some code
# finally:
#     some code


### доп задание
# students = ('sultan', 'eric', 'akmal', 'said')
# c = 0
# data = {}
# while len(data) != students:
#     rate = int(input(f'поставьте оценку для {students[c]}'))
#     c += 1
#     data[students[c]] = rate
# print(data)



# word = 'python'
# while True:
#     try:
#         index_object = int(input('введите индекс: '))
#         print(word[index_object])
#     except ValueError:
#         print('вводите только числа!')
#     except IndexError:
#         print("введите правильный индекс")


# map, filter
# print(34 / 0)
# print(name)
# print('123'[5])
# print(int('defg'))
# print('34' + 23)




# numbers = ['23', '56', '67']
# numbers = list(map(float, numbers))
# print(sum(numbers))

# dct = {
#     'one': 1,
#     'three': 3,
#     'seven': 7,
#     'two': 2
# }
#
# sort_dict = dict(sorted(dct.items(), key=lambda item: item[0]))
# print(sort_dict)

# print(dict(sorted(dct, key=lambda a: sorted(a))))


# numbers = list(range(1, 11))
# print(numbers)

# mapped = tuple(map(lambda x: x**2, numbers))
# print(mapped)

# filtered = [i for i in numbers if i < 5]
# filtered = list(filter(lambda n: n % 2 == 0, numbers))
# print(filtered)


# plus = lambda number1, number2: number1 + number2
#
# def plus_def(n1, n2):
#     return n1 + n2
#
# print(type(plus))
# print(type(plus_def))


# print(plus(2, 3))
# print(plus_def(2, 3))

# min, max
# lst = [23, 44,  44, 1, 5, 3, 23, 44, 23]
# a = sorted(lst, key=lst.count)
# print(sorted(lst, key=lst.count))
# print(list(set(a))[-2:])

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


# print(sorted(lst, key=lst.count))

# lst = [20, 5, 3, 10, 4]

# def min1(iterable):
    # iterable.sort()
    # iterable = sorted(iterable)
    # print(isinstance(iterable, list, tuple))
    # print(type(iterable) == list)
    # return iterable[0]
    # min_value = iterable[0]
    # for i in iterable:
    #     if i < min_value:
    #         min_value = i
    # return min_value

# print(min1((34, 56, 87, 12)))
# print(min(lst))


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
