__author__ = 'LENOVO'
length = int(input('enter the length of your list'))
a = 0
lst = []
while a < length:
    a = a + 1
    el = float(input('enter the element'))
    sp = lst.append(el)
print(lst)
max = (max(lst), lst.index(max(lst)))
min = (min(lst), lst.index(min(lst)))
print(max, min)
input()
