__author__ = 'Steven Sarasin'


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
        if self.is_empty():
            raise RuntimeError("Popped an empty stack")
        else:
            return self.items.pop()

    # O(1)
    def peek(self):
        if self.is_empty():
            raise RuntimeError("Peeked on an empty stack")
        else:
            return self.items[-1]

    def __str__(self):
        return str(self.items)


class ListQueue:
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
        if self.size() == 0:
            return None
        else:
            item = self.items[0]
            self.items.remove(item)
            return item

    def __str__(self):
        return str(self.items)


class QueueNode:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def get_queue_node_cargo(node):
        while node:
            yield node.cargo
            node = node.next
        return


class Queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    # O(1)
    def size(self):
        return self.length

    # O(1)
    def is_empty(self):
        return self.length == 0

    # O(1)
    def enqueue(self, cargo):
        node = QueueNode(cargo)
        node.next = None
        if self.length == 0:
            self.head = node
            self.last = self.head
            self.length += 1
        else:
            self.last.next = node
            self.last = node
            self.length += 1

    # O(1)
    def dequeue(self):
        if self.length == 0:
            return None
        else:
            cargo = self.head.cargo
            self.head = self.head.next
            self.length -= 1
            return cargo

    def __str__(self):
        node = self.head
        p = get_queue_node_cargo(node)
        return str(list(p))