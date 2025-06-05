my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_list_recursive(lst):
    if not lst:  # базовый случай - список пуст
        print("Конец списка")
        return

    print(lst[0])  # выводим первый элемент
    print_list_recursive(lst[1:])  # рекурсивный вызов с оставшейся частью списка


# Вызов функции
print_list_recursive(my_list)