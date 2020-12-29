# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)
import math


def sum_vector(vector_1, vector_2):
    sum_v = []
    if len(vector_1) < len(vector_2):
        vector_1.append(0)
    elif len(vector_2) < len(vector_1):
        vector_2.append(0)
    for item in range(len(vector_1)):
        sum_v.append(vector_1[item] + vector_2[item])
    return sum_v


def len_vector(vector):
    len_v = 0
    for el in vector:
        len_v += el * el
    return math.sqrt(len_v)


x1 = [10, 10, 10]
x2 = [0, 0, -10]
x3 = sum_vector(x1, x2)
print(x3)
print(len_vector(x3))
