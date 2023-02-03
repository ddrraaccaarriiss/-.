eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = "йцукенгшщзхъфывапролджэячсмитьбю"

while True:
    word = input('\nвведите слово:').lower()

    for i in word:

        if i in eng:
            print(rus[eng.index(i)], end='')
        elif i in rus:
            print(eng[rus.index(i)], end='')
        else:
            print((' '), end='')
