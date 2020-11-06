# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
while True:
    month = int(input("Введите номер месяца от 1 до 12\n"))
    year_dict = {"зима": [12, 1, 2, "ы"],
                 "весна": [3, 4, 5, "ы"],
                 "лето": [6, 7, 8, "а"],
                 "осень": [9, 10, 11, "и"]}
    for key, value_dict in year_dict.items():
        for value_list in value_dict:
            if month == value_list:
                print(f"Это месяц {key[:len(key) - 1]}{value_dict[len(value_dict) - 1]}")
