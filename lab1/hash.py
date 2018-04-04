from bin_tree import Node


class HashTable(object):
    def __init__(self):
        self._table = []
        self._size = 0

    @staticmethod
    def hash_func(key):
        last_letter = 3
        hash_code = 0
        if len(key) < 3:
            last_letter = len(key)
        first_three = list(key)[0:last_letter:1]
        for char in first_three:
            hash_code += ord(char)
        return hash_code

    def insert(self, key):
        if type(key) is not str:
            raise TypeError('You can insert only string')
        index = self.hash_func(key)
        if index >= self._size:
            self._table += [None] * (index - self._size + 1)
            self._size = index + 1
        node = Node(key)
        if type(self._table[index]) is Node:
            self._table[index].insert(node)
        else:
            self._table[index] = node

    def find(self, key, cmp_count):
        if type(key) is not str:
            raise TypeError('You can find only string identifier')
        index = self.hash_func(key)
        if index + 1 > self._size:
            return None
        if self._table[index] is None:
            return None
        else:
            return self._table[index].find(key, cmp_count)

    def get_avg_collisions(self):
        coll_count = 0
        for node in self._table:
            node_count = [0]
            if node is not None:
                node_count[0] = 1
                node.child_count(node_count)
            coll_count += node_count[0]
        return coll_count / len(self._table)
