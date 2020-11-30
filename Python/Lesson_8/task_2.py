# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.
class MyError_Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyError_not_num(Exception):
    def __init__(self, txt):
        self.txt = txt


def check_numbers(str_):
    for el in str_:
        if ord(el) < 45 or ord(el) > 57 or ord(el) == 47:  # 45 '-'  46 '.'  48-57 '0-9'  47 '/'
            raise MyError_not_num("Введенные значения не числа\n"
                                  "Попробуйте еще раз")


def division():
    a, b = input("Введите делимое\n"), input("Введите делитель\n")
    try:
        check_numbers(a)
        check_numbers(b)
        if int(b) == 0:
            raise MyError_Zero("Деление на нуль даст бесконечность, не очень удобное значение\n"
                               "Попробуйте еще раз")
    except MyError_Zero as err:
        print(err)
        division()
    except MyError_not_num as err:
        print(err)
        division()
    else:
        print(f"{float(a)} / {float(b)} = {round(float(a) / float(b), 2)}")


division()
