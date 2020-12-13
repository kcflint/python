# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
# порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [origin_list[i] for i in range(len(origin_list)) if origin_list.count(origin_list[i]) == 1]
print('Исходный список: ', origin_list)
print('Новый список:    ', new_list)

# С функцией count, прописанной вручную


def counter(lst, el):
    a = 0
    for m in range(len(lst)):
        if lst[m] == el:
            a += 1
    return a


new_list2 = [origin_list[n] for n in range(len(origin_list)) if counter(origin_list, origin_list[n]) == 1]
print('Новый список:    ', new_list2)
