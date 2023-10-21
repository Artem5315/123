'''Дан вектор A, который содержит вещественные числа как больше, так и меньше нуля.
Округлите их до целых по принципу:
 положительные числа округляем всегда вверх до целого
 отрицательные числа округляем всегда вниз до целого
 0 остаётся 0'''
import numpy as np

def round_array(A):
    return np.where(A > 0, np.ceil(A), np.floor(A))

A = np.array([-3.1, -5.9, 0, 2.2, 9.8])
print(round_array(A))
