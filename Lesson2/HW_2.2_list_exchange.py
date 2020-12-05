line = input('Введите элементы списка через пробел: ')
user_list = line.split()
print('Исходный список', user_list)
new_list = []

for i in range(1, len(user_list), 2):
    a, b = user_list[(i-1)], user_list[i]
    a, b = b, a
    new_list.append(a)
    new_list.append(b)
if len(user_list) % 2 != 0:
    new_list.append(user_list[-1])

print('Новый список   ', new_list)
