from collections import deque
import heapq

INF = 10 ** 10


class PathFinder:
    def __init__(self, graph):
        self.graph = graph

    def applicability_of_these_graph(self):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[0] = 0
        check = True
        for _ in range(len(self.graph.adjacency_list) + 1):
            check = True
            for edge in self.graph.edge_list:
                if distances[edge.s] < INF and distances[edge.s] +\
                        edge.weight < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.weight
                    check = False
        if not check:
            return False
        return True

    def pathfinder(self, start, end=None):
        pass


class Dijkstra(PathFinder):
    def pathfinder(self, start=0, end=None):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, v = heapq.heappop(q)
            if dist > distances[v]:
                continue

            for u, len_edge in self.graph.adjacency_list[v]:
                if distances[v] + len_edge < distances[u]:
                    distances[u] = distances[v] + len_edge
                    heapq.heappush(q, (distances[u], u))

        return distances if end is None else distances[end]

    def applicability_of_these_graph(self):
        for edge in self.graph.edge_list:
            if edge.weight < 0:
                return False
        return True


class FordBellman(PathFinder):
    def pathfinder(self, start=0, end=None):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[start] = 0

        for _ in range(len(self.graph.adjacency_list)):
            check = True
            for edge in self.graph.edge_list:
                if distances[edge.s] < INF and distances[edge.s]\
                        + edge.weight < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.weight
                    check = False
            if check:
                break
        return distances if end is None else distances[end]


class Levit(PathFinder):
    def pathfinder(self, start=0, end=None):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[start] = 0
        q1 = deque()
        q2 = deque()
        q1.append(start)
        unused = set()
        used = set()
        for v in range(len(self.graph.adjacency_list)):
            if v != start:
                unused.add(v)
        while q1 or q2:
            if q2:
                u = q2.popleft()
            else:
                u = q1.popleft()
            for v, dist in self.graph.adjacency_list[u]:
                if v in unused:
                    q1.append(v)
                    unused.remove(v)
                    distances[v] = min(distances[v], distances[u] + dist)
                elif v in used and distances[v] > distances[u] + dist:
                    q2.append(v)
                    used.remove(v)
                    distances[v] = distances[u] + dist
                else:
                    distances[v] = min(distances[v], distances[u] + dist)

            used.add(u)
        return distances if end is None else distances[end]


class MinimalPathBetweenSpecifiedVertexes:
    def __init__(self, graph, specified_vertexes):
        self.graph = graph
        self.specified_vertexes = specified_vertexes

    def floyd_algorithm(self):
        size = self.graph.max_vertex()
        distances = [[INF for _ in range(size + 1)] for _ in range(size + 1)]
        for edge in self.graph.edge_list:
            distances[edge.s][edge.f] = edge.weight
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    if distances[i][k] < INF and distances[k][j] < INF:
                        distances[i][j] = min(
                            distances[i][j],
                            distances[i][k] + distances[k][j]
                        )
        return distances

    def prim_algorithm(self):
        graph = self.get_graph_from_specified_vertexes()
        size = len(self.specified_vertexes)
        used = [False for _ in range(size)]
        min_edges_weight = [INF for _ in range(size)]
        min_edges_weight[0] = 0

        for i in range(size):
            v = -1
            for j in range(size):
                if not used[j] and (v == -1 or min_edges_weight[j]
                                    < min_edges_weight[v]):
                    v = j
            used[v] = True

            for j in range(size):
                min_edges_weight[j] = min(min_edges_weight[j], graph[v][j])
        return min_edges_weight

    def get_min_path(self):
        return sum(self.prim_algorithm())

    def get_graph_from_specified_vertexes(self):
        distances = self.floyd_algorithm()
        size = len(self.specified_vertexes)
        new_graph = [[INF for _ in range(size)] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if j != i:
                    new_graph[i][j] = distances[
                        self.specified_vertexes[i]
                    ][self.specified_vertexes[j]]

        return new_graph
