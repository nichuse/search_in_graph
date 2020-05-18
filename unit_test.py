from generators import (
    RandomGraphGenerator,
    CompleteGraphGenerator,
    WorstForLevitGenerator,
    BestForFordBellmanGraphGenerator,
    WorstForFordBellmanGraphGenerator,
    UndirectedConnectedRandomGraphGenerator
)

from algorithms import (
    Dijkstra,
    FordBellman,
    Levit,
    MinimalPathBetweenSpecifiedVertexes,
    INF
)

from graph import Graph
import time
import unittest


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

    def test_save_graph(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2, 2)
        with open('test_graph.txt', 'w') as graph:
            g.save(graph)

        with open('test_graph.txt', 'r') as graph:
            read_graph = graph.read()
        self.assertEqual(read_graph, str(g))

    def test_read_graph(self):
        g = Graph()
        with open('test_graph.txt', 'r') as graph:
            g.read(graph)
        self.assertEqual('0 1 1\n0 2 2\n', str(g))


class DijkstraTest(unittest.TestCase):
    def test_pathfinder(self):
        g = init_graph()
        self.assertEqual(Dijkstra(g, 0, 1).get_path(), 2)
        self.assertEqual(Dijkstra(g, 1, 0).get_path(), 5)
        self.assertEqual(Dijkstra(g, 3, 15).get_path(), 5)
        self.assertEqual(Dijkstra(g, 3, 12).get_path(), INF)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 2] +
                         [INF for _ in range(14)])

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
        self.assertEqual(FordBellman(g, 0).get_path(), [0, 2] +
                         [INF for _ in range(14)])

    def test_applicability_of_these_graph(self):
        g = init_graph()
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(),
                         True)
        g = Graph()
        g.add_edge(0, 1, -1)
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(),
                         True)
        g.add_edge(1, 2, 1)
        g.add_edge(2, 0, -1)
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(),
                         False)


class LevitTest(unittest.TestCase):
    def test_pathfinder(self):
        g = init_graph()
        p = FordBellman(g, 0, 1)
        self.assertEqual(p.get_path(), 2)
        self.assertEqual(Levit(g, 0).get_path(), [0, 2] +
                         [INF for _ in range(14)])
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
        self.assertEqual(FordBellman(g, 0).applicability_of_these_graph(),
                         False)


class GenerateRandomGraphTest(unittest.TestCase):
    def test_size_graph(self):
        generator = RandomGraphGenerator(4, 4)
        g = generator(2)
        self.assertEqual(g.count_edges(), 4)
        self.assertEqual(g.count_vertex(), 4)
        self.assertEqual(g.max_vertex(), 3)

    def test_determinate(self):
        generator = RandomGraphGenerator(4, 4)
        g = generator(2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 855)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, INF, 855, INF])


class GenerateCompleteGraphTest(unittest.TestCase):
    def test_size_graph(self):
        generator = CompleteGraphGenerator(4, 6)
        g = generator(2)
        self.assertEqual(g.count_edges(), 4 * 3)
        self.assertEqual(g.count_vertex(), 4)
        self.assertEqual(g.max_vertex(), 3)

    def test_determinate(self):
        generator = CompleteGraphGenerator(4, 6)
        g = generator(2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 883)
        self.assertEqual(Dijkstra(g, 0).get_path(),
                         [0, 978, 883, 970])


class GenerateBestForFordBellmanGraphTest(unittest.TestCase):
    def test_size_graph(self):
        generator = BestForFordBellmanGraphGenerator(4, 4)
        g = generator(2)
        self.assertEqual(g.count_edges(), 4)
        self.assertEqual(g.count_vertex(), 4)
        self.assertEqual(g.max_vertex(), 3)

    def test_determinate(self):
        generator = BestForFordBellmanGraphGenerator(6, 7)
        g = generator(2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 883)
        self.assertEqual(Dijkstra(g, 0).get_path(),
                         [0, 978, 883, 970, 869, 57])


class GenerateWorstForFordBellmanGraphTest(unittest.TestCase):
    def test_size_graph(self):
        generator = WorstForFordBellmanGraphGenerator(5, 6)
        g = generator(2)
        self.assertEqual(g.count_edges(), 6)
        self.assertEqual(g.count_vertex(), 5)
        self.assertEqual(g.max_vertex(), 4)

    def test_determinate(self):
        generator = WorstForFordBellmanGraphGenerator(6, 7)
        g = generator(2)
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 1861)
        self.assertEqual(Dijkstra(g, 0).get_path(),
                         [0, 978, 1861, 2831, 3700, 3757])


class GenerateWorstForLevitGraphTest(unittest.TestCase):
    def test_size_graph(self):
        generator = WorstForLevitGenerator(5, 10)
        g = generator()
        self.assertEqual(g.count_edges(), 20)
        self.assertEqual(g.count_vertex(), 5)
        self.assertEqual(g.max_vertex(), 4)

    def test_determinate(self):
        generator = WorstForLevitGenerator(6, 15)
        g = generator()
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 0)
        self.assertEqual(Dijkstra(g, 0).get_path(), [0, 0, 0, 0, 0, 0])


class GenerateUndirectedConnectedRandomGraphTest(unittest.TestCase):
    def test_size_graph(self):
        generator = UndirectedConnectedRandomGraphGenerator(5, 10)
        g = generator()
        self.assertEqual(g.count_edges(), 10)
        self.assertEqual(g.count_vertex(), 5)
        self.assertEqual(g.max_vertex(), 4)

    def test_determinate(self):
        generator = UndirectedConnectedRandomGraphGenerator(6, 15)
        g = generator()
        self.assertEqual(Dijkstra(g, 0, 2).get_path(), 1186)
        self.assertEqual(Dijkstra(g, 0).get_path(),
                         [0, 654, 1186, 553, 288, 722])


class MinimalPathBetweenSpecifiedVertexesTest(unittest.TestCase):
    def test_prim(self):
        g = init_graph()
        edges = g.edge_list.copy()
        for edge in edges:
            g.add_edge(edge.f, edge.s, edge.weight)
        pathfinder = MinimalPathBetweenSpecifiedVertexes(g, [2, 3, 4, 6])
        self.assertEqual(pathfinder.get_min_path(), 112)
        pathfinder.specified_vertexes = [2, 3, 4]
        self.assertEqual(pathfinder.get_min_path(), 1)
        pathfinder.specified_vertexes = [1, 2, 3, 4, 5]
        self.assertGreaterEqual(pathfinder.get_min_path(), INF)

    def test_get_graph_from_specified_vertexes(self):
        g = init_graph()
        pathfinder = MinimalPathBetweenSpecifiedVertexes(g, [2, 3, 4])
        self.assertEqual(len(pathfinder.get_graph_from_specified_vertexes()),
                         3)
        self.assertEqual(pathfinder.get_graph_from_specified_vertexes(),
                         [[INF, INF, INF], [0, INF, 1], [INF, INF, INF]])

    def test_floyd(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(0, 2)
        pathfinder = MinimalPathBetweenSpecifiedVertexes(g, [0])
        self.assertEqual(pathfinder.floyd_algorithm(),
                         [[INF, 1, 1], [INF, INF, 1], [INF, INF, INF]])
        g.add_edge(1, 0)
        pathfinder = MinimalPathBetweenSpecifiedVertexes(g, [0])
        self.assertEqual(pathfinder.floyd_algorithm(),
                         [[2, 1, 1], [1, 2, 1], [INF, INF, INF]])


class ComparisonTimeTest(unittest.TestCase):
    def test_generate_best_and_worst_ford_bellman(self):
        start_time = time.time()
        generator = BestForFordBellmanGraphGenerator(1000, 5000)
        g = generator()
        FordBellman(g, 0).get_path()
        best_time = time.time() - start_time

        start_time = time.time()
        generator = WorstForFordBellmanGraphGenerator(1000, 5000)
        g = generator()
        FordBellman(g, 0).get_path()
        worst_time = time.time() - start_time

        self.assertGreater(worst_time, best_time)

    def test_generate_worst_and_random_levit(self):
        start_time = time.time()
        generator = CompleteGraphGenerator(100, 4950)
        g = generator()
        Levit(g, 0).get_path()
        best_time = time.time() - start_time

        start_time = time.time()
        generator = WorstForLevitGenerator(100, 4950)
        g = generator()
        Levit(g, 0).get_path()
        worst_time = time.time() - start_time

        self.assertGreater(worst_time, best_time)


if __name__ == '__main__':
    unittest.main()
