__author__ = 'ForcesOfOdin'


class Stack:
    def __init__(self):
        self.items = []

    # O(1)
    def size(self):
        return len(self.items)

    # O(1)
    def is_empty(self):
        return self.size() == 0

    # O(1)
    def push(self, item):
        self.items.append(item)

    # O(1)
    def pop(self):
        return self.items.pop()

    # O(1)
    def peek(self):
        return self.items[-1]


class Queue:
    def __init__(self):
        self.items = []

    # O(1)
    def size(self):
        return len(self.items)

    # O(1)
    def is_empty(self):
        return self.size() == 0

    # O(1)
    def enqueue(self, item):
        self.items.append(item)

    # O(n)
    def dequeue(self):
        item = self.items[0]
        self.items.remove(item)
        return item
