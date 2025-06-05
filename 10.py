# Задание 1
pets = {}

# Ввод данных о питомце
pet_name = input("Введите кличку питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца: "))
owner_name = input("Введите имя владельца: ")

# Добавление информации в словарь
pets[pet_name] = {
    'Вид питомца': pet_type,
    'Возраст питомца': pet_age,
    'Имя владельца': owner_name
}

# Функция для правильного склонения слова "год"
def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

# Получение информации о питомце
pet_info = pets[pet_name]
age_suffix = get_age_suffix(pet_info['Возраст питомца'])

# Формирование и вывод информации
print(f'Это {pet_info["Вид питомца"]} по кличке "{pet_name}". '
      f'Возраст питомца: {pet_info["Возраст питомца"]} {age_suffix}. '
      f'Имя владельца: {pet_info["Имя владельца"]}')

# Вывод всего словаря (для проверки)
print("\nВесь словарь pets:")
print(pets)

# Задание 2
my_dict = {}

for num in range(10, -6, -1):
    my_dict[num] = num ** num

# Вывод словаря (первые и последние 3 элемента для демонстрации)
print("Первые 3 элемента:")
for key in list(my_dict.keys())[:3]:
    print(f"{key}: {my_dict[key]}")

print("\nПоследние 3 элемента:")
for key in list(my_dict.keys())[-3:]:
    print(f"{key}: {my_dict[key]}")
