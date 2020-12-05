month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

dict_month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dict_season = {1: 'Winter', 2: 'Winter', 12: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
               6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}
print('Через словари:')
print(month, dict_month[month], dict_season[month])

list_month = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
list_season = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer',
               'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
print('Через списки:')
print(month, list_month[month-1], list_season[month-1])
