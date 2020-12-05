line = input('Введите несколько слов через пробел: ')
user_list = line.split()
print(user_list)

for i in range(len(user_list)):
    if len(user_list[(i-1)]) > 10:
        m = user_list[(i-1)]
        user_list[(i-1)] = m[0:10]

for ind, el in enumerate(user_list, 1):
    print(ind, el)
