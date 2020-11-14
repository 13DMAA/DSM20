# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# 300 2.2 12 44 1 1 4 10 fg th 7 1 78 123 55
# Результат: [12, 44, 4, 10, 78, 123].

def check_list_int(check_list, iteration=0):
    for el in range(iteration, len(check_list)):
        el = check_list[iteration]
        try:
            i = check_list.index(el)
            check_list.remove(el)
            check_list.insert(i, int(float(el) // 1))
            if len(check_list) > iteration + 1:
                iteration += 1
        except ValueError:
            pass
    return check_list


list_ = input("Введите список чисел\n").split()
print([int(list_[i]) for i in range(1, len(check_list_int(list_))) if int(list_[i]) > int(list_[i - 1])])
