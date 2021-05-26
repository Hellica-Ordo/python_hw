# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {self.direction}.')

    def show_speed(self, speed):
        print(f'Скорость машины {self.name} - {self.speed} км/ч.')

class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}"

class SportCar(Car):

class WorkCar(Car):             # тут почему-то Питон ругается на отступы. ЧЯДНТ?
    def show_speed(self):
        return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}"

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

toyota = SportCar(175, 'silver', 'Toyota', False)
kamaz = WorkCar(70, 'brown', 'KAMAZ', False)
nypd = PoliceCar(190, 'white', 'NYPD')
lada = TownCar(35, 'red', 'Lada', False)

print(nypd.show_speed())
print(toyota.turn('налево'))
print(kamaz.go())