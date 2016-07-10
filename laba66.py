# -*- coding: utf-8 -*-
"""
Created on Wed May 18 01:17:45 2016
@author: LENOVO
"""

from collections import defaultdict

class Digraph(object):
    def __init__(self, nodes=[]):
        self.nodes = set()
        self.neighbours = defaultdict(set)
        self.dist = {}

    def addNode(self, *nodes):
        [self.nodes.add(n) for n in nodes]

    def addEdge(self, frm, to, d=1e309):
        self.addNode(frm, to)
        self.neighbours[frm].add(to)
        self.dist[ frm, to ] = d

    def dijkstra(self, start, maxD=1e309):
        """Returns a map of nodes to distance from start and a map of nodes to
        the neighbouring node that is closest to start."""
        # total distance from origin
        tdist = defaultdict(lambda: 1e309)
        tdist[start] = 0
        # neighbour that is nearest to the origin
        preceding_node = {}
        unvisited = self.nodes

        while unvisited:
            current = unvisited.intersection(tdist.keys())
            if not current: break
            min_node = min(current, key=tdist.get)
            unvisited.remove(min_node)

            for neighbour in self.neighbours[min_node]:
                d = tdist[min_node] + self.dist[min_node, neighbour]
                if tdist[neighbour] > d and maxD >= d:
                    tdist[neighbour] = d
                    preceding_node[neighbour] = min_node

        return tdist, preceding_node

    def min_path(self, start, end, maxD=1e309):
        """Returns the minimum distance and path from start to end."""
        tdist, preceding_node = self.dijkstra(start, maxD)
        dist = tdist[end]
        backpath = [end]
        try:
            while end != start:
                end = preceding_node[end]
                backpath.append(end)
            path = list(reversed(backpath))
        except KeyError:
            path = None

        return dist, path

graph = Digraph()
cities = ['Донецьк', 'Харків', 'Київ', 'Дніпропетровськ', 'Львів', 'Вінниця', 'Житомир', 'Львів']
for node in cities:
    graph.addNode(node)
graph.addEdge('Донецьк', 'Харків', 299)
graph.addEdge('Донецьк', 'Дніпропетровськ', 248)
graph.addEdge('Дніпропетровськ', 'Київ', 477)
graph.addEdge('Дніпропетровськ', 'Вінниця', 362)
graph.addEdge('Київ', 'Житомир', 140)
graph.addEdge('Житомир', 'Львів', 402)
graph.addEdge('Вінниця', 'Житомир', 128)
graph.addEdge('Вінниця', 'Львів', 362)
graph.addEdge('Харків', 'Київ', 479)
graph.addEdge('Харків', 'Дніпропетровськ', 217)
print(graph.neighbours)
print(graph.min_path('Львів', 'Донецьк'))