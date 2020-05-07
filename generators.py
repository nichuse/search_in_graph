from collections import defaultdict
from graph import Edge
import random
MAX_EDGE_COST = 1000
MIN_EDGE_COST = 0


def generate_random_graph(count_vertex, count_edges, seed):
    used = defaultdict(bool)
    edges = []
    random.seed(seed)
    c = 0
    while c < count_edges:
        s = random.randint(0, count_vertex - 1)
        f = random.randint(0, count_vertex - 1)
        if not used[(s, f)] and s != f:
            used[(s, f)] = True
            edges.append(Edge(s, f, random.randint(MIN_EDGE_COST,
                                                   MAX_EDGE_COST)))
            c += 1

    return edges


def generate_complete_graph(count_vertex, seed):
    edges = []
    random.seed(seed)
    for i in range(count_vertex):
        for j in range(count_vertex):
            if i != j:
                edges.append(Edge(
                    i,
                    j,
                    random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
                ))
    return edges


def generate_best_for_ford_bellman(count_vertex, count_edges, seed):
    edges = []
    count_edges = count_edges
    current_vertex = 0
    random.seed(seed)
    while count_edges:
        for vertex in range(current_vertex + 1, count_vertex):
            count_edges -= 1
            edges.append(Edge(
                current_vertex,
                vertex,
                random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
            ))

            if not count_edges:
                break
        current_vertex += 1

    return edges


def generate_worst_for_ford_bellman(count_vertex, count_edges, seed):
    edges = []
    count_edges = count_edges
    random.seed(seed)
    for v in range(count_vertex - 1):
        edges.append(Edge(v, v + 1, random.randint(
            MIN_EDGE_COST, MAX_EDGE_COST)))
        count_edges -= 1
        if count_edges == 0:
            return edges

    current_vertex = count_vertex - 1

    while count_edges:
        for vertex in range(current_vertex, 0, -1):
            count_edges -= 1
            edges.append(Edge(
                current_vertex,
                vertex,
                random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
            ))

            if not count_edges:
                break
        current_vertex -= 1

    return edges[::-1]


def generate_worst_for_levit(count_vertex):
    edges = []
    for i in range(1, count_vertex):
        for j in range(i + 1, count_vertex):
            edges.append(Edge(i, j, j - i - 1))
            edges.append(Edge(j, i, j - i - 1))
    s = 0
    for i in range(count_vertex - 2, 0, -1):
        s += i
        edges.append(Edge(0, i, s))
        edges.append(Edge(i, 0, s))
    edges.append(Edge(0, count_vertex - 1, 0))
    edges.append(Edge(count_vertex - 1, 0, 0))

    return edges
