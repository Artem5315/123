'''Создайте двумерный массив размером n×n и заполните его
случайными двузначными числами. Замените все элементы побочной
диагонали на 0. Исходный и полученный массивы выведите на экран.
Числа в строке разделяйте одним пробелом.'''
import random

# ввод размерности массива
n = int(input("Введите размерность массива: "))

# создание двумерного массива и заполнение случайными двузначными числами
array = [[random.randint(10, 99) for j in range(n)] for i in range(n)]

# вывод исходного массива
print("Исходный массив:")
for row in array:
    print(*row)

# замена элементов побочной диагонали на 0
for i in range(n):
    array[i][n-i-1] = 0

# вывод измененного массива
print("Измененный массив:")
for row in array:
    print(*row)
