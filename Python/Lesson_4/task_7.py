# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить
# только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
from itertools import islice, count


def fact(n):
    if n:
        for el_fact in range(1, n+1):
            result = 1
            for el_count in islice(count(1), el_fact):
                result *= el_count
            yield el_fact, result
    else:
        yield 0, 0


for el, res_el in fact(10):
    print(f"{el}! = {res_el}")
