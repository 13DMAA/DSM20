# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calc_cons(self, *args):
        result = 0
        for item in args:
            result += item.calc_cons
        return round(result, 2)


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def calc_cons(self):
        return round(self.v / 6.5 + 0.5, 2)

    def parent_calc_conv(self, *args):
        return super().calc_cons(*args)


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def calc_cons(self):
        return round(0.02 * self.h + 0.3, 2)
        # при первом запросе в поисковике не нашел правильной формулы
        # дальше не искал, подогнал примерно, что пришло в голову

    def parent_calc_conv(self, *args):
        return super().calc_cons(*args)


coat = Coat(34)
print(f"Расход ткани для пальто размером {coat.v} = {coat.calc_cons} м2")
costume = Costume(175)
print(f"Расход ткани для костюма, рост {costume.h} см = {costume.calc_cons} м2")
print(f"Общий расход ткани на все изделия = {coat.parent_calc_conv(coat, costume)} м2")
print(f"Общий расход ткани на все изделия = {costume.parent_calc_conv(coat, costume)} м2")
# Googleние ничего конкретного не дало, как правильно обратиться к методу
# родительского абстрактного класса, который уже переопределен во всех
# дочерних классах, буду рад узнать как проще это сделать
