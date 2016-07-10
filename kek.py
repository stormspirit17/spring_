import time
# -*- coding: utf-8 -*-
# __author__ = 'LENOVO'
# a = int(input('height'))
# for i in range(a):
#     for j in range(i):
#         if j <= a - i:
#             print('', sep='', end='')
#         else:
#             print('*', sep='', end='')
#             print('\n')
# Фиотр Ьлума: отсеивает заведомо безуспешные операции поиска данных по ключу
# Если контр. сумма не сходится...
# Декораторы!
# def makebold(fn):
#     def wrapped():
#         return "<b>" + fn() + "</b>"
#     return wrapped()
# def makeitalic(fn):
#     def wrapped():
#         return '<i>' + fn() + '</i>'
#     return wrapped()
# @makebold
# @makeitalic
# def hello():
#     return 'hello vasya!'
# print(hello())
#вызвали болд, потом италик, и тип внутри них - Хелло
#Need to release 2 methods:
#__iter__ and __next__
# testlist = iter([1, 2, 3, 4, 5])
# class Fib:
#     def __init__(self, max):
#         self.max = max
#     def __iter__(self):
#         self.a = 0
#         self.b = 1
#         return self
#     def next(self):
#         fib = self.a
#         if fib > self.max:
#             raise StopIteration
#... .....
#Problem about horse's steps
#Need to find way of chess horse who come through all points of chess board only one time
#Обход на макс  глубину прежде чем перейти на новую вершину
# Next Lecture. Hash functions
# Passanger -- Id
# Slojnost' = O(N)
# P1, P2, P3...
#0, 1, 2...
#Nujno vichislit' adres i perejti k nemu za edinicu vremeni!
# Diiiiidbko
#h: x -- N, gde N - natural'noe
# bitcoin
#moshmost' floata bol'she chem integera))0)
#nu karoch iz-za floatov ebuchih kollizii byvaut, kogda 2 odinajovyh hash-f. u raznyh sobak
# i togda prihoditsya sravnivat' po bytam))0)
# class Point:
#     pass
# p = Point()
# p1 = Point()
# print(hash(p))
# print(hash(p1))
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return ('(' + str(self.x) + str(self.y) + ')')
    def __hash__(self):
        return 17*self.x + self.y
p = Point(0, 9)
p1 = Point(4, 2)
# print(hash(p))
# print(hash(p1))
# print('НИ')
# time.sleep(3)
# print('ХУ')
# time.sleep(3)
# print('Я')
#hash - tablica (google(net))
#tam tipa massiv, i ego elementy = buckets
#iz-za colliziy v bucketah byvaiut spiski (spisok v spiske karoch(ya debil, lol))
numb = int(input())
for i in range(numb):
    x = ''
