# Переменные регионов
region1 = float(input("Бишкек:"))
region2 = float(input("Ош:"))
region3 = float(input("Баткен:"))
region4 = float(input("Иссык-Куль:"))
region5 = float(input("Нарын:"))

# Переменная вычисляющая среднюю температуру в регионах с округлением

average_regions = round((region1 + region2 + region3 + region4 + region5 ) / 5,1)

# Выводим температуру на экран

print(f'Средний показатель температуры воздуха по КР на сегодня {average_regions}°C')