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
        return self.items.pop()

    # O(1)
    def peek(self):
        return self.items[-1]


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


class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def get_node_cargo(node):
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
        node = Node(cargo)
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
        p = get_node_cargo(node)
        return str(list(p))

if __name__ == "__main__":
    q = ListQueue()
    q2 = Queue()
    
    q.enqueue('a')
    q2.enqueue('a')
    
    print "q:", q, "q.size() =", q.size()
    print "q2:", q2, "q2.size() =", q2.size()
    
    q.enqueue('b')
    q2.enqueue('b')
    q.enqueue('c')
    q2.enqueue('c')

    print "q:", q, "q.size() =", q.size()
    print "q2:", q2, "q2.size() =", q2.size()

    print "q is empty:", str(q.is_empty())
    print "q2 is empty:", str(q2.is_empty())

    q.dequeue()
    q2.dequeue()

    print "q:", q, "q.size() =", q.size()
    print "q2:", q2, "q2.size() =", q2.size()

    q.dequeue()
    q2.dequeue()

    print "q:", q, "q.size() =", q.size()
    print "q2:", q2, "q2.size() =", q2.size()

    q.dequeue()
    q2.dequeue()

    print "q:", q, "q.size() =", q.size()
    print "q2:", q2, "q2.size() =", q2.size()

    print "q is empty:", str(q.is_empty())
    print "q2 is empty:", str(q2.is_empty())

    q.dequeue()
    q2.dequeue()