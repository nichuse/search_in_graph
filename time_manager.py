from algorithms import (
    Dijkstra,
    FordBellman,
    Levit,
    MinimalPathBetweenSpecifiedVertexes,
)

from generators import RandomListVertexesGenerator
from graph import Graph
import timeit
import time
import os
import argparse


ALGORITHMS = {
    'levit': Levit,
    'dijkstra': Dijkstra,
    'ford-bellman': FordBellman,
    'other': MinimalPathBetweenSpecifiedVertexes,
}


def timer(algorithm):
    t = []
    for _ in range(101):
        tm = timeit.timeit(algorithm.pathfinder, number=1)
        t.append(tm)
        if len(t) > 3 and get_inaccuracy(t) / (sum(t) / len(t)) <= 0.05:
            break
    #print(get_inaccuracy(t) / sum(t) / len(t))
    return sum(t) / len(t), get_inaccuracy(t)


def get_inaccuracy(t):
    medium = sum(t) / len(t)
    s = 0
    for i in t:
        s += (i - medium) ** 2
    return (1 / (len(t) - 1) * s) ** 0.5


def initiate_graph(filename, path):
    g = Graph()
    os.chdir(os.path.join(path, 'generated_graphs'))
    with open(filename, 'r') as file:
        g.read(file)

    return g


def parseargs():
    description = 'Information about algorithm'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-a', '--algorithm-name', action='store',
                        dest='algorithm', type=str,
                        choices=[
                            'dijkstra', 'ford-bellman', 'levit', 'other'
                        ])
    parser.add_argument('-r', '--file_read', action='store',
                        dest='filename_for_read', type=str)
    parser.add_argument('-w', '--file_write', action='store',
                        dest='filename_for_write', type=str)
    parser.add_argument('-p', '--path', action='store',
                        dest='path', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    args = parseargs()
    graph = initiate_graph(args.filename_for_read, args.path)
    if args.algorithm == 'other':
        vertexes = RandomListVertexesGenerator(graph.max_vertex(), 10)()
        time, inaccuracy = timer(ALGORITHMS[args.algorithm](
            graph,
            vertexes
        ))
    else:
        time, inaccuracy = timer(ALGORITHMS[args.algorithm](graph))
    os.chdir(os.path.join(args.path, 'results'))
    with open(args.filename_for_write, 'a') as r:
        r.write(f"{args.algorithm} {time}"
                f" {inaccuracy} \n")
