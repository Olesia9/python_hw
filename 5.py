# Задание 1
num = int(input("Введите целое число: "))

if num == 0:
    print("нулевое число")
else:
    if num > 0:
        sign = "положительное"
    else:
        sign = "отрицательное"

    if num % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    if num % 2 == 0:
        print(f"{sign} {parity} число")
    else:
        print("число не является четным")


# Задание 2
word = input("Введите слово из маленьких латинских букв: ").lower()

vowels = {'a', 'e', 'i', 'o', 'u'}
vowel_count = 0
consonant_count = 0
vowel_stats = {v: 0 for v in vowels}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_stats[letter] += 1
    else:
        consonant_count += 1

print(f"Согласных букв: {consonant_count}")
print(f"Гласных букв: {vowel_count}")

# Вывод статистики по каждой гласной
for vowel, count in vowel_stats.items():
    if count == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {count}")

# Задание 3
X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Сколько у Майкла: "))
B = int(input("Сколько у Ивана: "))

mike_can = A >= X
ivan_can = B >= X

if mike_can and ivan_can:
    print(2)
elif mike_can:
    print("Mike")
elif ivan_can:
    print("Ivan")
elif (A + B) >= X:
    print(1)
else:
    print(0)