class Node:
    def __init__(self, cargo=None, next=None, prev=None):
        self.cargo = cargo
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.cargo)

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def isEmpty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
            # if list is empty the new node goes first
            self.head = node
        else:
            # find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # append the new node
            last.next = node
            node.prev = last
        self.length = self.length + 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo

    def size(self):
        return self.length

class PriorityQueue(Queue):
    def __init__(self):
        super(). __init__()
    def remove(self):
        maxval, maxnode = self.head.cargo, self.head
        node = self.head
        while node.next is not None:
            node = node.next
            if node.cargo >= maxval:
                maxval, maxnode = node.cargo, node

        if maxnode is self.head:
            self.head = maxnode.next

        if maxnode.prev:
            maxnode.prev.next = maxnode.next

        if maxnode.next:
            maxnode.next.prev = maxnode.prev

        self.length -= 1
        return maxval
    # def updateKey(self, vert, value):

# pq = PriorityQueue()
# pq.insert(3)
# pq.insert(1)
# pq.insert(5)
#
# print(pq.remove())
#
# pq.insert(2)
# pq.insert(4)
# pq.insert(2)
# while not pq.isEmpty():
#     print(pq.remove())
class TupQueue(object):
    def __init__(self):
        self.list = []
        # self.dict = {}
    def insert(self, dist, vert):
        self.list.append((dist, vert))
        # self.list.sort()
    # def priority(self, kek):
    #     if kek in self.list:
    #         return self.list.index(kek)
    def isEmpty(self):
        return len(self.list) == 0
    def remove(self):
        mx = max([x[0] for x in self.list])
        ind = [x[0] for x in self.list].index(mx)
        rem = self.list[ind]
        self.list.remove(rem)
        return rem[1]

    def updatekey(self, newkey, vert):
        ind = [x[1] for x in self.list].index(vert)
        # print(ind)
        self.list.remove(self.list[ind])
        self.list.append((newkey, vert))

    def __str__(self):
        return str(self.list)

# q = TupQueue()
# q.insert(192, 1)
# q.insert(104, 0)
# q.insert(130, 2)
# print(q)
# q.updatekey(322, 0)
# q.insert(500, 3)
# print(q)
# q.remove()
# print(q)
# q.remove()
# print(q)
class BaseVertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Vertex(BaseVertex):
    def __init__(self, key):
        BaseVertex.__init__(self, key)
        self.distance = 999999999
        self.color = "white"
        self.pred = None
        self.discovery = 0
        self.finish = 0

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance

    def setPred(self, pred):
        self.pred = pred

    def getPred(self):
        return self.pred

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setDiscovery(self, time):
        self.discovery = time

    def getDiscovery(self):
        return self.discovery

    def setFinish(self, time):
        self.finish = time

    def getFinish(self):
        return self.finish

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t,cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)
        fr = self.vertList[f]
        to = self.vertList[t]
        fr.addNeighbor(to, cost)
        # self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

g = Graph()
g.addVertex('kyiv')
g.addVertex('lviv')
g.addVertex('vinnytsa')
g.addVertex('zhytomyr')
g.addEdge('kyiv', 'zhytomyr', 200)
g.addEdge('zhytomyr', 'lviv', 400)
g.addEdge('vinnytsa', 'lviv', 300)
g.addEdge('kyiv', 'vinnytsa', 283)
d = Vertex('d')
g.vertList['kyiv'].setDistance(700)
g.vertList['vinnytsa'].setDistance(800)
print(g.vertList['kyiv'].getConnections())
def dijkstra(aGraph, start):
    pq = TupQueue()
    start.setDistance(0)
    for v in aGraph:
        pq.insert(v.getDistance(), v)
        print(pq)
    while not pq.isEmpty():
        currentVert = pq.remove()
        print(pq)
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.updatekey(newDist, nextVert)

