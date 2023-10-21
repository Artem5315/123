import random
import math
a = random.randint(100000, 999999)
suma = 0
print('Рандомное число:', a)
while a > 0:
    digit = a % 10
    suma = suma + digit
    a = a // 10
print('Сумма:', suma)
