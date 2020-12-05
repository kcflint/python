line = input('Введите несколько слов через пробел: ')
user_list = line.split()
print(user_list)

for ind, el in enumerate(user_list, 1):
    print(ind, el[:10])
