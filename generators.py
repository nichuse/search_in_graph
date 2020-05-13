from collections import defaultdict
from graph import Graph
import random
MAX_EDGE_COST = 1000
MIN_EDGE_COST = 0


class Generator:
    def __init__(self, count_vertex, count_edges=0):
        self.count_vertex = count_vertex
        self.count_edges = count_edges

    def __call__(self, seed=0):
        return self.generate(seed)

    def generate(self, seed):
        pass


class RandomGraphGenerator(Generator):
    def generate(self, seed):
        graph = Graph()
        used = defaultdict(bool)
        random.seed(seed)
        c = 0
        while c < self.count_edges:
            s = random.randint(0, self.count_vertex - 1)
            f = random.randint(0, self.count_vertex - 1)
            if not used[(s, f)] and s != f:
                used[(s, f)] = True
                graph.add_edge(
                    s,
                    f,
                    random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
                )
                c += 1

        return graph


class BestForFordBellmanGraphGenerator(Generator):
    def generate(self, seed):
        graph = Graph()
        count_edges = self.count_edges
        current_vertex = 0
        random.seed(seed)
        while count_edges:
            for vertex in range(current_vertex + 1, self.count_vertex):
                count_edges -= 1
                graph.add_edge(
                    current_vertex,
                    vertex,
                    random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
                )

                if not count_edges:
                    break
            current_vertex += 1

        return graph


class WorstForFordBellmanGraphGenerator(Generator):
    def generate(self, seed):
        graph = Graph()
        count_edges = self.count_edges
        random.seed(seed)
        for v in range(self.count_vertex - 1):
            graph.add_edge(
                v,
                v + 1,
                random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
            )
            count_edges -= 1
            if count_edges == 0:
                return graph

        current_vertex = self.count_vertex - 1

        while count_edges:
            for vertex in range(current_vertex, 0, -1):
                count_edges -= 1
                graph.add_edge(
                    current_vertex,
                    vertex,
                    random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
                )

                if not count_edges:
                    break
            current_vertex -= 1

        graph.edge_list = graph.edge_list[::-1]
        return graph


class WorstForLevitGenerator(Generator):
    def generate(self, seed):
        graph = Graph()
        for i in range(1, self.count_vertex):
            for j in range(i + 1, self.count_vertex):
                graph.add_edge(i, j, j - i - 1)
                graph.add_edge(j, i, j - i - 1)
        s = 0
        for i in range(self.count_vertex - 2, 0, -1):
            s += i
            graph.add_edge(0, i, s)
            graph.add_edge(i, 0, s)
        graph.add_edge(0, self.count_vertex - 1, 0)
        graph.add_edge(self.count_vertex - 1, 0, 0)

        return graph


class CompleteGraphGenerator(Generator):
    def generate(self, seed):
        graph = Graph()
        random.seed(seed)
        for i in range(self.count_vertex):
            for j in range(self.count_vertex):
                if i != j:
                    graph.add_edge(
                        i,
                        j,
                        random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
                    )
        return graph
