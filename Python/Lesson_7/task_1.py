# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str_ = ""
        # for item in self.matrix:
        #     str__ = ""
        #     for item_ in item:
        #         str__ += str(item_) + " "
        #     str_ += str__ + "\n"
        # return str_
        for element in ("\n" + str(el) + " " if j == 0 and i else str(el) + " " for i, item in enumerate(self.matrix)
                        for
                        j, el in enumerate(item)):
            str_ += element
        return "-----\n" + str_ + "\n-----"

    def __add__(self, other):
        new_matrix = []
        for i, item in enumerate(self.matrix):
            new_matrix.append([el + int(other.matrix[i][j]) for j, el in enumerate(item)])
        return Matrix(new_matrix)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
