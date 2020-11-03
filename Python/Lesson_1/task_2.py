# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.
sec = int(input("Введите время в секундах здесь --> "))
hours = sec // 3600
minutes = int((sec % 3600) // 60)
sec = int(sec - hours * 3600 - minutes * 60)
if hours >= 24:
    hours = hours % 24
if hours >= 0 and hours <= 9:
    hours = "0" + str(hours)
if minutes >= 0 and minutes <= 9:
    minutes = "0" + str(minutes)
if sec >= 0 and sec <= 9:
    sec = "0" + str(sec)

print(f"{hours}:{minutes}:{sec}")
