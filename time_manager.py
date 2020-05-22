from algorithms import (
    Dijkstra,
    FordBellman,
    Levit,
    MinimalPathBetweenSpecifiedVertexes,
)
from graph import Graph
import time
import os
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
    os.chdir(os.getcwd() + '/generated_graphs')
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
    parser.add_argument('-r', '--file_read', action='store', dest='filename_for_read',
                        type=str)
    parser.add_argument('-w', '--file_write', action='store', dest='filename_for_write',
                        type=str)

    return parser.parse_args()


if __name__ == '__main__':
    args = parseargs()
    graph = initiate_graph(args.filename_for_read)
    time = timer(ALGORITHMS[args.algorithm](graph), args.number_of_starts, args.start, args.end)
    os.chdir(os.getcwd()[::-1][os.getcwd()[::-1].find('/'):][::-1] + '/results')
    with open(args.filename_for_write, 'a') as r:
        r.write(f"{args.algorithm} {sum(time)} {args.number_of_starts} {' '.join(map(str, time))} \n")
