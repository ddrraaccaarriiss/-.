data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters, numbers = [], []

for i in data_tuple:
      letters.append(i) if type(i) == str else numbers.append(i)

letters = [str(i) for i in letters[::-1]]
letters[0], letters[1], letters[3], letters[4], letters[5], letters[6],letters[7] = 'G', 'e', 'k', 'T', 'e', 'c', 'h'

del numbers[0]
letters.append(numbers.pop(0))

numbers.insert(1, 2)
numbers = [int(i) for i in numbers[::-1]]
numbers = [int(i) ** 2 for i in numbers]

letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
