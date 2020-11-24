# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между
# \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
# то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell > other.cell:
            return self.cell - other.cell
        else:
            return other.cell - self.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, row):
        str_ = ""
        for i in range(self.cell // row):
            str_ += "*" * row + "\n"
        str_ += "*" * (self.cell % row) + "\n"
        return str_


cell_1 = Cell(15)
cell_2 = Cell(32)
print(f"Сложение клеток со значениями {cell_1.cell} и {cell_2.cell} = {cell_1 + cell_2}")
print(f"Разность клеток со значениями {cell_1.cell} и {cell_2.cell} = {cell_1 - cell_2}")
print(f"Произведение клеток со значениями {cell_1.cell} и {cell_2.cell} = {cell_1 * cell_2}")
print(f"Целочисленное деление клеток со значениями {cell_1.cell} и {cell_2.cell} = {cell_1 // cell_2}")
print(f"Целочисленное деление клеток со значениями {cell_2.cell} и {cell_1.cell} = {cell_2 // cell_1}")
print(cell_1.make_order(7))
print(cell_2.make_order(12))
