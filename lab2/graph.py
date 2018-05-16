import random
from heap import Heap
from heap import Node
import math
import sys


class Vertex(object):
    def __init__(self, name, weight):
        self.next = None
        self.name = name
        self.weight = weight


def init_graph(n: int, m: int, q: int, r: int):
    if n < 2 or m > n * n + 1 or m < n - 1:
        raise ValueError
    graph = [None] * n
    for i in range(0, m):
        edge_from = random.randint(0, n - 1)
        edge_to = edge_from
        while edge_from == edge_to:
            edge_to = random.randint(0, n-1)
        weight = random.randint(q, r)
        p = graph[edge_from]
        graph[edge_from] = Vertex(edge_to, weight)
        graph[edge_from].next = p
        ##print(sys.getsizeof(graph[edge_from]))
    return graph


def dijkstra_d_heap(graph, d, s):
    node = []
    index = list(range(0, len(graph)))
    for i in range(0, len(graph)):
        node += [Node(i, math.inf)]
    heap = Heap(d, len(graph), node, index)
    heap.node[s].key = 0
    heap.make_queue()
    nq = len(graph)
    while nq > 0:
        i = heap.node[0].name
        dist = heap.node[0].key
        nq = heap.extract_min()
        p = graph[i]
        while p is not None:
            j = p.name
            jq = index[j]
            if heap.node[jq].key > dist + p.weight:
                heap.node[jq].key = dist + p.weight
                heap.shift_up(jq)
            p = p.next
    return heap
