# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = input("Введите целое положительное число --> ")
len_number = len(number) # нельзя такое использовать, но как я узнаю скольки значное число ввели?
# нашел здесь https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
number_change = int(number)
i = 1
max_num = 0
while i <= len_number:
    number_num = number_change % 10
    if number_num > max_num:
        max_num = number_num
    # print("number_num = ", number_num, sep="")
    number_change = number_change // 10
    # print("number_change = ", number_change, sep="")
    i += 1
    # print("max_num = ", max_num, sep="")
print(f"Самая большая цифра в числе {number} = {max_num}")