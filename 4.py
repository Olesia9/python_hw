# Задание 1
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))

# Вычисление площади и периметра
area = a * b
perimeter = 2 * (a + b)

# Вывод результатов
print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")

# Ввод пятизначного числа
number = int(input("Введите пятизначное число: "))

# Задание 2
tens_of_thousands = number // 10000
thousands = (number // 1000) % 10
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

# Выполняем вычисления по алгоритму
result = (tens ** units) * hundreds / (tens_of_thousands - thousands)

# Вывод результата
print(f"Результат вычислений: {result}")