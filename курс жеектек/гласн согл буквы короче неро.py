vowels ='аоыуиэеAEIOU'
consonants ="BCDFGHJKLMNPQRSTVWXYZБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
a = 0
b = 0
while True:
    word = input('введите слово:')
    if word == 'stop':
        print('вы вышли из праграмы.')
        break
    for i in word.upper():
        for v in vowels:
            if i == v:
                a += 1
        for c in consonants:
            if i == c:
                b += 1
    vowels_percent = round(100/len(word)*a,2)
    consonants_percent = round(100 /len(word)*b,2)

    print(f'слово: {word}\nколичество букв:{len(word)}\nгласные букв:{a}\nсогласные букв: {b}\n'
          f'гласные / согласные:{vowels_percent}% / {consonants_percent}% ')


