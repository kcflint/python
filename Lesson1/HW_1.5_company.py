earnings = int(input('Введите значение выручки в долларах: '))
expenses = int(input('Введите значение издержек в долларах: '))
balance = earnings - expenses
profit = balance * 100 / earnings

if expenses > earnings:
    print(f'Фирма работает в убыток. Баланс {balance} доллар(а/ов)')
elif expenses == earnings:
    print(f'Фирма работает в ноль. Баланс {balance} доллар(а/ов)')
elif expenses < earnings:
    print(f'Фирма в прибыли. Баланс {balance} доллар(а/ов).')
    print(f'Рентабельность выручки = {profit:.0f}%')
    workers = int(input('Введите число сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника в долларах: {(balance / workers):.2f}')
