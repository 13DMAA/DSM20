# 6. Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
with open(r"Sample_files/text_6.txt", "r", encoding="utf-8") as file_handle:
    dict_ = {}
    for item in file_handle.readlines():
        key = item.split()[0]
        sum_item_value_num = 0
        for item_value in item.split()[1:]:
            item_value_num = "0"
            for item_char in list(item_value):
                if item_char.isdigit():
                    item_value_num += item_char
            sum_item_value_num += int(item_value_num)
        dict_.update({key: sum_item_value_num})
    print(dict_)
