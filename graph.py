__author__ = 'Steven Sarasin'


class Node:
    def __init__(self, value):
        self.value = value
        self.color = "white"
        self.dist = float("inf")
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __lt__(self, other):
        return float(self) < float(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __eq__(self, other):
        return float(self) == float(other)

    def __hash__(self):
        return hash(self.value)


def BFS(graph, source):

    from adts import Queue

    for node in graph.keys():
        if node is not source:
            node.color = "white"
            node.dist = float("inf")
            node.predecessor = None
    source.color = "grey"
    source.dist = 0
    source.predecessor = None
    q = Queue()
    q.enqueue(source)
    while q.size() is not 0:
        node = q.dequeue()
        for child in graph[node]:
            if child.color is "white":
                child.dist = node.dist + 1
                child.predecessor = node
                child.color = "grey"
                q.enqueue(child)
        node.color = "black"
