# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.
from time import sleep


class Car:
    def __init__(self, speed=0, color="white", name="car", is_police=False, speed_limit=100, direction="stop"):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.speed_limit = speed_limit
        self.direction = direction

    def go(self):
        self.direction = "forward"
        self.turn()
        print("Go - go!")
        while self.show_speed() < self.speed_limit:
            sleep(1)
            self.speed += 10
            print(f"Скорость автомобиля = {self.show_speed()}")
        if self.show_speed() >= self.speed_limit:
            print(f"Вы привысили ограничение скорости в {self.speed_limit} км/ч, экстренная остановка")
            self.stop()

    def stop(self):
        self.direction = "stop"
        self.turn()
        self.speed = 0

    def turn(self):
        print(f"Turn {self.direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed=0, color="white", name="car", is_police=False, speed_limit=60):
        super().__init__(speed, color, name, is_police, speed_limit)


class WorkCar(Car):
    def __init__(self, speed=0, color="white", name="car", is_police=False, speed_limit=40):
        super().__init__(speed, color, name, is_police, speed_limit)


class SportCar(Car):
    def __init__(self, speed=0, color="white", name="car", is_police=False, speed_limit=100):
        super().__init__(speed, color, name, is_police, speed_limit)


class PoliceCar(Car):
    def __init__(self, speed=0, color="white", name="car", is_police=True, speed_limit=170):
        super().__init__(speed, color, name, is_police, speed_limit)


town_car = TownCar()
town_car.go()
work_car = WorkCar()
work_car.go()
sport_car = SportCar()
sport_car.go()
police_car = PoliceCar()
police_car.go()
# SportCar, WorkCar, PoliceCar
