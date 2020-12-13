# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours_of_work, hours_payment, bonus = argv


def salary(hours, payment, extra):
    return int(hours)*int(payment) + int(extra)


print('Имя скрипта: ', script_name)
print('Выработка в часах: ', hours_of_work)
print('Ставка в часах: ', hours_payment)
print('Премия: ', bonus)
print('Размер заработной платы сотрудника: ', salary(hours_of_work, hours_payment, bonus))
