import random
from heap import Heap
from heap import Node
import math


class Vertex(object):
    def __init__(self, name, weight):
        self.next = None
        self.name = name
        self.weight = weight


class Graph(object):
    def __init__(self, n, m):
        self.adj = []
        self.n = n
        for i in range(n):
            prev = None
            rand_coeff = random.randint(-20, 20)
            for j in range(round(m / n * (1 + rand_coeff / 100))):
                v = random.randint(0, n - 1)
                p = Vertex(v, random.randint(1, 100))
                p.next = prev
                prev = p
            self.adj += [p]

    def extend(self, diff, coeff):
        v_in_list_before = self.n // coeff
        v_in_list_after = (self.n + diff)  // coeff
        for i in range(self.n):
            prev = self.adj[i]
            for j in range(v_in_list_before, v_in_list_after):
                v = random.randint(0, self.n + diff - 1)
                p = Vertex(v, random.randint(1, 1000000))
                p.next = prev
                prev = p
            self.adj[i] = p
        self.n += diff
        for i in range(diff):
            prev = None
            for j in range(v_in_list_after):
                v = random.randint(0, self.n - 1)
                p = Vertex(v, random.randint(1, 1000000))
                p.next = prev
                prev = p
            self.adj += [p]




    def dijktstra_dheap(self, d, s):
        node = []
        index = list(range(0, self.n))
        for i in range(0, self.n):
            node += [Node(i, math.inf)]
        heap = Heap(d, self.n, node, index)
        heap.node[s].key = 0
        nq = self.n
        heap.make_queue()
        while nq > 0:
            node0 = heap.node[0]
            nq = heap.extract_min()
            i = node0.name
            dist = node0.key
            p = self.adj[i]
            while p is not None:
                j = p.name
                jq = heap.index[j]
                if heap.node[jq].key > (dist + p.weight):
                    heap.node[jq].key = dist + p.weight
                    heap.shift_up(jq)
                p = p.next
        return heap
