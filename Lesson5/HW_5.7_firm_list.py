# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать .
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
# Подсказка: использовать менеджер контекста.
# firm_1 ООО 10000 5000
# firm_2 ЗАО 20000 30000
# firm_3 ОАО 30000 12000

import json

with open('HW_5.7_firm_list.txt') as f:
    profit_dict = {}
    total_profit = 0
    number = 0
    for line in f:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        profit_dict.update({line[0]: profit})
        if profit > 0:
            total_profit += profit
            number += 1
    mean_profit = total_profit / number
    mean_profit_dict = {"mean_profit": mean_profit}
abs_list = [profit_dict, mean_profit_dict]
print(abs_list)

with open("HW_5.7_firm_list.json", "w") as f2:
    json.dump(abs_list, f2)
