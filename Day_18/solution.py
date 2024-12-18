import os
import time
import networkx as nx

def main(part):
    data = [['.' for _ in range(71)] for _ in range(71)]
    bytes_locations = []

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while(len(line := f.readline()) != 0):
            line = line.strip().split(',')
            bytes_locations.append((int(line[1]), int(line[0])))

    # Part 1 ensures the graph is pathable after the first 1024 bytes
    for b in bytes_locations[:1024]:
        data[b[1]][b[0]] = '#'

    # Create the networkx graph, each '.' is a node with edges to adjacent '.' nodes
    grid = nx.Graph()
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == '.':
                grid.add_node((x, y))

    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]    
    for node in grid.nodes():
        for d in directions:
            if (node[0] + d[0], node[1] + d[1]) in grid.nodes():
                grid.add_edge(node, (node[0] + d[0], node[1] + d[1]))


    if part == 1:
        return(nx.shortest_path_length(grid, (0,0), (70,70)))
    else:
        byte_index = 1024
        while True:
            try:
                nx.shortest_path(grid, (0,0), (70,70))
                grid.remove_node((bytes_locations[byte_index][0], bytes_locations[byte_index][1]))
                byte_index += 1
            except nx.exception.NetworkXNoPath:
                return(bytes_locations[byte_index - 1][::-1])


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
