# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.
while True:
    str_ = input("Введите произвольную строку -->\n")
    str_ = str_.split(" ")
    i = 0
    i_list = []
    for value in str_:
        if value:
            i += 1
        else:
            i_list.append(i)
            i += 1
    i = len(i_list)-1
    while i >= 0:
        str_.pop(int(i_list[i]))
        i -= 1
    i = 1
    for el in str_:
        if len(el) > 10:
            el = el[:10]
        print(f"{i}. {el.title()}\n")
        i += 1
