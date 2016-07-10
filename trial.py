from math import factorial
from random import shuffle
class Graph(object):
    def __init__(self):
        self.nodes = []
        self.connections = []
        self.distances = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, fr, to, dist):
        self.connections.append([to, fr])
        self.connections.append([fr, to])
        self.distances[(fr, to)] = dist
        self.distances[(to, fr)] = dist

    def __str__(self):
        return str(self.distances)

    def pathfinder(self, beginning, end):
        if beginning not in self.nodes:
            raise ValueError('Wrong node')
        else:
            n = 0
            initial = beginning
            newlist = self.connections
            visited = [beginning]
            distance = 0
            for pair in newlist:
                if initial in pair:
                    pair.remove(initial)
                    #print('pair', pair)
                    visited.append(pair[0])
                    initial = pair[0]
                    newlist.remove(pair)
                    #print('newlist', newlist, '\n', 'visited', visited)
                # if end in visited:
                #     i = 0
                #     while i < len(visited)-1:
                #         distance = distance + self.distances[(visited[i], visited[i+1])]
                #         i += 1
                #     skyrim = [(visited, distance)]
                if visited == None:
                    continue
                else:
                    if end in visited:
                        return visited
    def bad_method(self, fr, to):
        meow = self.pathfinder(fr, to)
        n = 0
        while n < factorial(len(self.connections)):
            shuffle(self.connections)
            n += 1
            kek = self.pathfinder(fr, to)
            if kek not in meow:
                meow.append(kek)
        #meow.remove(None)
        return meow

g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('D', 'F', 6)
g.add_edge('D', 'E', 7)
g.add_edge('F', 'E', 4)
g.add_edge('C', 'E', 1)
g.add_edge('A', 'E', 12)

#print(g.distances)
#print(g.connections)
print(g.pathfinder('C', 'D'))
#print(g.bad_method('F', 'C'))
