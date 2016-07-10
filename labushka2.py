__author__ = 'LENOVO'
# -*- coding: utf-8 -*-
import string
import collections
nya = open('2.txt', 'r')
#nya.seek(0)
a = str(nya.read())
#print(a)
for c in string.punctuation:
    a = a.replace(c, '')
for i in a:
    if i == '«' or i == '»' or i == '—':
        a = a.replace(i, '')
a = a.lower()
kek = a.split()
e = collections.Counter(kek)
d = e.most_common()
print(d)
new = []
for i in range(len(d)):
    dota = d[i][0]
    new.append(dota)
print(new)
zxc = '\n'.join(new)
print(zxc)
nya.close()
# def selection_sort(a):
#     for i in range(len(a)):
#         def pop(i):
#             return i[1]
#     for dota in range(0, len(a)):
#         ismall = dota
#         for lol in range(dota, len(a)):
#             if pop(a[ismall]) < pop(a[lol]):
#                 ismall = lol
#                 a[dota], a[ismall] = a[ismall], a[dota]
#     return a
# print(selection_sort(d))