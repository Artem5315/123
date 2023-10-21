import math
import random
A= round(random.uniform(-100, 100), 3)
print('A=', A)
B= round(random.uniform(-100, 100), 3)
print('B=', B)
C= round(random.uniform(-100, 100), 3)
print('C=', C)
try:
 X = round(float(abs(5*B-6*(A-30/C))**2), 3)
except ZeroDivisionError:
 X = 0
print('X=', X)
