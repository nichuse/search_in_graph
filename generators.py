from collections import defaultdict
from graph import Graph
import random
MAX_EDGE_COST = 1000
MIN_EDGE_COST = 0


def generate_random_graph(count_vertex, count_edges, seed):
    graph = Graph()
    used = defaultdict(bool)
    random.seed(seed)
    c = 0
    while c < count_edges:
        s = random.randint(0, count_vertex - 1)
        f = random.randint(0, count_vertex - 1)
        if not used[(s, f)] and s != f:
            used[(s, f)] = True
            graph.add_edge(
                s,
                f,
                random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
            )
            c += 1

    return graph


def generate_complete_graph(count_vertex, seed):
    graph = Graph()
    random.seed(seed)
    for i in range(count_vertex):
        for j in range(count_vertex):
            if i != j:
                graph.add_edge(
                    i,
                    j,
                    random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
                )
    return graph


def generate_best_for_ford_bellman(count_vertex, count_edges, seed):
    graph = Graph()
    count_edges = count_edges
    current_vertex = 0
    random.seed(seed)
    while count_edges:
        for vertex in range(current_vertex + 1, count_vertex):
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


def generate_worst_for_ford_bellman(count_vertex, count_edges, seed):
    graph = Graph()
    count_edges = count_edges
    random.seed(seed)
    for v in range(count_vertex - 1):
        graph.add_edge(
            v,
            v + 1,
            random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
        )
        count_edges -= 1
        if count_edges == 0:
            return graph

    current_vertex = count_vertex - 1

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


def generate_worst_for_levit(count_vertex):
    graph = Graph()
    for i in range(1, count_vertex):
        for j in range(i + 1, count_vertex):
            graph.add_edge(i, j, j - i - 1)
            graph.add_edge(j, i, j - i - 1)
    s = 0
    for i in range(count_vertex - 2, 0, -1):
        s += i
        graph.add_edge(0, i, s)
        graph.add_edge(i, 0, s)
    graph.add_edge(0, count_vertex - 1, 0)
    graph.add_edge(count_vertex - 1, 0, 0)

    return graph
