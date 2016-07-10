__author__ = 'LENOVO'
from math import*
print('a = ln(n!)/n^2')
n = 1
s = 0
a = 1
while n < 13:
    s = a + 1
    a = a + log(factorial(n))/n**2
    n = n + 1
    if n == 13:
        print(s)
