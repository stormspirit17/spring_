from math import sqrt
eps = 0.0001
a = float(input('Enter A!'))
b = float(input('Enter B!'))
c = float(input('Enter C!'))
n = 3
m = 5
def sqr(a):
    x1 = 1.0
    xn = (x1 + a/x1)/2
    eps = 0.0001
    if a > 1:
        while abs(xn - x1) > eps:
            xn = (x1 + a/x1)/2
            x1 = x1 + eps
        return round (xn, 4)
    elif a < 1 and a > 0:
        aa = 1/a
        b = 1/sqr(aa)
        return round(b, 4)
    elif a == 0:
        return 0
    else:
        return 'DIIIIDbKO! A MENSHE ZA NUL`!!'
def kek(a, b, c):
    if abs(c-a) <= eps:
        return 'NA NUL` DILYTY NE MOZHNA!!11!1!!'
    elif abs(((a-b)**5)/((c-a)**3)) <= eps:
        return 0
    elif ((a-b)**5)/((c-a)**3) <0:
        return 'OT HALEPA! VID`EMNE CHYSLO!'
    else:
        lol = sqr(((a-b)**5)/((c-a)**3))
        return round(lol, 4)
print(kek(a, b, c))
perevirka = sqrt(((a-b)**5)/((c-a)**3))
print('perevirka', perevirka)
