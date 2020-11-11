# 4. Программа принимает действительное положительное число x и целое
# отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def check_x(x):
    if x > 0:
        return x
    else:
        print(f"Ошибка ввода --> {x}, значение заменено на 0")
        return 0


def my_func(x, y):
    x = check_x(x)
    if y > 0:
        pow_ = x
        i = y
        while i > 1:
            pow_ *= x
            i -= 1
        return f"Нужно было ввести отрицательное значение степени, но {x} в степени {y} = {pow_}"
    elif y == 0:
        return f"Нужно было ввести отрицательное значение степени , но {x} в степени {y} = 1"
    elif y < 0:
        pow_ = x
        i = y
        while i < -1:
            pow_ *= x
            i += 1
        return f"{x} в степени {y} = {round(1 / pow_, 2)}"


print(my_func(-1, 3))
print(my_func(2, 3))
print(my_func(2, -3))
