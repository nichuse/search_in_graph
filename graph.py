from collections import deque
import heapq
INF = 10 ** 10


class Edge:
    def __init__(self, s, f, dist):
        self.s = s
        self.f = f
        self.dist = dist

    def __str__(self):
        return f'{self.s} {self.f} {self.dist}'


class Graph:
    def __init__(self, start, edge_list, adjacency_list):
        self.start = start
        self.adjacency_list = adjacency_list
        self.edge_list = edge_list

    def dijkstra(self):
        distances = [INF for _ in range(len(self.adjacency_list))]
        distances[self.start] = 0
        q = []
        heapq.heappush(q, (0, self.start))

        while q:
            dist, v = heapq.heappop(q)
            if dist > distances[v]:
                continue

            for u, len_edge in self.adjacency_list[v]:
                if distances[v] + len_edge < distances[u]:
                    distances[u] = distances[v] + len_edge
                    heapq.heappush(q, (distances[u], u))

        return distances

    def ford_bellman(self):
        distances = [INF for _ in range(len(self.adjacency_list))]
        distances[self.start] = 0

        for a in range(len(self.adjacency_list)):
            check = True
            for edge in self.edge_list:
                if distances[edge.s] < INF and distances[edge.s] + edge.dist < distances[edge.f]:
                    distances[edge.f] = distances[edge.s] + edge.dist
                    check = False
            if check:
                break

        return distances

    def levit(self):
        distances = [INF for _ in range(len(self.adjacency_list))]
        distances[self.start] = 0
        q1 = deque()
        q2 = deque()
        q1.append(self.start)
        unused = set()
        used = set()
        for v in range(len(self.adjacency_list)):
            if v != self.start:
                unused.add(v)
        while q1 or q2:
            if q2:
                u = q2.popleft()
            else:
                u = q1.popleft()
            for v, dist in self.adjacency_list[u]:
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


def edge_list_to_adjacency_list(edge_list, count_vertex):
    adjacency_list = [[] for _ in range(count_vertex)]
    for edge in edge_list:
        adjacency_list[edge.s].append([edge.f, edge.dist])
    for i in range(len(adjacency_list)):
        adjacency_list[i].sort()
    return adjacency_list
