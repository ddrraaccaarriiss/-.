glas = 'aeiouyаяуюоеёэиы'
while True:
    glasnye = 0
    soglasnye = 0
    word = input('введите слово:').lower()
    if word == 'stop':
        print('вы вышли из цикла.'.upper())
        break
    for i in word:
        letter = i.lower()
        if letter in glas:

            glasnye += 1
        else:
            soglasnye += 1


    sum_of_letter = soglasnye + glasnye  # вычесление количество слов
    percent1 = round((glasnye / sum_of_letter) * 100, 2)  # вычесление процента гласных букв
    percent2 = round((soglasnye / sum_of_letter) * 100, 2)  # вычесление процента согласных букв
    print(f'слово: {word}\n'
          f'количество букв: {len(word)}\n'
          f'согласные буквы: {soglasnye}\n'
          f'гласные буквы: {glasnye}\n'
          f'гласные/согласные: {percent1} % / {percent2} % ')
