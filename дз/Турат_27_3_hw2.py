
data = '1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31'
mesyas ='1,2,3,4,5,6,7,8,9,10,11,12'


data = int(input("Введите день рождения: "))
mesyas = int(input("Введите месяц рождения: "))



a1 = 'vash znak zadiaka OVEN'
a2 = 'vash znak zadiaka TELES'
a3 = 'vash znak zadiaka BLIZNESY'
a4 = 'vash znak zadiaka RAK'
a5 = 'vash znak zadiaka LEV'
a6 = 'vash znak zadiaka DEVA'
a7 = 'vash znak zadiaka VESY'
a8 = 'vash znak zadiaka SKORPION'
a9 = 'vash znak zadiaka STRELES'
a10 = 'vash znak zadiaka KOZEROG'
a11 = 'vash znak zadiaka VODOLEI'
a12 = 'vash znak zadiaka RYBY'


if (data>=21 and data<=31 and mesyas==3)\
        or(data>=1 and data<=19 and mesyas==4):

   print(a1)

elif (data>=20 and data<=30 and mesyas==4) \
        or( mesyas==5 and data>=1 and data<=20):

   print(a2)

elif (data>=21 and data<=31 and mesyas==5) \
        or( mesyas==6 and data>=1 and data<=21):

   print(a3)

elif (data>=22 and data<=30 and mesyas==6) \
        or( mesyas==7 and data>=1 and data<=22):

   print(a4)

elif (data>=23 and data<=31 and mesyas==7) \
        or( mesyas==8 and data>=1 and data<=22):

   print(a5)

elif (data>=23 and data<=31 and mesyas==8) \
        or( mesyas==9 and data>=1 and data<=22):

   print(a6)

elif (data>=23 and data<=30 and mesyas==9) \
        or( mesyas==10 and data>=1 and data<=23):

   print(a7)

elif (data>=24 and data<=31 and mesyas==10) \
        or( mesyas==11 and data>=1 and data<=22):

   print(a8)

elif (data>=23 and data<=30 and mesyas==11) \
        or( mesyas==12 and data>=1 and data<=21):

   print(a9)

elif (data>=22 and data<=31 and mesyas==12) \
        or( mesyas==1 and data>=1 and data<=20):

   print(a10)

elif (data>=21 and data<=31 and mesyas==1) \
        or( mesyas==2 and data>=1 and data<=18):

   print(a11)

elif (data>=19 and data<=29 and mesyas==2) \
        or( mesyas==3 and data>=1 and data<=20):

   print(a12)
else:
     print('вы ввели неправильные цифры')



