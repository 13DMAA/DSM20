# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    def __init__(self, name="traffic_light"):
        self.__color = [["red", 31, 7], ["yellow", 33, 2], ["green", 32, 7]]
        self.name = name
        self.time = time.time()
        self.time_working = float(input("Введите время работы светофора в секундах\n"))

    def running(self):
        print(f"Start {self.name}, start time = {time.ctime(self.time)}")
        self.change_color(self.__color, len(self.__color))

    def change_color(self, color, i, reverse=False):
        time_now = time.time()
        print(f"\033[{color[len(color) - i][1]}m{color[len(color) - i][0]}")
        time.sleep(color[len(color) - i][2])
        if time.time() - self.time <= self.time_working:
            if i == 1:
                reverse = True
            elif i == len(color):
                reverse = False
            self.change_color(self.__color, i + 1, reverse) if reverse else self.change_color(self.__color, i - 1,
                                                                                              reverse)
        else:
            print("Светофор выключен!")
            return 0


traffic_light_1 = TrafficLight("traffic_light_1")
traffic_light_1.running()
