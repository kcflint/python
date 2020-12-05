my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    new_el = int(input('Введите натуральное число: '))
    my_list.append(new_el)
    print(sorted(my_list, reverse=True))
