# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('HW_5.5_sum.txt', "w") as file:
    numbers = input('Введите числа через пробел: ')
    file.write(numbers + "\n")
    numbers = numbers.split()
    total = 0
    for i in range(len(numbers)):
        total += int(numbers[i])
    print(total)
    file.write('Сумма введеных чисел: ')
    file.write(str(total))
