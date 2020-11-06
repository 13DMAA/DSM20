# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
list_ = [2, 'text', 456, 45.3, None, ["123", 123], ("123", 123), {"123", 123}, {"key_1": "123", "key_2": 123}]
continue_ = True
while continue_:
    user_active = input("Введите цифру нужной команды --> "
                        "\n1.Вывести стандартный список и их типы. "
                        "\n2.Добавить элемент в список.\n")
    if user_active.isdigit():
        user_active = int(user_active)
        if 0 < user_active <= 3:
            if user_active == 1:
                for el in list_:
                    print(el, "-->", type(el))
                    type_ = None
            elif user_active == 2:
                user_value = input("Введите элемент\n")
                type_ = input("Введите тип элемента str/int/float\n")
                if type_ == "int" and user_value.isdigit():
                    list_.append(int(user_value))
                elif type_ == "float" and (len(user_value.split(".")) == 2
                                           and user_value.split(".")[0].isdigit()
                                           and user_value.split(".")[1].isdigit()
                                           or user_value.isdigit()):
                    list_.append(float(user_value))
                elif type_ == "str":
                    list_.append(user_value)
                else:
                    print("Вы ввели неверный параметр, элемент не будет добавлен")
                    type_ = None
            if type_ == "int" or type_ == "float" or type_ == "str":
                for el in list_:
                    print(el, "-->", type(el))
        else:
            print("Вы ввели неверную команду")
        if input("\nПродолжим работу? Y/N\n").upper() != "Y":
            continue_ = False
    else:
        print("Вы ввели неверную команду")
        if input("\nПродолжим работу? Y/N\n").upper() != "Y":
            continue_ = False
