# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

user_word = input('Введите слова латинскими буквами через пробел ')
# Первый способ


def int_func1(arg1):
    word = list(arg1)
    letter = word[0].upper()
    word[0] = letter
    return ''.join(word)


user_word1 = user_word.split()
user_line1 = ''
for i in range(len(user_word1)):
    user_line1 += (int_func1(user_word1[i]) + " ")
print('Первый способ:', user_line1)

# Второй способ


def int_func(arg1):
    return arg1.title()


print('Второй способ:', int_func(user_word))

# Третий способ


def int_func3(arg3):
    arg3 = arg3.capitalize()
    return arg3


user_word3 = user_word.split()
user_line3 = ''
for i in range(len(user_word3)):
    user_line3 += (int_func3(user_word3[i]) + " ")
print('Третий способ:', user_line3)
