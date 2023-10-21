import math
import random
A= random.randint(-100, 100)
print('A=', A)
B=random.randint(-100, 100)
print('B=', B)
C= random.randint(-100, 100)
print('C=', C)
try:
 x = abs(5*B-6*(A-30/C))**2
except ZeroDivisionError:
 x = 0
print('X=', x)
