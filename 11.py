# Задание 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_sequence(n):
    initial_fact = factorial(n)
    result = []
    for i in range(initial_fact, 0, -1):
        result.append(factorial(i))
    return result

# Пример использования
num = int(input("Введите натуральное число: "))
print(factorial_sequence(num))

# Задание 2
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'


def get_pet(ID):
    return pets[ID] if ID in pets else False


def pets_list():
    for pet_id, pet_info in pets.items():
        for name, data in pet_info.items():
            age = data['Возраст питомца']
            print(f"ID: {pet_id}")
            print(f"Имя питомца: {name}")
            print(f"Вид питомца: {data['Вид питомца']}")
            print(f"Возраст: {age} {get_suffix(age)}")
            print(f"Владелец: {data['Имя владельца']}\n")


def create():
    last = collections.deque(pets, maxlen=1)[0] if pets else 0
    new_id = last + 1

    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Добавлен новый питомец с ID {new_id}")


def read(pet_id):
    pet = get_pet(pet_id)
    if not pet:
        print("Питомец с таким ID не найден")
        return

    for name, data in pet.items():
        age = data['Возраст питомца']
        print(f'Это {data["Вид питомца"]} по кличке "{name}". '
              f'Возраст питомца: {age} {get_suffix(age)}. '
              f'Имя владельца: {data["Имя владельца"]}')


def update(pet_id):
    pet = get_pet(pet_id)
    if not pet:
        print("Питомец с таким ID не найден")
        return

    for name in pet.keys():
        print(f"Обновление информации для питомца {name}")
        pet[name]["Вид питомца"] = input("Новый вид питомца: ") or pet[name]["Вид питомца"]
        age_input = input("Новый возраст питомца: ")
        pet[name]["Возраст питомца"] = int(age_input) if age_input else pet[name]["Возраст питомца"]
        pet[name]["Имя владельца"] = input("Новое имя владельца: ") or pet[name]["Имя владельца"]
        print("Информация обновлена")


def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        print(f"Питомец с ID {pet_id} удален")
    else:
        print("Питомец с таким ID не найден")


# Основной цикл программы
while True:
    print("\nДоступные команды: create, read, update, delete, list, stop")
    command = input("Введите команду: ").lower()

    if command == 'stop':
        break
    elif command == 'create':
        create()
    elif command == 'read':
        pet_id = int(input("Введите ID питомца: "))
        read(pet_id)
    elif command == 'update':
        pet_id = int(input("Введите ID питомца: "))
        update(pet_id)
    elif command == 'delete':
        pet_id = int(input("Введите ID питомца: "))
        delete(pet_id)
    elif command == 'list':
        pets_list()
    else:
        print("Неизвестная команда")
