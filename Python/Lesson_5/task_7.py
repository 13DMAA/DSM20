# 7. Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open(r"Sample_files/text_7.txt", "r", encoding="utf-8") as file_handle:
    # print(file_handle.read())
    average_profit = 0
    average_profit_count = 0
    dict_firm = {}
    dict_average_profit = {}
    list_dicts = []
    for item in file_handle.readlines():
        print(item.split()[-2:])
        profit = int(item.split()[-2]) - int(item.split()[-1])
        dict_firm.update({item.split()[0]: profit})
        print(profit)
        if profit > 0:
            average_profit += profit
            average_profit_count += 1
    list_dicts.append(dict_firm)
    print(average_profit, average_profit_count)
    average_profit = average_profit / average_profit_count
    dict_average_profit.update({"average_profit": average_profit})
    list_dicts.append(dict_average_profit)
    print(list_dicts)
    with open(r"Sample_files/text_77.json", "w", encoding="utf-8") as json_handle:
        json.dump(list_dicts, json_handle, indent=4, ensure_ascii=False)
