# -*- coding: utf-8 -*-
"""
Created on Thu May 19 01:59:46 2016

@author: LENOVO
"""
from collections import defaultdict
class Network(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
    
    def add_node(self, value):
        self.nodes.add(value)
    def add_edge(self, person, friend):
        self.edges[person].append(friend)
        self.edges[friend].append(person)
    def isFriends(self, person, other):
        if other in self.edges[person] or person in self.edges[other]:
            return True
        else:
            return False
    def __repr__(self):
        return self.edges
    def __str__(self):
        return self.edges

g = Network()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('X')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
print(g.edges)



def bbfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return 'friends and their friends of', start, ':', visited, \
            'friends only', graph[start]


print (bbfs(g.edges, 'A'))
print(g.isFriends('A', 'B'))
print(g.isFriends('A', 'X'))
