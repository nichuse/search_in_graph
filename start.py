from graph import Graph, edge_list_to_adjacency_list
from generators import Generator
import random
import time


def start_algorithm(number_of_vertex, graph, text):
    print(text)
    print('---')

    g = Graph(0, graph, edge_list_to_adjacency_list(graph, number_of_vertex))

    start_time = time.time()
    g.dijkstra()
    print("Dijkstra algorithm")
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    g.ford_bellman()
    print("Ford-Bellman algorithm")
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    g.levit()
    print("Levit algorithm")
    print("--- %s seconds ---" % (time.time() - start_time))
    print()


if __name__ == '__main__':
    count_vertex = 100
    start_algorithm(count_vertex, Generator(
        count_vertex, count_vertex).generate_worst_for_levit(),
                    'Worst for Levit')

    count_vertex = 1000
    start_algorithm(count_vertex, Generator(
        count_vertex, count_vertex).generate_complete_graph(),
                    'Random complete graph')

    count_vertex = 10000
    count_edges = 500000
    start_algorithm(count_vertex, Generator(
        count_vertex, count_edges, seed_different=1).generate_random_graph(),
                    'Random graph')

    start_algorithm(count_vertex, Generator(
        count_vertex, count_edges).generate_bamboo(),
                    'Bamboo')

    start_algorithm(count_vertex, Generator(
        count_vertex, count_edges, 10).generate_best_for_ford_bellman(),
                    'Best for Ford Bellman')