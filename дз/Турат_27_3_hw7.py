ten = list(range(1, 11))
evens = list(filter(lambda n: n % 2 == 0, ten))
print(evens)
print(list(map(lambda x: x**2, evens)))

def get_by_index(lst=ten):
    while True:
        try:
            ind = input('введите индекс: ')
            if ind == 'stop':
                print('вы вышли из функции')
                break
            print(lst[int(ind)])
        except ValueError:
            print('вводите только числа!')
        except IndexError:
            print(f'  введите правильный индекс от 0 до {len(lst) - 1} ')

get_by_index('python')
# get_by_index()
















