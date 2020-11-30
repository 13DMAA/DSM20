# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    def __init__(self, c_num):
        self.c_num = c_num

    def __add__(self, other):
        real_self, imaginary_self, imaginary_unit_self = self.complex_in_list(self)
        real_other, imaginary_other, imaginary_unit_other = self.complex_in_list(other)
        if real_self and real_other and imaginary_self and imaginary_other and \
                imaginary_unit_self and imaginary_unit_other:
            if imaginary_unit_self == imaginary_unit_other:
                real_sum = real_self + real_other
                if real_sum % 1 == 0:
                    real_sum = int(real_sum)
                imaginary_sum = imaginary_self + imaginary_other
                if imaginary_sum % 1 == 0:
                    imaginary_sum = int(imaginary_sum)
                if imaginary_sum == 1:
                    imaginary_sum = ''
                print(f"{real_sum} + "
                      f"{imaginary_sum}"
                      f"{imaginary_unit_self}")
            else:
                print("Ошибка, символы мнимой единицы слагаемых не одинаковы")
        else:
            print("Ошибка ввода значений комплексных чисел")

    def __mul__(self, other):
        real_self, imaginary_self, imaginary_unit_self = self.complex_in_list(self)
        real_other, imaginary_other, imaginary_unit_other = self.complex_in_list(other)
        if real_self and real_other and imaginary_self and imaginary_other and \
                imaginary_unit_self and imaginary_unit_other:
            if imaginary_unit_self == imaginary_unit_other:
                str_ = f"{real_self * real_other}+" \
                       f"{real_self * imaginary_other}{imaginary_unit_other}+" \
                       f"{imaginary_self * real_other}{imaginary_unit_self}+" \
                       f"{imaginary_self * imaginary_other}{imaginary_unit_self + imaginary_unit_other}"
                str__ = ""
                real_self = 0
                imaginary_self = 0
                for el in str_.split('+'):
                    if len(el.split(f"{imaginary_unit_self}")) <= 1:
                        real_self += float(el.split(f"{imaginary_unit_self}")[0])
                    elif len(el.split(f"{imaginary_unit_self}")) == 2:
                        imaginary_self += float(el.split(f"{imaginary_unit_self}")[0])
                    elif len(el.split(f"{imaginary_unit_self}")) == 3:
                        real_self += float(el.split(f"{imaginary_unit_self}")[0])*-1
                if real_self % 1 == 0:
                    real_self = int(real_self)
                if imaginary_self % 1 == 0:
                    imaginary_self = int(imaginary_self)
                if imaginary_self > 0:
                    if imaginary_self == 1:
                        imaginary_self = f" + "
                    else:
                        imaginary_self = f" + {imaginary_self}"
                elif imaginary_self < 0:
                    if imaginary_self == -1:
                        imaginary_self = f" - "
                    else:
                        imaginary_self = f" - {imaginary_self*-1}"
                print(f"{real_self}{imaginary_self}{imaginary_unit_self}")
            else:
                print("Ошибка, символы мнимой единицы множителей не одинаковы")
        else:
            print("Ошибка ввода значений комплексных чисел")

    @staticmethod
    def complex_in_list(obj):
        if obj.check_valid_complex():
            for i, letter in enumerate(obj.c_num):
                if (ord(letter) == 43 or ord(letter) == 45) and i > 0:
                    if obj.c_num[i:-1] == "+" or obj.c_num[i:-1] == "-":
                        return float(obj.c_num[:i]), 1.0, obj.c_num[-1]
                    else:
                        return float(obj.c_num[:i]), float(obj.c_num[i:-1]), obj.c_num[-1]
        else:
            return 0, 0, 0

    def check_valid_complex(self):
        count_min_plus = 0
        for letter in self.c_num:
            if ord(letter) == 43 or ord(letter) == 45 or 122 >= ord(letter) >= 97 \
                    or 57 >= ord(letter) >= 48:
                if ord(letter) == 43 or ord(letter) == 45:
                    count_min_plus += 1
                if count_min_plus > 2:
                    return False
                pass
            else:
                return False
        return True


c_num_1 = Complex('1+3i')
c_num_2 = Complex('-5-2i')
c_num_1 + c_num_2
c_num_1 * c_num_2
