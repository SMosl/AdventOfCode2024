import os
import time

def main(part):

    grid = []
    trailhead_coords = set()
    y_i = 0
    solution = 0
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while len(line := f.readline().split()) != 0:
            x_i = [i for i in range(len(line[0])) if line[0][i] == '0']
            grid.append([int(x) for x in list(line[0])])
            trailhead_coords = trailhead_coords | {(x, y_i) for x in x_i}
            y_i += 1
    
    for start in trailhead_coords:
        solution += find_score(grid, start, part)

    return(solution)


def find_score(grid, start, part):
    paths = [[(start[0], start[1])]]
    directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
    visited_peaks = set()
    score = 0
    while paths:
        path = paths.pop(0)
        curr_height = path[-1]
        if grid[curr_height[1]][curr_height[0]] == 9 and ((curr_height not in visited_peaks)or (part == 2)):
            visited_peaks.add(curr_height)
            score += 1
        else:
            for d in directions:
                next_pos = (curr_height[0] + d[0], curr_height[1] + d[1])
                if (0 <= next_pos[0] <= len(grid[0]) - 1) and (0 <= next_pos[1] <= len(grid) - 1):
                    if grid[next_pos[1]][next_pos[0]] == grid[curr_height[1]][curr_height[0]] + 1:
                        paths.append(path + [next_pos])
    return(score)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
