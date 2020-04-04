from collections import defaultdict
from graph import Edge
import random
MAX_EDGE_COST = 1000
MIN_EDGE_COST = 0


class Generator:
    def __init__(self, count_vertex, count_edges, seed=10, seed_different=0):
        self.count_vertex = count_vertex
        self.count_edges = count_edges
        self.seed = seed
        self.seed_different = seed_different

    def generate_random_graph(self):
        used = defaultdict(bool)
        edges = []
        seed = self.seed
        c = 0
        while c < self.count_edges:
            random.seed(seed)
            s = random.randint(0, self.count_vertex - 1)
            seed += self.seed_different
            random.seed(seed)
            f = random.randint(0, self.count_vertex - 1)
            seed += self.seed_different
            if not used[(s, f)] and s != f:
                used[(s, f)] = True
                edges.append(Edge(s, f, random.randint(MIN_EDGE_COST,
                                                       MAX_EDGE_COST)))
                c += 1

        return edges

    def generate_bamboo(self):
        random.seed(self.seed)
        cost = random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
        edges = []
        for i in range(self.count_vertex - 1):
            edges.append(Edge(i, i + 1, cost))

        return edges[::-1]

    def generate_complete_graph(self):
        edges = []
        seed = self.seed
        for i in range(self.count_vertex):
            for j in range(self.count_vertex):
                if i != j:
                    random.seed(seed)
                    seed += self.seed_different
                    edges.append(Edge(i, j, random.randint(MIN_EDGE_COST,
                                                           MAX_EDGE_COST)))
        return edges

    def generate_best_for_ford_bellman(self):
        edges = []
        count_edges = self.count_edges
        current_vertex = 0
        seed = self.seed
        while count_edges:
            for vertex in range(current_vertex + 1, self.count_vertex):
                count_edges -= 1
                random.seed(seed)
                seed += self.seed_different
                edges.append(Edge(current_vertex, vertex,
                                  random.randint(MIN_EDGE_COST, MAX_EDGE_COST)))
                if not count_edges:
                    break
            current_vertex += 1

        return edges

    def generate_worst_for_levit(self):
        edges = []
        for i in range(1, self.count_vertex):
            for j in range(i + 1, self.count_vertex):
                edges.append(Edge(i, j, j - i - 1))
                edges.append(Edge(j, i, j - i - 1))
        s = 0
        for i in range(self.count_vertex - 2, 0, -1):
            s += i
            edges.append(Edge(0, i, s))
            edges.append(Edge(i, 0, s))
        edges.append(Edge(0, self.count_vertex - 1, 0))
        edges.append(Edge(self.count_vertex - 1, 0, 0))

        return edges
