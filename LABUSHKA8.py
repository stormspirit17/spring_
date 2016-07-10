__author__ = 'Igor'
import time
import string
n = int(input('ENTER THE LENGTH OF YOUR LIST'))
a = []
i = 0
while i < n:
    i = i + 1
    meow = (input('enter a single element'))
    a.append(meow)
print(a)
trans = dict(zip(string.ascii_lowercase, range(26)))
def bubble_sort(a):
    changed = True
    while changed:
        changed = False
        for j in range(len(a)-1):
            if trans[a[j]] < trans[a[j+1]]:
                a[j], a[j+1] = a[j+1], a[j]
                changed = True
    return a
start = time.time()
print('bubble sort!', bubble_sort(a))
stop = time.time()-start
print('done in', stop, 'seconds')
def insertion_sort(a):
    for kpi in range(1, len(a)):
        j = kpi - 1
        key = trans[a[j]]
        while trans[a[j]] < key and j >= 0:
            j -= 1
            a[j+1] = key
    return a
staart = time.time()
print('insertion sort!!', insertion_sort(a))
stoop = time.time()-staart
print('done in', stoop, 'seconds')
def selection_sort(a):
    for dota in range(0, len(a)):
        ismall = dota
        for lol in range(dota, len(a)):
            if trans[a[ismall]] < trans[a[lol]]:
                ismall = lol
                a[dota], a[ismall] = a[ismall], a[dota]
    return a
strt = time.time()
print('selection sort!!!', selection_sort(a))
stp = time.time()-strt
print('done in', stp, 'seconds')
