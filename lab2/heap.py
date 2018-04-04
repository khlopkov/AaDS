class Node(object):
    def __init__(self, name, key):
        self.name = name
        self.key = key


class Heap(object):
    def __init__(self, d, n, node, index):
        self._d = d
        self._n = n
        self.node = node
        self.index = index

    def first_child(self, i):
        k = i*self._d + 1
        if k > self._n - 1:
            return 0
        else:
            return k

    def last_child(self, i):
        k = self.first_child(i)
        if k == 0:
            return 0
        else:
            return min(k + self._d - 1, self._n - 1)

    def parent(self, i):
        return (i - 1) // self._d

    def min_child(self, i):
        k_first = self.first_child(i)
        if k_first == 0:
            return i
        else:
            k_last = self.last_child(i)
            min_child = k_first
            min_key = self.node[k_first].key
            for j in range(k_first + 1, k_last + 1):
                if self.node[j].key < min_key:
                    min_key = self.node[j].key
                    min_child = j
            return min_child

    def shift_down(self, i):
        node0 = self.node[i]
        c = self.min_child(i)
        while (c != i) and (node0.key > self.node[c].key):
            self.node[i] = self.node[c]
            self.index[self.node[i].name] = i
            i = c
            c = self.min_child(i)
        self.node[i] = node0
        self.index[self.node[i].name] = i

    def shift_up(self, i):
        node0 = self.node[i]
        p = self.parent(i)
        while i != 0 and self.node[p].key > node0.key:
            self.node[i] = self.node[p]
            self.index[self.node[i].name] = i
            i = p
            p = self.parent(i)
        self.node[i] = node0
        self.index[self.node[i].name] = i

    def extract_min(self):
        node0 = self.node[0]

        self.node[0] = self.node[self._n - 1]
        self.node[self._n - 1] = node0
        self.index[self.node[self._n - 1].name] = self._n - 1

        self._n -= 1

        if self._n > 1:
            self.shift_down(0)
        return self._n

    def make_queue(self):
        for i in reversed(range(0, self._n)):
            self.shift_down(i)
