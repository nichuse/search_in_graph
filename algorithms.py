from collections import deque
from graph import Graph
import heapq

INF = 10 ** 10


class PathFinder:
    def __init__(self, graph, *args):
        self.graph = graph
        if len(args) > 0:
            self.start = args[0]
        if len(args) > 1:
            self.finish = args[1]
        else:
            self.finish = -1

    def get_path(self, distances):
        if self.finish == -1:
            return distances
        else:
            return distances[self.finish]

    def applicability_of_these_graph(self):
        distances = [INF for _ in range(len(self.graph.adjacency_list))]
        distances[self.graph.start] = 0
        check = True
        for _ in range(len(self.graph.adjacency_list) + 1):
            check = True
            for edge in self.graph.edge_list:
                if distances[edge.s] < INF and distances[edge.s] + edge.dist \
                        < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.dist
                    check = False
        if not check:
            print('Данный алгоритм неприменим к заданному графу')
            return False
        print('Данный алгоритм применим к заданному графу')
        return True

    def pathfinder(self):
        pass


class Dijkstra(PathFinder):
    def pathfinder(self):
        distances = [INF for _ in range(len(self.graph.adjacency_list))]
        distances[self.graph.start] = 0
        q = []
        heapq.heappush(q, (0, self.graph.start))

        while q:
            dist, v = heapq.heappop(q)
            if dist > distances[v]:
                continue

            for u, len_edge in self.graph.adjacency_list[v]:
                if distances[v] + len_edge < distances[u]:
                    distances[u] = distances[v] + len_edge
                    heapq.heappush(q, (distances[u], u))

        return distances

    def applicability_of_these_graph(self):
        for edge in self.graph.edge_list:
            if edge.weight < 0:
                print('Данный алгоритм неприменим к заданному графу')
                return False
        print('Данный алгоритм применим к заданному графу')
        return True


class FordBellman(PathFinder):
    def pathfinder(self):
        distances = [INF for _ in range(len(self.graph.adjacency_list))]
        distances[self.graph.start] = 0

        for _ in range(len(self.graph.adjacency_list)):
            check = True
            for edge in self.graph.edge_list:
                if distances[edge.s] < INF and distances[edge.s] + edge.dist \
                        < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.dist
                    check = False
            if check:
                break
        return distances


class Levit(PathFinder):
    def pathfinder(self):
        distances = [INF for _ in range(len(self.graph.adjacency_list))]
        distances[self.graph.start] = 0
        q1 = deque()
        q2 = deque()
        q1.append(self.graph.start)
        unused = set()
        used = set()
        for v in range(len(self.graph.adjacency_list)):
            if v != self.graph.start:
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
        return distances
