""" Implement linked list data structure."""

class Node:
    """implement node structure."""
    def __init__(self,data,pointer=None):
        self.data = data
        self.pointer = pointer


class LinkedList:
    """ Implement linked list."""
    def __init__(self, iterable=None):
        self.head = None
        self.length = 0
        if isinstance(iterable, (str, list, tuple)):
            for item in iterable:
                self.push(item)

    def __len__(self):
        """Reset default function for len."""
        return self.length 

    def __str___(self):
        """Reset default function for str."""
        return self.display()

    def size(self):
        """Give length of linked list."""
        return len(self)

    def push(self, data):
        """Add node to the front of the list."""
        self.head = Node(data, self.head )
        self.length += 1

    def pop(self):
        """Remove first node from list."""
        if not self.head:
            raise IndexError('Cannot pop from empty list.')
        data = self.head.data
        self.head = self.head.pointer
        self.length -= 1
        return data

    def search(self, data):
        """Travers through linked list to find Node with data"""
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.pointer
        raise ValueError('Node is not in list.')

    def insert(self, data, Node):
        """Insert Node at specified point in linked list."""
        cur = search(data)
        Node.pointer = cur.pointer
        cur.pointer = Node
        self.length +=  1
        return 'Node inserted after' + data

    def remove(self, data):
        """Remove node from linked list."""
        if self.head.data == data:
            self.head = self.head.pointer
            self.length -= 1
            return
        cur = self.head
        while cur:
            if cur.pointer == data:
                xn = cur.pointer
                cur.pointer = xn.pointer
                self.length -= 1
                return
            cur = cur.pointer
        
        raise ValueError('Node is not in list.')

    def display(self):
        """Display LinkedList."""
        if not self.head:
            return ValueError('LinkedList is empty.')
        cur = self.head
        l = []
        while cur:
            l.append(cur.data)
            cur = cur.pointer
        return tuple(l).__str__()

    