from algorithms import (
    Dijkstra,
    FordBellman,
    Levit,
    MinimalPathBetweenSpecifiedVertexes,
)
from graph import Graph
import time
import argparse


GENERATORS = {
    'levit': Levit,
    'dijkstra': Dijkstra,
    'ford-bellman': FordBellman,
    'other': MinimalPathBetweenSpecifiedVertexes,
}


def timer(algorithm, number_of_starts, start=0, end=None):

    start_time = time.time()
    for _ in range(number_of_starts):
        algorithm.pathfinder(start, end)
    end_time = time.time()

    return end_time - start_time


def initiate_graph(filename):
    graph = Graph()
    with open(filename, 'r') as g:
        graph.read(g)

    return graph


def parseargs():
    description = 'Information about algorithm'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-e', action='store', dest='end',
                        type=int, default=None)
    parser.add_argument('-s', action='store', dest='start',
                        type=int, default=0)
    parser.add_argument('-n', action='store', dest='number_of_starts',
                        type=int, default=100)
    parser.add_argument('-an', action='store', dest='algorithm', type=str,
                        choices=['dijkstra', 'ford-bellman', 'levit', 'other'])
    parser.add_argument('-fn', action='store', dest='filename',
                        type=str, default='stdout')

    return parser.parse_args()


if __name__ == '__main__':
    args = parseargs()
    graph = initiate_graph(args.filename)
    time = timer(args.algorithm, args.number_of_starts, args.start, args.end)
