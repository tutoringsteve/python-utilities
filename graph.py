__author__ = 'Steven Sarasin'


class GraphNode:
    def __init__(self, key):
        self.key = key
        # { adjacent_node.source_key : weight from node to adjacent_node }
        self.adjacent_nodes = {}
        # used for Breadth First Search and Path Finding
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
        # source_key : GraphNode dictionary
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
            raise KeyError("source_key not found in nodes")

    def add_edge(self, a, b):
        if a not in self.nodes.keys():
            self.add_node(a)
        if b not in self.nodes.keys():
            self.add_node(b)
        if b not in self.get_adjacent_nodes(a):
            self.nodes[a].add_adjacent_node(b)
            self.total_edges += 1

    def get_adjacent_nodes(self, key):
        if key in self.nodes.keys():
            return self.nodes[key].adjacent_nodes


def BFS(graph, source_key):
    from adts import Queue
    from copy import deepcopy

    graph_deep_copy = deepcopy(graph)
    searched_nodes = set()
    source_node = graph_deep_copy.get_node(source_key)
    for key in graph_deep_copy.nodes.keys():
        node = graph_deep_copy.get_node(key)
        if key is not source_key:
            node.color = "white"
            node.dist = float("inf")
            node.prev = None
    source_node.color = "grey"
    source_node.dist = 0
    source_node.prev = None
    q = Queue()
    q.enqueue(source_node)
    while q.size() > 0:
        node = q.dequeue()
        for child in graph_deep_copy.get_adjacent_nodes(node.get_key()):
            child = graph_deep_copy.get_node(child)
            if child.color is "white":
                child.dist = node.dist + 1
                child.prev = node
                child.color = "grey"
                q.enqueue(child)
        node.color = "black"
        searched_nodes.add(node)
    return searched_nodes


def gen_all_keys_in_dic_with_dist_d(dic_and_d):
    dic, d = dic_and_d
    for key in dic:
        if dic[key] == d:
            yield key


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

    # matches each source_key in the adj_graph to the BFS results when run using that source_key as a source
    source_key_to_BFS_results = {key: (BFS(g, key)) for key in adj_graph}
    for key in source_key_to_BFS_results:
        print key, ":", list(node.get_key() for node in source_key_to_BFS_results[key])
    for key in adj_graph:
        BFS(g, key)

    # matches each source for a BFS in the adj_graph to a dictionary matching each source_key with the dist to the source as computed from the BFS
    key_to_BFS_results_as_key_to_dist = {
        source_key: {node.get_key(): node.dist for node in source_key_to_BFS_results[source_key]}
        for source_key in adj_graph}

    #testing arbitrary nodes for their node.prev tree, which should give shortest paths
    from copy import deepcopy
    searched_nodes = deepcopy(source_key_to_BFS_results[0])
    target_node = searched_nodes.pop()
    #searching for a node with dist 5 for longer path to examine in the search results of BFS on graph with source node key 0
    while target_node.dist != 5:
        target_node = searched_nodes.pop()
    target_node2 = deepcopy(target_node)

    while target_node.prev:
        print "key", target_node.get_key(), "dist", target_node.dist
        target_node = target_node.prev

    def get_path_to_node(node):
        while node:
            yield node.get_key()
            node = node.prev
        return

    path_lst = list(get_path_to_node(target_node2)) #works
    print path_lst
    # uses every source_key in adj_graph as a source for BFS,
    # and matches that source source_key to a dictionary matching
    # the distances from the source to the keys in adj_graph
    # that were that distance from the source source_key

    key_to_BFS_results_as_dist_to_key = {}
    for key in adj_graph:
        dic = key_to_BFS_results_as_key_to_dist[key]
        dic2 = {d: list(gen_all_keys_in_dic_with_dist_d((dic, d))) for d in dic.values()}
        key_to_BFS_results_as_dist_to_key[key] = dic2
    print key_to_BFS_results_as_key_to_dist
    print key_to_BFS_results_as_dist_to_key

    # test dic keys are nodes in the graph and the values are the distance from a source node used in a BFS on the graph
    dic = {0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1,
           17: 1, 18: 4, 19: 5, 20: 5, 21: 5, 22: 4, 23: 3, 24: 3, 25: 4, 26: 5, 27: 5, 28: 3, 29: 4, 30: 4, 31: 4,
           32: 3, 33: 2, 34: 2, 35: 2, 36: 3, 37: 2}
    # testing a dictionary comprehension using a generator
    # for values to accumulate all the nodes in the graph
    # that were a dist d from the source node of a BFS search
    dic2 = {d: list(gen_all_keys_in_dic_with_dist_d((dic, d))) for d in dic.values()}
    # print dic2
