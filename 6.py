# Задание 1
N = int(input("Введите количество чисел: "))
count = 0

for _ in range(N):
    num = int(input())
    if num == 0:
        count += 1

print(f"Количество нулей: {count}")

# Задание 2
X = int(input("Введите натуральное число X: "))
count = 0

for i in range(1, int(X**0.5) + 1):
    if X % i == 0:
        if i == X // i:
            count += 1
        else:
            count += 2

print(f"Количество натуральных делителей: {count}")

# Задание 3
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Генерируем четные числа от A до B включительно
even_numbers = [str(num) for num in range(A, B + 1) if num % 2 == 0]

print(' '.join(even_numbers))

