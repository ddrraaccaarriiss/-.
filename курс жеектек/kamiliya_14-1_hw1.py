try:
    osh = float(input('Введите температуру в Оше:'))
    bat = float(input('Введите температуру в Баткене:'))
    bis = float(input('Введите температуру в Чуе:'))
    tah = float(input('Введите температуру в Таласе:'))
    ysyk = float(input('Введите температуру на Ыссык-Куле:'))
    djal = float(input('Введите температуру в Джалал-Абаде:'))
    nar = float(input('Введите температуру в Нарыне:'))
    avarage = round((osh + bis + bat + tah + ysyk + djal + nar) / 7, 1)
    print(f'Средний показатель температуры воздуха по КР на сегодня {avarage} °C')
except ValueError:
    print('нет')

