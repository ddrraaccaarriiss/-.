Naryn = float(input("Температура воздуха Нарын = "))
Jalal_Abad = float(input("Температура воздуха Джалал-Абад  = "))
Bishkek = float(input("Температура воздуха Бишкек = "))
Kemin = float(input("Температура воздуха Кемин = "))
Osh = float(input("Температура воздуха Ош = "))
Sokuluk = float(input("Температура воздуха Сокулук = "))


a = round((Naryn + Jalal_Abad + Bishkek + Kemin + Osh + Sokuluk) / 6, 1)
print(f"Температура областях в КР - {a}º")
print("До встречи")