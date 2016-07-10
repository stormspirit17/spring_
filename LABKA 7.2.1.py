__author__ = 'LENOVO'
while True:
    n = int(input('PLEASE ENTER YOUR NUMBER'))
    if n == 00:
        break
    else:
        def convert(x):
            if x < 10:
                return str(x)
            elif (x == 10):
                return 'A'
            elif (x == 11):
                return 'B'
            elif (x == 12):
                return 'C'
            elif (x == 13):
                return 'D'
            elif (x == 14):
                return 'E'
            elif (x == 15):
                return 'F'
        def sixteen(n):
            n = abs(n)
            remaining = n // 16
            last = n % 16
            if remaining == 0:
                return convert(last)
            else:
                return sixteen(remaining) + convert(last)
        if n >= 0:
            print(sixteen(n))
        else:
            print('-', sixteen(n))
        print('perevirka', hex(n))
