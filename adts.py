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

    print "\nTESTING class ListQueue: instance called list_q."
    list_q = ListQueue()
    list_q.enqueue('a')
    print "	list_q:", list_q, "list_q.size() ==", list_q.size()
    list_q.enqueue('b')
    list_q.enqueue('c')
    print "	list_q:", list_q, "list_q.size() ==", list_q.size()
    print "	list_q is empty:", str(list_q.is_empty())
    list_q.dequeue()
    print "	list_q:", list_q, "list_q.size() ==", list_q.size()
    list_q.dequeue()
    print "	list_q:", list_q, "list_q.size() ==", list_q.size()
    list_q.dequeue()
    print "	list_q:", list_q, "list_q.size() ==", list_q.size()
    print "	list_q is empty:", str(list_q.is_empty())
    print "	list_q.dequeue() ==", str(list_q.dequeue())
    print "FINISHED TESTING ListQueue"

    print "\nTESTING class Queue: instance called link_q."
    link_q = Queue()
    link_q.enqueue('a')
    print "	link_q:", link_q, "link_q.size() ==", link_q.size()
    link_q.enqueue('b')
    link_q.enqueue('c')
    print "	link_q:", link_q, "link_q.size() ==", link_q.size()
    print "	link_q is empty:", str(link_q.is_empty())
    link_q.dequeue()
    print "	link_q:", link_q, "link_q.size() ==", link_q.size()
    link_q.dequeue()
    print "	link_q:", link_q, "link_q.size() ==", link_q.size()
    link_q.dequeue()
    print "	link_q:", link_q, "link_q.size() ==", link_q.size()
    print "	link_q is empty:", str(link_q.is_empty())
    link_q.dequeue()
    print "	link_q is empty:", str(link_q.is_empty())
    print "	link_q.dequeue() ==", str(link_q.dequeue())
    print "FINISHED TESTING Queue"






