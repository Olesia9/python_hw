# Задание 1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создаем класс Autobus, наследующий Transport
class Autobus(Transport):
    pass

# Создаем объект Autobus и выводим его параметры
autobus = Autobus("Renaul Logan", 180, 12)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")

# Задание 2
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

# Создаем объект Autobus и выводим вместимость
autobus = Autobus("Renaul Logan", 180, 12)
print(autobus.seating_capacity())
