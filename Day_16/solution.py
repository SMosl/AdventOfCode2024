import os
import time
import networkx as nx

def main(part):

    data = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while(len(line := f.readline()) != 0):
            data.append(list(line.strip().replace('#', '█').replace('.', ' ')))

    graph = nx.DiGraph()
    nodes = set()
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == 'S':
                start = (x, y)
                for d in directions:
                    graph.add_node((x, y, d[0], d[1]))
                nodes.add((x,y))
            elif val == 'E':
                end = (x, y)
                for d in directions:
                    graph.add_node((x, y, d[0], d[1]))
                nodes.add((x,y))
            elif val == ' ':
                for d in directions:
                    graph.add_node((x, y, d[0], d[1]))
                nodes.add((x,y))

    for n in graph.nodes():
        curr_direction = directions.index((n[2], n[3]))
        # anticlockwise
        graph.add_edge(n, (n[0], n[1], directions[(curr_direction + 1) % 4][0], directions[(curr_direction + 1) % 4][1]), weight=1000)
        # clockwise
        graph.add_edge(n, (n[0], n[1], directions[(curr_direction - 1) % 4][0], directions[(curr_direction - 1) % 4][1]), weight=1000)
        # straight forward
        if (n[0] + n[2], n[1] + n[3]) in nodes:
            graph.add_edge(n, (n[0] + n[2], n[1] + n[3], n[2], n[3]), weight=1)

    # the end goal can be facing any direction
    graph.add_node((end[0], end[1]))
    for d in directions:
        graph.add_edge((end[0], end[1], d[0], d[1]), (end[0], end[1]), weight=0)

    if part == 1:
        shortest_path = nx.shortest_path(graph, source=(start[0], start[1], 1, 0), target=(end[0], end[1]), weight='weight')
        return(nx.path_weight(graph, shortest_path, weight='weight'))
    else:
        good_seats = set()
        shortest_paths = nx.all_shortest_paths(graph, source=(start[0], start[1], 1, 0), target=(end[0], end[1]), weight='weight')
        for path in shortest_paths:
            good_seats = good_seats | {(n[0], n[1]) for n in path}
        return(len(good_seats))


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
