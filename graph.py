class Edge:
    def __init__(self, s, f, weight):
        self.s = s
        self.f = f
        self.weight = weight

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f'{self.s} {self.f} {self.weight}'


class Graph:
    def __init__(self):
        self.adjacency_list = []
        self.edge_list = []

    def read(self, filename):
        with open(filename, 'r') as g:
            for line in g.readlines():
                s, f, w = list(map(int, line.split()))
                self.add_edge(s, f, w)

    def save(self, filename):
        with open(filename, 'w') as g:
            for edge in self.edge_list:
                g.writelines(str(edge) + '\n')

    def add_edge(self, s, f, weight=1):
        while len(self.adjacency_list) <= max(s, f):
            self.adjacency_list.append([])
        self.edge_list.append(Edge(s, f, weight))
        self.adjacency_list[s].append([f, weight])

    def adjacent_vertex(self, v):
        return self.adjacency_list[v]

    def max_vertex(self):
        return max(max(edge.s, edge.f) for edge in self.edge_list)

    def count_vertex(self):
        vertexes = set()
        for edge in self.edge_list:
            vertexes.add(edge.s)
            vertexes.add(edge.f)
        return len(vertexes)

    def count_edges(self):
        return len(self.edge_list)


def edge_list_to_adjacency_list(edge_list, count_vertex):
    adjacency_list = [[] for _ in range(count_vertex)]
    for edge in edge_list:
        adjacency_list[edge.s].append([edge.f, edge.dist])
    for i in range(len(adjacency_list)):
        adjacency_list[i].sort()
    return adjacency_list
