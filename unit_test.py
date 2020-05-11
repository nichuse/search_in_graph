from generators import *
from algorithms import *
import time
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
        self.assertEqual(len(g.adjacency_list), 2)
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
        self.assertEqual(Dijkstra(g, 1, 0).get_path(), 5)
        self.assertEqual(Dijkstra(g, 3, 15).get_path(), 5)
        self.assertEqual(Dijkstra(g, 3, 12).get_path(), INF)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 2] + [INF for _ in range(14)])

    def test_applicability_of_these_graph(self):
        g = init_graph()
        self.assertEqual(Dijkstra(g, 0).applicability_of_these_graph(), True)
        g = Graph()
        g.add_edge(0, 1, -1)
        self.assertEqual(Dijkstra(g, 0).applicability_of_these_graph(), False)


class FordBellmanTest(unittest.TestCase):
    def test_pathfinder(self):
        g = init_graph()
        p = FordBellman(g, 0, 1)
        self.assertEqual(p.get_path(), 2)
        self.assertEqual(FordBellman(g, 1, 0).get_path(), 5)
        self.assertEqual(FordBellman(g, 3, 15).get_path(), 5)
        self.assertEqual(FordBellman(g, 3, 12).get_path(), INF)
        self.assertEqual(FordBellman(g, 0).get_path(), [0, 2] + [INF for _ in range(14)])

    def test_applicability_of_these_graph(self):
        g = init_graph()
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(), True)
        g = Graph()
        g.add_edge(0, 1, -1)
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(), True)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 0, -1)
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(), False)


class LevitTest(unittest.TestCase):
    def test_pathfinder(self):
        g = init_graph()
        p = FordBellman(g, 0, 1)
        self.assertEqual(p.get_path(), 2)
        self.assertEqual(Levit(g, 0).get_path(), [0, 2] + [INF for _ in range(14)])
        self.assertEqual(Levit(g, 1, 0).get_path(), 5)
        self.assertEqual(Levit(g, 3, 15).get_path(), 5)
        self.assertEqual(Levit(g, 3, 12).get_path(), INF)

    def test_applicability_of_these_graph(self):
        g = init_graph()
        self.assertEqual(Levit(g, 0).applicability_of_these_graph(), True)
        g = Graph()
        g.add_edge(0, 1, -1)
        self.assertEqual(Levit(g, 0).applicability_of_these_graph(), True)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 0, -1)
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(), False)


class GenerateRandomGraphTest(unittest.TestCase):
    def test_size_graph(self):
        g = generate_random_graph(4, 4, 2)
        self.assertEqual(g.count_edges(), 4)
        self.assertEqual(g.count_vertex(), 4)
        self.assertEqual(g.max_vertex(), 3)

    def test_determinate(self):
        g = generate_random_graph(4, 4, 2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 855)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, INF, 855, INF])


class GenerateCompleteGraphTest(unittest.TestCase):
    def test_size_graph(self):
        g = generate_complete_graph(4, 2)
        self.assertEqual(g.count_edges(), 4 * 3)
        self.assertEqual(g.count_vertex(), 4)
        self.assertEqual(g.max_vertex(), 3)

    def test_determinate(self):
        g = generate_complete_graph(4, 2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 883)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 978, 883, 970])


class GenerateBestForFordBellmanGraphTest(unittest.TestCase):
    def test_size_graph(self):
        g = generate_best_for_ford_bellman(4, 4, 2)
        self.assertEqual(g.count_edges(), 4)
        self.assertEqual(g.count_vertex(), 4)
        self.assertEqual(g.max_vertex(), 3)

    def test_determinate(self):
        g = generate_best_for_ford_bellman(6, 7, 2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 883)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 978, 883, 970, 869, 57])


class GenerateWorstForFordBellmanGraphTest(unittest.TestCase):
    def test_size_graph(self):
        g = generate_worst_for_ford_bellman(5, 6, 2)
        self.assertEqual(g.count_edges(), 6)
        self.assertEqual(g.count_vertex(), 5)
        self.assertEqual(g.max_vertex(), 4)

    def test_determinate(self):
        g = generate_worst_for_ford_bellman(6, 7, 2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 1861)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 978, 1861, 2831, 3700, 3757])


class GenerateWorstForLevitGraphTest(unittest.TestCase):
    def test_size_graph(self):
        g = generate_worst_for_levit(5)
        self.assertEqual(g.count_edges(), 20)
        self.assertEqual(g.count_vertex(), 5)
        self.assertEqual(g.max_vertex(), 4)

    def test_determinate(self):
        g = generate_worst_for_levit(6)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 0)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 0, 0, 0, 0, 0])


class ComparisonTimeTest(unittest.TestCase):
    def test_generate_best_and_worst_ford_bellman(self):
        start_time = time.time()
        g = generate_best_for_ford_bellman(1000, 5000, 2)
        FordBellman(g, 0).get_path()
        best_time = time.time() - start_time

        start_time = time.time()
        g = generate_worst_for_ford_bellman(1000, 5000, 2)
        FordBellman(g, 0).get_path()
        worst_time = time.time() - start_time

        self.assertGreater(worst_time, best_time)

    def test_generate_worst_and_random_levit(self):
        start_time = time.time()
        g = generate_complete_graph(100, 2)
        Levit(g, 0).get_path()
        best_time = time.time() - start_time

        start_time = time.time()
        g = generate_worst_for_levit(100)
        Levit(g, 0).get_path()
        worst_time = time.time() - start_time

        self.assertGreater(worst_time, best_time)


if __name__ == '__main__':
    unittest.main()
