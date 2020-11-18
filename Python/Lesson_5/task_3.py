# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
# и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open(r"Sample_files\text_3.txt", "r", encoding="utf-8") as file_handle:
    average_profit = 0
    count_worker = 0
    for item in file_handle.read().split("\n"):
        average_profit += float(item.split()[1])
        count_worker += 1
        if float(item.split()[1]) < 20000:
            print(f"{item.split()[0]} имеет оклад менее 20 тыс.")
    print(f"Средняя величина дохода сотрудников = {average_profit / count_worker}")
