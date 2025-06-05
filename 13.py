import random


def generate_matrix(rows, cols, min_val=-100, max_val=100):
    """Генерация матрицы заданного размера со случайными значениями"""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]


def add_matrices(matrix1, matrix2):
    """Сложение двух матриц одинаковой размерности"""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Матрицы должны быть одинакового размера")

    return {
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))
         for i in range(len(matrix1))
         ]
    }


def print_matrix(matrix):
    """Красивый вывод матрицы"""
    for row in matrix:
        print(row)


# Основная программа
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Генерация двух матриц
matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)

print("\nМатрица 1:")
print_matrix(matrix_1)

print("\nМатрица 2:")
print_matrix(matrix_2)

# Сложение матриц
try:
    matrix_3 = add_matrices(matrix_1, matrix_2)
    print("\nРезультат сложения (Матрица 3):")
    print_matrix(matrix_3)
except ValueError as e:
    print(f"\nОшибка: {e}")
