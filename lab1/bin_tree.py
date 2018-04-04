class Node(object):
    def __init__(self, identifier):
        self._identifier = identifier
        self._left = None
        self._right = None
        self._parent = None

    def get_identifier(self):
        return self._identifier

    def set_identifier(self, identifier):
        if isinstance(identifier, str):
            self._identifier = identifier
        else:
            raise TypeError('Identifier should be string')

    identifier = property(get_identifier, set_identifier)

    def get_parent(self):
        return self._parent

    parent = property(get_parent)

    def insert(self, node):
        if type(node) is not Node:
            raise TypeError('You can insert only objects type of Node')
        if node.identifier < self._identifier:
            if self._left is None:
                self._left = node
                node._parent = self
            else:
                self._left.insert(node)
        elif node.identifier > self._identifier:
            if self._right is None:
                self._right = node
                node._parent = self
            else:
                self._right.insert(node)
        else:
            raise KeyError('Identifier already exists')

    def find(self, key, cmp_count):
        if type(key) is not str:
            raise TypeError('Key for search should be string')
        if self._identifier is None:
            return None
        elif self._identifier == key:
            return self
        elif key < self._identifier:
            cmp_count[0] += 1
            if self._left is not None:
                return self._left.find(key, cmp_count)
            else:
                return None
        elif key > self._identifier:
            cmp_count[0] += 1
            if self._right is not None:
                return self._right.find(key, cmp_count)
            else:
                return None

    def child_count(self, count):
        if self._left is not None:
            count[0] += 1
            self._left.child_count(count)
        if self._right is not None:
            count[0] += 1
            self._right.child_count(count)
        return count[0]
