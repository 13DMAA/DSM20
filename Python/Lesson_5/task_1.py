# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open("file_task_1.txt", "w", encoding="utf-8") as file_handle:
    while True:
        input_ = input("Введите текст либо нажмите \"Enter\" для завершения работы\n")
        if input_:
            file_handle.write(input_ + "\n")
        else:
            print("Ввод закончен")
            break
