# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def input_(i):
    list_data_set = ["имя", "фамилия", "год рождения", "город проживания", "email", "телефон"]
    if 0 <= i < len(list_data_set):
        item = list_data_set[i]
        if i == 1:
            item = item[:len(item) - 1] + "ю"
        item = input(f"Введите {item} ")
    return [list_data_set[i], item]


def render_data_set(name=input_(0), surname=input_(1), birthday=input_(2),
                    city=input_(3), e_mail=input_(4), phone_number=input_(5)):
    dict_data_set = {f'{name[0]}: {name[1]}, {surname[0]}: {surname[1]}, {birthday[0]}: {birthday[1]},'
                     f' {city[0]}: {city[1]}, {e_mail[0]}: {e_mail[1]}, {phone_number[0]}: {phone_number[1]}'}
    print(dict_data_set)


render_data_set()

