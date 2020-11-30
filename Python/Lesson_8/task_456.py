from random import random


class Warehouse:
    def __init__(self, name):
        self.name = name
        self.divisions = {self.name: [], 'Некрасова': [], 'Раковская': [], 'Пушкина': [], 'Оптовый склад': []}

    def append_division(self, name):
        """Добавить подразделение/склад/магазин"""
        self.divisions.update({name: []})

    def set_division(self, name_division):
        """Выбрать склад по названию"""
        return self.divisions.setdefault(name_division)

    def append_tmc(self, name_division, tmc={}, quantity=1, product_id=0):
        """Добавить ТМЦ на склад"""
        if product_id:
            count_tmc = self.check_id_in_div(name_division, product_id)
            if count_tmc:
                product = self.divisions.setdefault(name_division)[count_tmc - 1]
                product.update({'count_': product.setdefault('count_') + quantity})
                print(f"ТМЦ c ID {product_id} в количестве {quantity} успешно добавлен на склад {name_division}")
            else:
                self.divisions.setdefault(name_division).append(tmc)
                print(f"ТМЦ c ID {product_id} в количестве {quantity} успешно добавлен на склад {name_division}")
        else:
            count_tmc = self.check_tmc_in_div(name_division, tmc)
            if count_tmc:
                product = self.divisions.setdefault(name_division)[count_tmc - 1]
                product.update({'count_': product.setdefault('count_') + quantity})
                print(
                    f"ТМЦ c ID {product.setdefault('id_')} в количестве {quantity} успешно добавлен на склад {name_division}")
            else:
                self.divisions.setdefault(name_division).append(tmc.__dict__)
                count_tmc = self.check_tmc_in_div(name_division, tmc)
                product = self.divisions.setdefault(name_division)[count_tmc - 1]
                product.update({'count_': quantity})
                print(
                    f"ТМЦ c ID {product.setdefault('id_')} в количестве {quantity} успешно добавлен на склад {name_division}")

    def del_tmc(self, name_division, product_id, quantity):
        """Удалить ТМЦ со склада"""
        count_tmc = self.check_id_in_div(name_division, product_id)
        if count_tmc:
            product = self.divisions.setdefault(name_division)[count_tmc - 1]
            if product.setdefault('count_') - quantity > 0:
                product.update({'count_': product.setdefault('count_') - quantity})
                print(f"ТМЦ c ID {product_id} в количестве {quantity} успешно удален со склада {name_division}")
                product_return = product.copy()
                print(type(product_return))
                product_return.update({'count_': quantity})
                return True, product_return
            elif product.setdefault('count_') - quantity < 0:
                print(f"Количества ТМЦ c ID {product_id} на складе {name_division} меньше {quantity}")
                return False, {}
            else:
                self.divisions.setdefault(name_division).pop(count_tmc - 1)
                print(f"ТМЦ c ID {product_id} в количестве {quantity} успешно удален со склада {name_division}")
                return True, product
        else:
            print(f"Количества ТМЦ c ID {product_id} недостаточно на складе {name_division}")

    def show_division(self, name_division):
        """Показать что есть на складе"""
        if len(self.divisions.setdefault(name_division)):
            print(f"Склад {name_division} содержит: ")
            for i, item in enumerate(self.divisions.setdefault(name_division), 1):
                print(f"{i}. {item}")
        else:
            print(f"Склад {name_division} пуст.")

    def check_tmc_in_div(self, name_division, tmc):
        """Проверить наличие ТМЦ на складе"""
        division = self.set_division(name_division)
        count_product = 0
        for product in division:
            count_product += 1
            count_for = 1
            for k, v in product.items():
                count_for += 1
                if k != 'id_' and k != 'count_':
                    if v == tmc.__dict__.setdefault(k):
                        pass
                    else:
                        break
                if count_for == len(product.items()):
                    return count_product
        return False

    def check_id_in_div(self, name_division, product_id):
        """Проверить наличие ТМЦ на складе по ID"""
        division = self.set_division(name_division)
        count_product = 0
        for product in division:
            count_product += 1
            for k, v in product.items():
                if k == 'id_':
                    if int(v) == int(product_id):
                        return count_product
                    else:
                        break
        return False

    def move_tmc(self, div_from, div_to, product_id_def, quantity=1):
        """Переместить ТМЦ"""
        division_from = self.set_division(div_from)
        division_to = self.set_division(div_to)
        check_def, product = self.del_tmc(div_from, product_id_def, quantity)
        if check_def:
            self.append_tmc(div_to, product, quantity, product_id=product_id_def)
            return True
        else:
            return False


class OfficeEquipment():
    def __init__(self, id_, type_, firm, model, count_):
        self.id_ = id_
        self.type_ = type_
        self.firm = firm
        self.model = model
        self.count_ = count_

    @classmethod
    def valid_count(cls, *args):
        check_if_count = True
        while check_if_count:
            count_ = input("Введите количество добавляемых ТМЦ\n")
            if count_.isdigit():
                check_if_count = False
                if int(count_):
                    check_if_div_count = True
                    while check_if_div_count:
                        print("Введите номер склада для добавления ТМЦ\n")
                        for i, division_name in enumerate(main_div.divisions.keys(), 1):
                            print(f"{i}. {division_name}")
                        div_num = input(f"Для возврата в главное меню введите 'b'\n")
                        div_name = ''
                        if div_num.isdigit():
                            for i, division_name in enumerate(main_div.divisions.keys(), 1):
                                if i == int(div_num):
                                    div_name = division_name
                        elif div_num == 'b':
                            break
                        if div_name:
                            main_div.append_tmc(div_name, cls(round(random() * 1000000000), *args), int(count_))
                            check_if_div_count = False
                        else:
                            print("Команда неизвестна, попробуйте еще раз.")
                else:
                    check_if_count = True
                    print("Количество добавляемых ТМЦ введено некорректно\n"
                          "Попробуйте ввести коректно еще раз\n"
                          "Для возврата в главное меню введите 'b'")
            elif count_ == 'b':
                break
            else:
                print("Количество добавляемых ТМЦ введено некорректно\n"
                      "Попробуйте ввести коректно еще раз\n"
                      "Для возврата в главное меню введите 'b'")


class Printer(OfficeEquipment):
    def __init__(self, id_, firm, model, print_speed, colored, count_=1, type_='Printer'):
        super().__init__(id_, type_, firm, model, count_)
        self.print_speed = print_speed
        self.colored = colored

    @classmethod
    def valid_count(cls, *args):
        super().valid_count(*args)


class Xerox(OfficeEquipment):
    def __init__(self, id_, firm, model, scan, print_, print_speed, colored, count_=1, type_='Xerox'):
        super().__init__(id_, type_, firm, model, count_)
        self.scan = scan
        self.print_ = print_
        self.print_speed = print_speed
        self.colored = colored

    @classmethod
    def valid_count(cls, *args):
        super().valid_count(*args)


class Scanner(OfficeEquipment):
    def __init__(self, id_, firm, model, wifi, count_=1, type_='Scanner'):
        super().__init__(id_, type_, firm, model, count_)
        self.wifi = wifi

    @classmethod
    def valid_count(cls, *args):
        super().valid_count(*args)


main_div = Warehouse('Главный')
scanner_1 = Scanner(round(random() * 1000000000), 'Canon', 'HFL-3', False)
scanner_2 = Scanner(round(random() * 1000000000), 'HP', 'SGU-5', True)
scanner_3 = Scanner(round(random() * 1000000000), 'HP', 'SHU-5', True)
main_div.append_tmc(main_div.name, scanner_1)
main_div.append_tmc('Некрасова', scanner_2)
main_div.append_tmc('Некрасова', scanner_2)
main_div.append_tmc(main_div.name, scanner_3)
main_div.append_tmc('Раковская', scanner_1)
main_div.move_tmc('Главный', "Некрасова", scanner_1.id_)
check = True
while check:
    print(f"{'-' * 20}\n- Главное меню -\n"
          f"Введите номер команды:\n"
          f"1. Просмотреть склад\n"
          f"2. Добавить склад/подразделение/магазин\n"
          f"3. Добавить ТМЦ на склад\n"
          f"4. Удалить ТМЦ со склада\n"
          f"5. Переместить ТМЦ\n"
          f"Для завершения программы введите 'q'")
    command = input()
    if command != 'q':
        if command == '1':
            check_if = True
            while check_if:
                print(f"{'-' * 20}\n- Просмотр склада -\n"
                      f"Введите номер склада для просмотра:")
                for i, division_name in enumerate(main_div.divisions.keys(), 1):
                    print(f"{i}. {division_name}")
                div_num = input(f"Для возврата в главное меню введите 'b'\n")
                div_name = ''
                if div_num.isdigit():
                    for i, division_name in enumerate(main_div.divisions.keys(), 1):
                        if i == int(div_num):
                            div_name = division_name
                elif div_num == 'b':
                    break
                if div_name:
                    main_div.show_division(div_name)
                    check_if = False
                else:
                    print("Команда неизвестна, попробуйте еще раз.")
        elif command == '2':
            check_if = True
            while check_if:
                div_name = input(f"{'-' * 20}\n- Добавление склада -\n"
                                 f"Для возврата в главное меню введите 'b'\n"
                                 f"Введите название склада/подразделения/магазина для добавления:\n")
                if div_name and div_name != 'b':
                    main_div.append_division(div_name)
                    print(f"Склад {div_name} успешно добален")
                    check_if = False
                elif div_name == 'b':
                    break
                else:
                    print("Название склада не должно быть пустым, попробуйте еще раз.")
        elif command == '3':
            check_if = True
            while check_if:
                print(f"{'-' * 20}\n- Добавление ТМЦ на склад -\n"
                      f"Для возврата в главное меню введите 'b'\n"
                      f"Для добавления ТМЦ следуйте инструкциям:")
                type_ = input(f"Введите тип ТМЦ:\n"
                              f"1. Printer\n"
                              f"2. Scanner\n"
                              f"3. Xerox\n")
                if type_.isdigit():
                    if 1 <= int(type_) <= 3:
                        if type_ == '1':
                            firm = input("Введите фирму-производителя\n")
                            model = input("Введите модель\n")
                            print_speed = input("Введите скорость печати\n")
                            colored = input("Принтер цветной печати?\n"
                                            "1. Цветной\n"
                                            "2. Черно-белой\n")
                            if colored == '1':
                                colored = True
                            elif colored == '2':
                                colored = False
                            else:
                                colored = ''
                            Printer.valid_count(firm, model, print_speed, colored)
                            break
                        if type_ == '2':
                            firm = input("Введите фирму-производителя\n")
                            model = input("Введите модель\n")
                            wifi = input("Сканер имеет модуль WiFi?\n"
                                         "1. Да\n"
                                         "2. Нет\n")
                            if wifi == '1':
                                wifi = True
                            elif wifi == '2':
                                wifi = False
                            else:
                                wifi = ''
                            Scanner.valid_count(firm, model, wifi)
                            break
                        if type_ == '3':
                            firm = input("Введите фирму-производителя\n")
                            model = input("Введите модель\n")
                            scan = input("Ксерокс имеет функцию сканирования?\n"
                                         "1. Да\n"
                                         "2. Нет\n")
                            if scan == '1':
                                scan = True
                            elif scan == '2':
                                scan = False
                            else:
                                scan = ''
                            print_ = input("Ксерокс имеет функцию печати с ПК?\n"
                                           "1. Да\n"
                                           "2. Нет\n")
                            if print_ == '1':
                                print_ = True
                            elif print_ == '2':
                                print_ = False
                            else:
                                print_ = ''
                            print_speed = input("Введите скорость печати\n")
                            colored = input("Ксерокс цветной печати?\n"
                                            "1. Цветной\n"
                                            "2. Черно-белой\n")
                            if colored == '1':
                                colored = True
                            elif colored == '2':
                                colored = False
                            else:
                                colored = ''
                            Xerox.valid_count(firm, model, scan, print_, print_speed, colored)
                            break
                elif type_ == 'b':
                    break
                else:
                    print("Команда неизвестна, попробуйте еще раз.")
        elif command == '4':
            check_if = True
            while check_if:
                print(f"{'-' * 20}\n- Удаление ТМЦ со склада -\n"
                      f"Для возврата в главное меню введите 'b'\n"
                      f"Для удаления ТМЦ следуйте инструкциям:\n"
                      f"Введите номер склада:")
                for i, division_name in enumerate(main_div.divisions.keys(), 1):
                    print(f"{i}. {division_name}")
                div_num = input()
                div_name = ''
                if div_num.isdigit():
                    for i, division_name in enumerate(main_div.divisions.keys(), 1):
                        if i == int(div_num):
                            div_name = division_name
                elif div_num == 'b':
                    break
                if div_name:
                    check_if_id = True
                    while check_if_id:
                        main_div.show_division(div_name)
                        product_id = input(f"Для возврата в главное меню введите 'b'\n"
                                           f"Введите ID ТМЦ:\n")
                        if product_id.isdigit():
                            if main_div.check_id_in_div(div_name, int(product_id)):
                                del_count = input("Введите количество ТМЦ для удаления\n")
                                if del_count.isdigit() and del_count:
                                    if main_div.del_tmc(div_name, int(product_id), int(del_count)):
                                        check_if = False
                                        break
                                else:
                                    print("Количество товара для удаления должно быть положительным числом, "
                                          "попробуйте еще раз")
                                    continue
                            else:
                                print(f"На складе {div_name} отсутствует ТМЦ с ID {product_id}, попробуйте еще раз")
                                continue
                        elif product_id == 'b':
                            break
                        else:
                            print("ID должен состоять только из цифр, попробуйте еще раз")
                            continue
                else:
                    print("Команда неизвестна, попробуйте еще раз.")
        elif command == '5':
            while True:
                print(f"{'-' * 20}\n- Перемещение ТМЦ -\n"
                      f"Для возврата в главное меню введите 'b'\n"
                      f"Для перемещения ТМЦ следуйте инструкциям:\n"
                      f"Введите номер склада-отправителя:")
                for i, division_name in enumerate(main_div.divisions.keys(), 1):
                    print(f"{i}. {division_name}")
                div_num = input()
                div_name = ''
                if div_num.isdigit():
                    for i, division_name in enumerate(main_div.divisions.keys(), 1):
                        if i == int(div_num):
                            div_name = division_name
                elif div_num == 'b':
                    break
                print(f"Введите номер склада-получателя:")
                for i, division_name in enumerate(main_div.divisions.keys(), 1):
                    print(f"{i}. {division_name}")
                div_to_num = input()
                div_to_name = ''
                if div_to_num.isdigit():
                    for i, division_name in enumerate(main_div.divisions.keys(), 1):
                        if i == int(div_to_num):
                            div_to_name = division_name
                elif div_to_num == 'b':
                    break
                if div_name and div_to_name:
                    while True:
                        main_div.show_division(div_name)
                        product_id = input(f"Для возврата в главное меню введите 'b'\n"
                                           f"Введите ID ТМЦ для перемещения:\n")
                        if product_id.isdigit():
                            if main_div.check_id_in_div(div_name, int(product_id)):
                                move_count = input("Введите количество ТМЦ для перемещения\n")
                                if move_count.isdigit() and move_count:
                                    if main_div.move_tmc(div_name, div_to_name, int(product_id), int(move_count)):
                                        break
                                    else:
                                        print("Ошибка перемещения, попробуйте еще раз")
                                else:
                                    print("Количество товара для удаления должно быть положительным числом, "
                                          "попробуйте еще раз")
                                    continue
                            else:
                                print(f"На складе {div_name} отсутствует ТМЦ с ID {product_id}, попробуйте еще раз")
                                continue
                        elif product_id == 'b':
                            break
                        else:
                            print("ID должен состоять только из цифр, попробуйте еще раз")
                            continue
                else:
                    print("Команда неизвестна, попробуйте еще раз.")
                    continue
                break
    elif command == 'q':
        check = False
        print("Спасибо за работу!")
