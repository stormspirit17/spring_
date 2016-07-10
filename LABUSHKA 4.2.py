__author__ = 'LENOVO'
from math import*
n = int(input('Enter a number'))
eps = 0.0001
if n >= eps:
    print(int(log(n, 10))+1)
elif abs(n) < eps:
    print(1)
else:
    print(int(log(-n, 10))+1)


