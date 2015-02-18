class Graph(object):
    """Implements a graph data structure"""

    def __init__(self):
        self.graph_dict = {}

    def nodes(self):
        return self.graph_dict.keys()

    def edges(self):
        return [(key, node) for key, value in
                self.graph_dict.iteritems() for node in value]

    def add_node(self, node):
        self.graph_dict[node] = []

    def add_edge(self, node_1, node_2):
        try:
            self.graph_dict[node_1].append(node_2)
        except KeyError:
            self.add_node(node_1)
            self.graph_dict[node_1].append(node_2)
        if node_2 not in self.nodes():
            self.add_node(node_2)

    def del_node(self, node):
        try:
            del self.graph_dict[node]
            for val_list in self.graph_dict.values():
                if node in val_list:
                    val_list.remove(node)
        except KeyError:
            raise KeyError("Node not found")

    def del_edge(self, node_1, node_2):
        try:
            self.graph_dict[node_1].remove(node_2)
        except KeyError:
            raise KeyError("First node not found")
        except ValueError:
            raise ValueError("Edge not found")

    def has_node(self, node):
        return node in self.graph_dict

    def neighbors(self, node):
        try:
            return self.graph_dict[node]
        except KeyError:
            raise KeyError("Node not found")

    def adjacent(self, node_1, node_2):
        if not self.has_node(node_2):
            raise KeyError("Second node not found")
        try:
            return node_2 in self.graph_dict[node_1]
        except KeyError:
            raise KeyError("First node not found")