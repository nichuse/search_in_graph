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

    def __str__(self):
        return '\n'.join(map(str, self.edge_list))

    def read(self, file):
        for edge in file:
            s, f, w = list(map(int, edge.split()))
            self.add_edge(s, f, w)

    def save(self, file):
        file.write(self.__str__())

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
