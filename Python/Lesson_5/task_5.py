# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randrange
with open("file_task_5.txt", "w+", encoding="utf-8") as file_handle:
    file_handle.write(' '.join(map(str, [item*randrange(1, 9) for item in range(1, randrange(5, 20))])))
    file_handle.seek(0)
    list_ = [item for item in map(int, file_handle.read().split())]
    print(f"Сумма чисел в файле {file_handle.name} = {sum(list_)}")

