import os
import time
from collections import deque

def main(part):

    garden = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while len(line := f.readline()) != 0:
            line = list(line.strip())
            garden.append(line)

    tot_price = 0
    regions = find_regions(garden)
    
    for region in regions:
        i = next(iter(region))
        plot_val = garden[i[1]][i[0]]
        perimeter = (4 * len(region) - find_shared_edges(plot_val, region, garden))
        if part == 1:
            tot_price += len(region) * perimeter
        else:
            tot_sides = perimeter - find_sides(plot_val, region, garden)
            tot_price += len(region) * tot_sides

    return(tot_price)


def find_regions(garden):
    regions = []
    visited = set()
    for y, row in enumerate(garden):
        for x in range(len(row)):
            if (x, y) not in visited:
                connected_region = find_connected_region(x, y, garden)
                visited = visited | connected_region
                regions.append(connected_region)
    return(regions)


def find_connected_region(x, y, garden):
    # Given a point (x,y), find all points in the garden that are connected to (x,y) and share the same plot value
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    connected_region = {(x, y)}
    queue = deque([(x, y)])
    plot_val = garden[y][x]
    while queue:
        for d in directions:
            if (0 <= queue[0][0] + d[0] <= len(garden[0]) - 1) and (0 <= queue[0][1] + d[1] <= len(garden) - 1):
                if garden[queue[0][1] + d[1]][queue[0][0] + d[0]] == plot_val:
                    if (queue[0][0] + d[0], queue[0][1] + d[1]) not in connected_region:
                        connected_region.add((queue[0][0] + d[0], queue[0][1] + d[1]))
                        queue.append((queue[0][0] + d[0], queue[0][1] + d[1]))
        queue.popleft()
    return(connected_region)


def find_shared_edges(plot, coords, garden):
    # A point in a region contributes 4-x sides to the perimiter, where x is the number of adjacent plots of the same value  
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    shared_edges = 0
    for location in coords:
        for d in directions:
            if (0 <= location[0] + d[0] <= len(garden[0]) - 1) and (0 <= location[1] + d[1] <= len(garden) - 1):
                if garden[location[1] + d[1]][location[0] + d[0]] == plot:
                    shared_edges += 1
    return(shared_edges)


def find_sides(plot, region, garden):
    shared_sides = 0
    # Check top
    for pos in region:
        # Plot above is edge of grid or different value
        if pos[1] == 0 or (pos[1] - 1 >= 0 and garden[pos[1] - 1][pos[0]] != plot):
            # Plot to the right is the same value
            if pos[0] + 1 <= len(garden[0]) - 1 and garden[pos[1]][pos[0] + 1] == plot:
                # Plot above and to the right is a different value
                if pos[1] == 0 or garden[pos[1] - 1][pos[0] + 1] != plot:
                    shared_sides += 1
    # Check left
    for pos in region:
        # Plot to the left is edge of grid or different value
        if pos[0] == 0 or (pos[0] - 1 >= 0 and garden[pos[1]][pos[0] - 1] != plot):
            # Plot above is the same value
            if pos[1] - 1 >= 0 and garden[pos[1] - 1][pos[0]] == plot:
                # Plot above and to the left is a different value
                if pos[0] == 0 or garden[pos[1] - 1][pos[0] - 1] != plot:
                    shared_sides += 1
    # Check right
    for pos in region:
        # Plot to the right is edge of grid or different value
        if pos[0] == len(garden) - 1 or (pos[0] + 1 <= len(garden) - 1 and garden[pos[1]][pos[0] + 1] != plot):
            # Plot above is the same value
            if pos[1] - 1 >= 0 and garden[pos[1] - 1][pos[0]] == plot:
                # Plot above and to the right is a different value
                if pos[0] == len(garden) - 1 or garden[pos[1] - 1][pos[0] + 1] != plot:
                    shared_sides += 1
    # Check bottom
    for pos in region:
        # Plot below is edge of grid or different value
        if pos[1] == len(garden) - 1 or (pos[1] + 1 <= len(garden) - 1 and garden[pos[1] + 1][pos[0]] != plot):
            # Plot to the right is the same value
            if pos[0] + 1 <= len(garden[0]) - 1 and garden[pos[1]][pos[0] + 1] == plot:
                # Plot below and to the right is a different value
                if pos[1] == len(garden) - 1 or garden[pos[1] + 1][pos[0] + 1] != plot:
                    shared_sides += 1
    return(shared_sides)

if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
