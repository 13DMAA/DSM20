# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.
def exit_program():
    while True:
        print("-" * 50)
        request = input("Закончить работу программы? Y/N\n")
        if request.upper() == "Y":
            print("Всего хорошего!")
            return False
        elif request.upper() == "N":
            return True
        else:
            print("Ошибка ввода. Введите 'Y' или 'N'")


def check_int(str_):
    try:
        return int(str_)
    except ValueError:
        print("Ошибка ввода, нужно было ввести число")
        str_ = input("Попробуйте еще раз --> ")
        return check_int(str_)


def division(var_1, var_2):
    try:
        return f"{var_1} деленное на {var_2} равно {round(var_1 / var_2, 2)}"
    except ZeroDivisionError:
        return "Ошибка...деление на ноль даст бесконечность, а с таким значением нам будет неудобно работать\n"


continue_while = True
while continue_while:
    a = check_int(input("Введите делимое "))
    b = check_int(input("Введите делитель "))
    print(division(a, b))
    continue_while = exit_program()
