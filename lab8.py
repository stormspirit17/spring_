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
def alphabet(x):
    if x == 'a':
        return 0
    elif x == 'b':
        return 1
    elif x == 'c':
        return 2
    elif x == 'd':
        return 3
    elif x == 'e':
        return 4
    elif x == 'f':
        return 5
    elif x == 'g':
        return 6
    elif x == 'h':
        return 7
    elif x == 'i':
        return 8
    elif x == 'j':
        return 9
    elif x == 'f':
        return 5
    elif x == 'g':
        return 6
    elif x == 'h':
        return 7
    elif x == 'i':
        return 8
    elif x == 'j':
        return 9
    elif x == 'k':
        return 10
    elif x == 'l':
        return 11
    elif x == 'm':
        return 12
    elif x == 'n':
        return 13
    elif x == 'o':
        return 14
    elif x == 'p':
        return 15
    elif x == 'q':
        return 16
    elif x == 'r':
        return 17
    elif x == 's':
        return 18
    elif x == 't':
        return 19
    elif x == 'u':
        return 20
    elif x == 'v':
        return 21
    elif x == 'w':
        return 22
    elif x == 'x':
        return 23
    elif x == 'y':
        return 24
    elif x == 'z':
        return 25
    else:
        return('Error')
def bubble_sort(a):
    changed = True
    while changed:
        changed = False
        for j in range(len(a)-1):
            if alphabet(a[j]) < alphabet(a[j+1]):
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
        key = alphabet(a[j])
        while alphabet(a[j]) < key and j >= 0:
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
            if alphabet(a[ismall]) < alphabet(a[lol]):
                ismall = lol
                a[dota], a[ismall] = a[ismall], a[dota]
    return a
strt = time.time()
print('selection sort!!!', selection_sort(a))
stp = time.time()-strt
print('done in', stp, 'seconds')
