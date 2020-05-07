from graph import Graph
from generators import *
from algorithms import *
import random
import unittest

START_SEED = 10


def init_graph():
    g = Graph()
    g.add_edge(0, 1, 2)
    g.add_edge(3, 4, 1)
    g.add_edge(3, 2, 0)
    g.add_edge(6, 4, 111)
    g.add_edge(2, 15, 5)
    g.add_edge(1, 0, 5)
    return g


class GraphTests(unittest.TestCase):
    def test_add_edge(self):
        g = Graph()
        g.add_edge(0, 1, 1)
        self.assertEqual(len(g.adjacency_list), 1)
        g.add_edge(1000, 14, -10)
        self.assertEqual(len(g.adjacency_list), 1001)

    def test_count_vertex(self):
        g = init_graph()
        self.assertEqual(g.count_vertex(), 7)
        g.add_edge(11, 12, 1)
        self.assertEqual(g.count_vertex(), 9)

    def test_count_edges(self):
        g = init_graph()
        self.assertEqual(g.count_edges(), 6)
        g.add_edge(100, 123, -100)
        self.assertEqual(g.count_edges(), 7)

    def test_adjacent_vertex(self):
        g = init_graph()
        self.assertEqual(g.adjacent_vertex(0), [[1, 2]])
        self.assertEqual(g.adjacent_vertex(3), [[4, 1], [2, 0]])
        self.assertEqual(g.adjacent_vertex(6), [[4, 111]])
        self.assertEqual(g.adjacent_vertex(2), [[15, 5]])
        self.assertEqual(g.adjacent_vertex(1), [[0, 5]])
        g.add_edge(3, 100, -1)
        self.assertEqual(g.adjacent_vertex(3), [[4, 1], [2, 0], [100, -1]])


class DijkstraTest(unittest.TestCase):
    def test_pathfinder(self):
        g = init_graph()
        self.assertEqual(Dijkstra(g, 0, 1).get_path(), 2)


# class Tests(unittest.TestCase):
#     def _check(self, start, edge_list, count_vertex, ans):
#         graph = Graph(start, edge_list, edge_list_to_adjacency_list(
#                                         edge_list, count_vertex))
#         self.assertEqual(ans, graph.dijkstra())
#         self.assertEqual(ans, graph.ford_bellman())
#         self.assertEqual(ans, graph.levit())
#
#     def test_graph_without_edges(self):
#         self._check(0, [], 1, [0])
#         self._check(1, [], 10, [INF, 0] + [INF for _ in range(8)])
#         self._check(100, [], 101, [INF for _ in range(100)] + [0])
#
#     def test_simple(self):
#         self._check(0, [Edge(0, 1, 1)], 2, [0, 1])
#         self._check(0, [Edge(0, 1, 1)], 2, [0, 1])
#
#     def test_circle(self):
#         self._check(1, [Edge(i, (i + 1) % 3, 2 ** i) for i in range(3)], 3,
#                     [6, 0, 2])
#         self._check(9, [Edge(i, (i + 1) % 10, 2 ** i) for i in range(10)], 10,
#                     [512 + sum(2 ** j for j in range(i)) for i in range(9)] +
#                     [0])
#
#     def test_random_graph(self):
#         gen = Generator(3, 5, seed_different=1)
#         self._check(0, gen.generate_random_graph(), 3, [0, 913, 44])
#
#     def test_complete_graph(self):
#         for count_vertex in range(1, 20):
#             gen = Generator(count_vertex,
#                             count_vertex * (count_vertex + 1) // 2,
#                             START_SEED)
#             answer = [0]
#             for _ in range(count_vertex - 1):
#                 random.seed(START_SEED)
#                 answer.append(random.randint(MIN_EDGE_COST, MAX_EDGE_COST))
#             self._check(0, gen.generate_complete_graph(), count_vertex,
#                         answer)
#
#     def test_best_for_ford_bellman(self):
#         for count_vertex in range(1, 20):
#             gen = Generator(count_vertex, count_vertex - 1,
#                             START_SEED)
#             answer = [0]
#             for _ in range(1, count_vertex):
#                 random.seed(START_SEED)
#                 answer.append(random.randint(MIN_EDGE_COST, MAX_EDGE_COST))
#             self._check(0, gen.generate_best_for_ford_bellman(), count_vertex,
#                         answer)
#
#     def test_worst_for_ford_bellman(self):
#         count_vertex = 1000
#         gen = Generator(count_vertex, count_vertex, START_SEED)
#         bamboo = gen.generate_worst_for_ford_bellman()
#         random.seed(START_SEED)
#         cost = random.randint(MIN_EDGE_COST, MAX_EDGE_COST)
#         self._check(0, bamboo, count_vertex,
#                     [i * cost for i in range(count_vertex)])
#
#     def test_worst_for_levit(self):
#         for count_vertex in range(1, 20):
#             gen = Generator(count_vertex, count_vertex, START_SEED)
#             answer = [0 for _ in range(count_vertex)]
#             self._check(count_vertex - 1, gen.generate_worst_for_levit(),
#                         count_vertex, answer)


if __name__ == '__main__':
    unittest.main()
