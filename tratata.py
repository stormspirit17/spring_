from math import*
n = 0.0
e = 0.0001
a = float(input('Enter a number'))
if a <= -e:
    print('Error, negative value')
elif abs(a)<e:
    print('0')
else:
    while a >= e:
        n = n + e
        x = (n + a/n)/2
        if abs (sqrt(a) - x) <= e:
            break
    print(round(x, 3))
