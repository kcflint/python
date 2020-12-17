# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open("HW_5.4.1_list.txt", "rt") as file1:
    with open("HW_5.4.2_new_list.txt", 'w') as file2:
        for line in file1:
            line = line.replace('One', 'Один')
            line = line.replace('Two', 'Два')
            line = line.replace('Three', 'Три')
            line = line.replace('Four', 'Четыре')
            file2.writelines(line)
