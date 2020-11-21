# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name="", surname="", position="", wage=0, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        # print(self._Worker__income)
        try:
            wage = float(self.wage)
            bonus = float(self.bonus)
            print(f"Доход сотрудника {self.get_full_name()} {f'= {wage + bonus} $' if wage + bonus else 'не указан'}")
        except ValueError:
            print("Значения оклад и премия введены неверно, пожалуйста исправьте")


worker_2 = Position("Arnold", "Trump", "Director", 100000, 45000)
worker_2.get_total_income()
print(worker_2.get_full_name())
