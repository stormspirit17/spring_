# -*- coding: utf-8 -*-
"""
Created on Mon May 16 01:06:03 2016
"""
from random import shuffle
from collections import defaultdict, deque
from math import factorial
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance      
    
def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = list(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
 
    #print('visited',visited)
    #print('path', path)
    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)
    
def printpath(graph, origin, destination):
    distance, path = shortest_path(graph, origin, destination)
    i = 0
    while i < factorial(len(graph.nodes)):
        l = list(graph.nodes)
        shuffle(l)
        graph.nodes = l
        dist2, path2 = shortest_path(graph, origin, destination)
        i += 1
        if path2 != path:
            break
    return distance, path, path2
        
graph = Graph()
cities = ['Донецьк', 'Харків', 'Київ', 'Дніпропетровськ', 'Львів', 'Вінниця', 'Житомир', 'Львів', 'Одеса']
for node in cities:
    graph.add_node(node)

graph.add_edge('Донецьк', 'Харків', 299)
graph.add_edge('Донецьк', 'Дніпропетровськ', 248)
graph.add_edge('Дніпропетровськ', 'Київ', 477)
graph.add_edge('Дніпропетровськ', 'Вінниця', 362)
graph.add_edge('Київ', 'Житомир', 140)
graph.add_edge('Житомир', 'Львів', 402)
graph.add_edge('Вінниця', 'Житомир', 128)
graph.add_edge('Вінниця', 'Львів', 362)
graph.add_edge('Харків', 'Київ', 479)
graph.add_edge('Одеса', 'Вінниця', 420)
graph.add_edge('Одеса', 'Дніпропетровськ', 340)
graph.add_edge('Харків', 'Дніпропетровськ', 217)
g = Graph()

g.add_node('1')
g.add_node('2')
g.add_node('3')
g.add_node('4')
#g.add_node('5')
#g.add_node('6')
g.add_edge('1', '2', 3)
g.add_edge('1', '3', 1)
g.add_edge('3', '4', 3)
g.add_edge('2', '4', 2)
g.add_edge('2', '3', 1)
#g.add_edge('3', '5', 5)
#g.add_edge('4', '6', 3)
#g.add_edge('5', '6', 3)
print('Прокладіть шлях між двома містами із списку:.', cities)
#print('edges', g.edges)
#print('dist',g.distances)
#print('nodes', g.nodes)
a = input('Звідки:')
b = input('Куди:')
#if a not in g.edges or b not in g.edges:
 #   raise KeyError('Такого елемента немає в списку')
#print('shortest', shortest_path(g, a, b)) 
print(printpath(graph, a, b))