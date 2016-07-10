__author__ = 'LENOVO'
from math import*
n = int(input('enter a number'))
if n <0:
    print('Negative value')
elif n <= 8:
    print('There is no Merssene numbers')
elif n > 1000500:
    print('sorry, your n is too large')
else:
    prost = []
    for p in range(2, int(sqrt(n))):
        for m in prost:
            if p%m == 0:
                break
        else:
            prost.append(p)
    for i in range(n):
        for p in prost:
            if i == pow(2, p) - 1:
                print(i)
