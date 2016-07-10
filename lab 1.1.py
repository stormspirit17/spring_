__author__ = 'LENOVO'
import random
m = int(input('enter the length of the first list'))
i = 0
l = []
while i < m:
    i += 1
    elem = random.randint(-1000, 1000)
    l.append(elem)
l.sort(reverse=True)
print(l)
z = int(input('enter the length of the second list'))
kek = 0
n = []
while kek < z:
    kek += 1
    elem = random.randint(-1000, 1000)
    n.append(elem)
n.sort(reverse=True)
print(n)
result = []
def kpi(a, b):
    while len(a) > 0 and len(b) > 0:
        pew = max(a)
        kek = max(b)
        if pew > kek:
            result.append(pew)
            a.remove(pew)
        elif pew < kek:
            result.append(kek)
            b.remove(kek)
    if len(a) > len(b):
        x = a
    else:
        x = b
    while len(x) > 0:
        ipt = max(x)
        x.remove(ipt)
        result.append(ipt)
    return result
print(kpi(l, n))
