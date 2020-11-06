# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
list_tuples = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
               (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
               (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
while True:
    new_product = input("Введите команду:\n"
                        "1. Добавить новый товар\n"
                        "2. Просмотреть список товаров\n"
                        "3. Вывести аналитику по всем товарам\n")
    if new_product.isdigit():
        if int(new_product) == 1:
            name = input("Введите название товара\n")
            check = False
            while not check:
                price = input("Введите цену товара\n")
                if price.split(".") == 2 and price.split(".")[0].isdigit() and price.split(".")[1].isdigit():
                    check = True
                if price.isdigit():
                    check = True
                if not check:
                    print("Введите коректные данные")
            check = False
            while not check:
                count = input("Введите количество товара\n")
                if count.isdigit():
                    check = True
                else:
                    print("Введите коректные данные")
            unit = input("Введите единицу измерения\n")
            tuple_ = (len(list_tuples)+1, {"название": name, "цена": price, "количество": count, "eд": unit})
            list_tuples.append(tuple_)
        if int(new_product) == 2:
            for item in list_tuples:
                print(item)
        if int(new_product) == 3:
            analytics_dict = {}
            # analytics_dict.update({1: 3})
            # print("analytics_dict = ", analytics_dict)
            for item in list_tuples:
                for key, value in item[1].items():
                    # print(key, value)
                    if not analytics_dict.get(key):
                        analytics_dict.update({key: [value]})
                    else:
                        if not analytics_dict.get(key).count(value):
                            analytics_dict.get(key).append(value)
            print("Структура аналитики о товарах -->\n{")
            for key, value in analytics_dict.items():
                print(f"    {key}: {value}")
            print("}")
    else:
        print("Ошибка команды. Пожалуйста, введите цифру от 1 до 3")
