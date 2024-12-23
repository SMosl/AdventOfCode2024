import os
import time
import networkx as nx
from itertools import combinations
from collections import defaultdict


def main(part):

    graph = nx.Graph()
    t_computers = set()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while len(line := f.readline()) > 0:
            line = line.strip().split('-')
            t_computers = t_computers | set(line)
            graph.add_nodes_from(line)
            graph.add_edge(line[0], line[1])

    if part == 1:
        solution = []
        t_computers = {x for x in t_computers if x[0] == 't'}
        for node in t_computers:
            for i in (first_connection := {x[1] for x in graph.edges(node)}):
                for j in first_connection:
                    if graph.has_edge(node, i) and graph.has_edge(i, j) and graph.has_edge(j, node) and {node, i, j} not in solution:
                        solution.append({node, i, j})
        return(len(solution))
    else:
        max_connected_group = defaultdict(set)
        for node in graph.nodes():
            # find all the subsets of the graph that are connected directly to each node
            for i in range(2, len(list(graph.neighbors(node)))):
                # find all the pairs of nodes in each subset and check if they're all directly connected
                for group in combinations(graph.neighbors(node), i):
                    if all(graph.has_edge(x,y) for x, y in combinations(group, 2)):
                        max_connected_group[i].add(node)
        password = list(max_connected_group[max(max_connected_group.keys())])
        return(','.join(sorted(password)))


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
