__author__ = 'LENOVO'
l = [89, 100501, 7, 666, 69, 545.61, 18, 6.4]
elem = 85
result = 'Not found'
while l:
    mid = int(len(l)/2)
    cand = l[mid]
    if cand == elem:
        result = 'found'
        break
    elif elem < cand:
        l = l[:mid]
    else:
        l = l[mid+1:]
print(result)