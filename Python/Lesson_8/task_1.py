# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, obj):
        day, month, year = Date.valid_date({el: k for el, k in enumerate(obj.date.split("-"))})
        if day and month and year:
            print(day, month, year)

    @staticmethod
    def valid_date(date):
        try:
            day, month, year = 0, 0, 0
            if int(date.setdefault(0)) < 1 or int(date.setdefault(0)) > 31:
                print(f"Число введено неверно. {date.setdefault(0)}")
            else:
                day = int(date.setdefault(0))
            if int(date.setdefault(1)) < 1 or int(date.setdefault(1)) > 12:
                print(f"Месяц введен неверно. {date.setdefault(1)}")
            else:
                month = int(date.setdefault(1))
            if int(date.setdefault(2)) < 1 or int(date.setdefault(2)) > 9999:
                print(f"Год введен неверно. {date.setdefault(2)}")
            else:
                year = int(date.setdefault(2))
            return day, month, year
        except ValueError:
            print("Ошибка ввода данных, введите числа в формате '31-12-9999'.")
            return day, month, year


date_1 = Date("31-11-2020")
Date.get_date(date_1)
