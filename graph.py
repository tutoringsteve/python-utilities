__author__ = 'Steven Sarasin'


class GraphNode:
    def __init__(self, key):
        self.key = key
        # adjacent_node key : weight to adjacent_node dictionary
        self.adjacent_nodes = {}
        #used for Depth First Search and Path Finding
        self.color = "white"
        self.dist = float("inf")
        self.prev = None

    def get_key(self):
        return self.key

    def add_adjacent_node(self, adj_node, weight=0):
        if adj_node not in self.adjacent_nodes:
            self.adjacent_nodes[adj_node] = weight

    def is_adjacent_to(self, adj_node):
        return adj_node in self.adjacent_nodes

    def get_weight_of_edge_with(self, adj_node):
        if self.is_adjacent_to(adj_node):
            return self.adjacent_nodes[adj_node]
        else:
            raise KeyError("attempted to get weight of edge to a node that isn't adjacent")

    def __str__(self):
        return str(self.key) + ": " + str([adj_node.key for adj_node in self.adjacent_nodes])


class Graph:
    def __init__(self):
        # key : GraphNode dictionary
        self.nodes = {}
        self.total_nodes = 0
        self.total_edges = 0

    def add_node(self, key):
        if key not in self.nodes.keys():
            self.nodes[key] = GraphNode(key)
            self.total_nodes += 1
        return self.nodes[key]

    def get_node(self, key):
        if key in self.nodes.keys():
            return self.nodes[key]
        else:
            raise KeyError("key not found in nodes")

    def add_edge(self, a, b):
        if a not in self.nodes.keys():
            self.add_node(a)
        if b not in self.nodes.keys():
            self.add_node(b)
        if b not in self.get_adjacent_nodes(a):
            self.nodes[a].add_adjacent_node(b)
            self.total_edges += 1
        else:
            raise KeyError("attempted to add edge comprised of node(s) not in the graph")

    def get_adjacent_nodes(self, key):
        if key in self.nodes.keys():
            return self.nodes[key].adjacent_nodes

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
        print node.cargo


if __name__ == "__main__":
    adj_graph = {0: [2, 10, 9, 5, 12, 11, 17, 7, 13, 14, 6, 3, 4, 15, 1, 16, 8], 1: [2, 17, 0, 37],
                 2: [0, 37, 1, 3, 35],
                 3: [34, 0, 2, 4], 4: [5, 33, 0, 3], 5: [4, 0, 6], 6: [5, 0, 7], 7: [8, 0, 6], 8: [7, 9, 0],
                 9: [0, 10, 8],
                 10: [0, 11, 9], 11: [10, 0, 12], 12: [0, 11, 13], 13: [14, 0, 12], 14: [13, 0, 15], 15: [16, 14, 0],
                 16: [17, 15, 0], 17: [16, 0, 1], 18: [26, 24, 23, 22, 27, 25, 21, 19, 20], 19: [27, 20, 18],
                 20: [19, 21, 18],
                 21: [29, 22, 18, 20], 22: [18, 23, 21, 36], 23: [18, 24, 35, 22, 37], 24: [18, 23, 25, 37],
                 25: [26, 24, 18],
                 26: [18, 25, 27], 27: [19, 18, 26], 28: [36, 32, 34, 31, 35, 29, 33, 30], 29: [21, 30, 28, 36],
                 30: [31, 29, 28], 31: [30, 28, 32], 32: [28, 33, 31], 33: [32, 4, 34, 28], 34: [3, 35, 28, 33],
                 35: [37, 34, 23, 28, 36, 2], 36: [28, 22, 35, 29], 37: [35, 2, 23, 1, 24]}

    g = Graph()

    for a in adj_graph.keys():
        g.add_node(a)
        for b in adj_graph[a]:
            g.add_edge(a, b)

    for a in g.nodes.keys():
        for b in g.get_adjacent_nodes(a):
            print("( %s , %s )" % (a, b))

    def generator(g, a, b):
        for a in g.nodes.keys():
            for b in g.get_adjacent_nodes(a):
                yield ("( %s , %s )" % (a, b))

    x = list(generator(g, a, b))
    print len(x)
    #for element in x: print element
    pairs_per_line = 6
    chunks = len(x) // pairs_per_line
    remainder = len(x) % pairs_per_line
    print chunks, remainder
    for n in xrange(chunks):
        print x[n:n+pairs_per_line]
    print x[-(remainder + 1):-1]