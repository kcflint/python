# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Информатика: 100(л) 50(пр) 20(лаб)
# Физика: 30(л) - 10(лаб)
# Физкультура: - 30(пр) -
# Философия: - - -
# Математика: 25(л)  -
# Химия: 30(л) 25(пр) -

# Первый способ с заменой части строки на "пустышку" для изъятия чисел
with open(file='HW_5.6_subject_list.txt', encoding='UTF-8') as file:
    new_dict = {}
    for line in file:
        total = 0
        line = line.split()
        for i in range(1, len(line)):
            if line[i] == '-':
                line[i] = 0
            else:
                line[i] = line[i].replace('(л)', '')
                line[i] = line[i].replace('(пр)', '')
                line[i] = line[i].replace('(лаб)', '')
            total += int(line[i])
        new_dict.update({line[0]: total})

print(new_dict)

# Второй способ с проверкой символов строки для изъятия чисел
with open(file='HW_5.6_subject_list.txt', encoding='UTF-8') as file:
    new_dict = {}
    for line in file:
        lst = line.split()
        total = 0
        for i in range(len(lst)):
            res = ''.join([n for n in lst[i] if n.isdigit()])
            if res == '':
                res = 0
            total += int(res)
        new_dict.update({lst[0]: total})

print(new_dict)
