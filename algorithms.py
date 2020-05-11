from collections import deque
import heapq

INF = 10 ** 10


class PathFinder:
    def __init__(self, graph, start, *args):
        self.graph = graph
        self.start = start
        if len(args) == 1:
            self.finish = args[0]
        else:
            self.finish = -1

    def get_path(self):
        if self.finish == -1:
            return self.pathfinder()
        else:
            return self.pathfinder()[self.finish]

    def applicability_of_these_graph(self):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[self.start] = 0
        check = True
        for _ in range(len(self.graph.adjacency_list) + 1):
            check = True
            for edge in self.graph.edge_list:
                if distances[edge.s] < INF and distances[edge.s] + edge.weight \
                        < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.weight
                    check = False
        if not check:
            return False
        return True

    def pathfinder(self):
        return []


class Dijkstra(PathFinder):
    def pathfinder(self):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[self.start] = 0
        q = []
        heapq.heappush(q, (0, self.start))

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
                return False
        return True


class FordBellman(PathFinder):
    def pathfinder(self):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[self.start] = 0

        for _ in range(len(self.graph.adjacency_list)):
            check = True
            for edge in self.graph.edge_list:
                if distances[edge.s] < INF and distances[edge.s] + edge.weight \
                        < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.weight
                    check = False
            if check:
                break
        return distances


class Levit(PathFinder):
    def pathfinder(self):
        distances = [INF for _ in range(self.graph.max_vertex() + 1)]
        distances[self.start] = 0
        q1 = deque()
        q2 = deque()
        q1.append(self.start)
        unused = set()
        used = set()
        for v in range(len(self.graph.adjacency_list)):
            if v != self.start:
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
