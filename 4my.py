i = 0
a = []
k = 0
q = int(input('number of people'))
while i < q:
    i += 1
    lol = input('''Im'ya Liudyly''''')
    kek = input('Misto')
    m = [lol, kek]
    a.append(tuple(m))
print a
counts = {}
for row in a:
    name = row[0]
    city = row[1]
    if city not in counts:
        counts[city] = 1
    else:
        counts[city] += 1
print(counts)+9