name = 'уважаемый читатель'

chyi = float(input('укажите температуру воздуха чуя: '))
yssykkol = float(input('укажите температуру воздуха ыссыккуля: '))
naryn = float(input('укажите температуру воздуха нарына: '))
talas = float(input('укажите температуру воздуха таласа: '))
batken = float(input('укажите температуру воздуха баткена: '))
osh = float(input('укажите температуру воздуха оша: '))
jalal_abad = float(input('укажите температуру воздуха жалал-абада: '))
the_sum_of_the_air_temperature_in_the_regions = (chyi + yssykkol + naryn + talas + batken + osh + jalal_abad)  # сумма
regions_amount = 7
average_air_temperature_in_KG = round(the_sum_of_the_air_temperature_in_the_regions / regions_amount, 1)  # деление
print(f'привет {name} ')  # показ имя
print(f'сумма температуры воздуха в областях: {the_sum_of_the_air_temperature_in_the_regions}\n'  # показ суммы
      f'количество областей: {regions_amount}\n'
      f'средний показатель температуры воздуха по КР на сегодня: {average_air_temperature_in_KG}°C ')  # показ результата
