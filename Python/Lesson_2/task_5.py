# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
# набор натуральных чисел. У пользователя необходимо запрашивать
# новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

list_ = []
while True:
    new_el = input("Введите новый элемент рейтинга, целое число\n")
    insert_ = False
    if new_el.isdigit():
        new_el = int(new_el)
        if len(list_):
            i = len(list_) - 1
            while i >= 0:
                if new_el <= list_[i]:
                    list_.insert(i + 1, new_el)
                    insert_ = True
                    i = 0
                i -= 1
            while not insert_ and i < len(list_):
                i = 0
                if new_el > list_[i]:
                    list_.insert(i, new_el)
                    insert_ = True
                else:
                    i += 1
        else:
            list_.append(new_el)
        print(list_)
    else:
        print("Попробуйте еще раз, нужно ввести целое число")
