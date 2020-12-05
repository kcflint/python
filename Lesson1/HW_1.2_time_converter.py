time = int(input('Введите время в сеундах: '))
print(f'Вы ввели {time} секунд(у/ы)')

hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

print(f'{time} секунд [{hours:02d}]:[{minutes:02d}]:[{seconds:02d}]')