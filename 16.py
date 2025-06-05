# Задание 1
class CashRegister:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

    def top_up(self, x):
        """Пополнить кассу на X"""
        self.amount += x

    def count_1000(self):
        """Сколько целых тысяч осталось в кассе"""
        return self.amount // 1000

    def take_away(self, x):
        """Забрать X из кассы"""
        if x > self.amount:
            raise ValueError("Недостаточно денег в кассе")
        self.amount -= x


# Пример использования
kassa = CashRegister(5000)
kassa.top_up(3000)
print(f"Целых тысяч в кассе: {kassa.count_1000()}")
try:
    kassa.take_away(2000)
    print(f"Остаток: {kassa.amount}")
    kassa.take_away(10000)  # Вызовет ошибку
except ValueError as e:
    print(f"Ошибка: {e}")

# Задание 2
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s  # шаг перемещения

    def go_up(self):
        """Увеличивает y на s"""
        self.y += self.s

    def go_down(self):
        """Уменьшает y на s"""
        self.y -= self.s

    def go_left(self):
        """Уменьшает x на s"""
        self.x -= self.s

    def go_right(self):
        """Увеличивает x на s"""
        self.x += self.s

    def evolve(self):
        """Увеличивает s на 1"""
        self.s += 1

    def degrade(self):
        """Уменьшает s на 1"""
        if self.s <= 1:
            raise ValueError("s не может быть меньше или равно 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        """Минимальное количество действий до точки (x2, y2)"""
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        if dx % self.s != 0 or dy % self.s != 0:
            return -1  # Невозможно достичь с текущим шагом

        return dx // self.s + dy // self.s


# Пример использования
t = Turtle(0, 0, 2)
t.go_up()
t.go_right()
print(f"Позиция: ({t.x}, {t.y})")
t.evolve()
print(f"Текущий шаг: {t.s}")
print(f"Шагов до (6, 6): {t.count_moves(6, 6)}")
try:
    t.degrade()
    t.degrade()  # Вызовет ошибку при s=1
except ValueError as e:
    print(f"Ошибка: {e}")
