def minvalues(d):
    keys = list(d.keys())
    vals = list(d.values())
    min = vals[0]
    minkey = keys[0]
    for i in range(1, len(keys)):
        current = vals[i]
        if current < min:
            min = current
            minkey = keys[i]
    return minkey
def newdict(d, listik):
    g = 0
    keys = list(d.keys())
    vals = list(d.values())
    min = None
    for i in range(1, len(keys)):
        current = vals[i]
        while min == None and g < len(keys)-1 :
            if keys[g] in listik:
                minkey = keys[g]
                min = vals[g]
            g += 1
        if min == None:
            return
        if current < min and keys[i] in listik:
            min = current
            minkey = keys[i]
    return minkey

class Node(object):
    def __init__(self, cargo):
        self.ways = {self: 0}
        self.cargo = cargo
    def __str__(self):
        return self.cargo
    def __repr__(self):
        return self.cargo

    def connect(self, other, distance):
        self.ways.update({other:distance})
        other.ways.update({self:distance})

    def getnodes(self):
        kek = []
        l = []
        for node in self.ways.keys():
            l.append(node)
            kek.append(node)
        while l:
            cur = l.pop()
            for node in cur.ways.keys():
                if node not in kek:
                    l.append(node)
                    kek.append(node)
        return kek

    def dijkstra(self, par):
        all = self.getnodes()
        fr = dict.fromkeys(all, [])
        ways = {}
        for node in all:
            ways.update({node: [[node]]})
        for node in self.ways.keys():
            fr.update({node: [self]})
        distances = dict.fromkeys(all, float('Inf'))
        distances.update(self.ways)
        all.pop(all.index(self))
        current = newdict(self.ways, all)

        while all:
            for node in current.ways:
                if node in all:
                    if current.ways[node] + distances[current] < distances[node]:
                        distances.update({node: current.ways[node] + distances[current]})
                        fr.update({node: [current]})

                    if current.ways[node] + distances[current] == distances[node] and current not in fr[node] and current != node:
                        fr[node].append(current)

            all.pop(all.index(current))
            current = newdict(distances, all)

            if current == None:
                break


        for node in distances.keys():

            zapomnil = None
            while True:
                now = node
                while now != fr[now][0]:
                    if len(fr[now])>1:
                        zapomnil =now
                        k = fr[now]
                    ways[node][len(ways[node])-1].insert(0, fr[now][0])
                    now = fr[now][0]
                if zapomnil == None or len(fr[zapomnil])==1:
                    try:
                        fr[zapomnil] = k
                    except UnboundLocalError:
                        break

                    break
                else:
                    fr[zapomnil] = fr[zapomnil][1:]
                    ways[node].append([node])


        if par == 'd':
            return distances
        if par == 'w':
            return ways

def from_to(self, other):
    return(self.dijkstra('w')[other])



a1 = Node('1')
a2 = Node('2')
a3 = Node('3')
a4 = Node('4')
a1.connect(a2, 1)
a1.connect(a3, 2)
a2.connect(a3, 1)
a2.connect(a4, 2)
a3.connect(a4, 1)
print(a1.dijkstra('w'))
print(from_to(a1, a4))

