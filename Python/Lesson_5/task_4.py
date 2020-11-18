# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
# pip install googletrans
from googletrans import Translator
translator = Translator()
with open(r"Sample_files\text_4.txt", "r+", encoding="utf-8") as file_handle:
    count_item = 0
    for item in file_handle.readlines():
        count_item += 1
        result = translator.translate(item, dest="ru")
        print(result.text)
        with open(f"task_4_file_{count_item}.txt", "w", encoding="utf-8") as item_handle:
            item_handle.write(result.text)
