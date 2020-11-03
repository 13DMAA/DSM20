# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = input("Введите число --> ")
print(f"Сумма n + nn + nnn = {int(number) + int(number + number) + int(number + number + number)}")
