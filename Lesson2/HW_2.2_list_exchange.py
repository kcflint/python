line = input('Введите элементы списка через пробел: ').split()
print('Исходный список', line)

for i in range(1, len(line), 2):
    line[i], line[i-1] = line[i-1], line[i]

print('Новый список   ', line)
