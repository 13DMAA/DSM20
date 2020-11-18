# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("file_task_1.txt", "r", encoding="utf-8") as file_handle:
    file_split = file_handle.read().split("\n")
    count_lines = 0
    count_words = []
    for item in file_split:
        if item:
            count_words.append(len(item.split()))
            count_lines += 1
    print(f"Количество строк в файле {file_handle.name} = {count_lines}")
    for i in range(len(count_words)):
        print(f"Количество слов в строке {i + 1} = {count_words[i]}")
