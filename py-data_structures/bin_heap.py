"""Create a Binary Heap class."""


class Node:
    """ Create Node class with attributes."""

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.c1 = None
        self.c2 = None
        self.index = 0


class BinHeap:
    """Implement a Binary Heap."""

    def __init__(self, iterable=None):
        """Inistialize the Bin Heap."""
        self.root = None
        self.values = [None]
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.insert(Node)


"""
insert node
remove node
search
"""
