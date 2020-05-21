from algorithms import (
    Dijkstra,
    FordBellman,
    Levit,
    MinimalPathBetweenSpecifiedVertexes,
)
from graph import Graph
import time
import argparse


ALGORITHMS = {
    'levit': Levit,
    'dijkstra': Dijkstra,
    'ford-bellman': FordBellman,
    'other': MinimalPathBetweenSpecifiedVertexes,
}


def timer(algorithm, number_of_starts, start=0, end=None):
    t = []
    for _ in range(number_of_starts):
        start_time = time.time()
        algorithm.pathfinder(start, end)
        end_time = time.time()
        t.append(end_time - start_time)

    return t


def initiate_graph(filename):
    g = Graph()
    with open(filename, 'r') as file:
        g.read(file)

    return g


def parseargs():
    description = 'Information about algorithm'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-e', action='store', dest='end',
                        type=int, default=None)
    parser.add_argument('-s', action='store', dest='start',
                        type=int, default=0)
    parser.add_argument('-n', action='store', dest='number_of_starts',
                        type=int, default=101)
    parser.add_argument('-a', '--algorithm-name', action='store', dest='algorithm', type=str,
                        choices=['dijkstra', 'ford-bellman', 'levit', 'other'])
    parser.add_argument('-f', '--file-name', action='store', dest='filename',
                        type=str)

    return parser.parse_args()


if __name__ == '__main__':
    args = parseargs()
    graph = initiate_graph(args.filename)
    time = timer(ALGORITHMS[args.algorithm](graph), args.number_of_starts, args.start, args.end)
    with open('results.txt', 'a') as r:
        r.write(f"{args.algorithm} {sum(time)} {args.number_of_starts} {' '.join(map(str, time))} \n")
