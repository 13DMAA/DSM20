# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.
name = "ED"
lastname = "Bibikov"
age = 31
print("My name is ", name, ". My lastname is ", lastname, ". I`m ", age, sep="", end=".\n")
name = input("Введите своё имя здесь --> ")
lastname = input("Введите свою фамилию здесь --> ")
age = input("Введите свой возраст здесь --> ")
print("My name is ", name, ". My lastname is ", lastname, ". I`m ", age, sep="", end=".\n")
age = int(age) + 1
print("Через год мне будет ", age, sep="", end=".")
# В этом задании ведь еще нет if else... но если бы были,
# Я сделал бы проверку на введенный возраст - является ли он int
