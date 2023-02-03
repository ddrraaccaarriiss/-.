eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = "йцукенгшщзхъфывапролджэячсмитьбю"

vowels = 0
consonants = 0

while True:
    word = input('\nВведите слово:').lower()
    for i in word:
        letter = i.lower()
        if letter == "a" or letter == "e" or \
                letter == "i" or letter == "o" or \
                letter == "u" or letter == "y" or \
                letter == "а" or letter == "я" or \
                letter == "у" or letter == "ю" or \
                letter == "о" or letter == "е" or \
                letter == "ё" or letter == "э" or \
                letter == "и" or letter == "ы":
            vowels += 1

        else:
            consonants += 1

    print(f'слово: {word}\n'
          f'Количество букв: {vowels + consonants}\n'
          f'Согласные буквы: {consonants}\n'
          f'Гласные буквы: {vowels}\n')
    vowels = round(vowels / len(word) * 100, 2)

    print("гласные/согласные:", vowels, "% /", round(100 - vowels, 2), "%")
    break