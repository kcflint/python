# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

f = open("HW_5.2_lines-words_number.txt")
print(f.read())
f.close()


lines_number = 0
symbols_number = 0
with open("HW_5.2_lines-words_number.txt") as file:
    for line in file:
        lines_number += 1
    symbols_number += file.tell()
    print("Количество символов:", symbols_number, 'Число строк', lines_number)
