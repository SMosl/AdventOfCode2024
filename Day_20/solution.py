import os
import time
from collections import defaultdict


def main(part):

    cheat_duration = (18 * (part - 1)) + 2
    data = []
    i = 0
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while(len(line := f.readline()) != 0):
            row = list(line.strip().replace('#', '█').replace('.', ' '))
            data.append(list(line.strip().replace('#', '█').replace('.', ' ')))
            if 'S' in row:
                start = (row.index('S'), i)
                data[i][row.index('S')] = ' '
            if 'E' in row:
                end = (row.index('E'), i)
                data[i][row.index('E')] = ' '
            i += 1

    path = [start]
    visited = {start}
    while end not in path:
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for d in directions:
            next_pos = (path[-1][0] + d[0], path[-1][1] + d[1])
            if data[next_pos[1]][next_pos[0]] == ' ' and next_pos not in visited:
                path.append(next_pos)
                visited.add(next_pos)

    cheat_scores = get_cheats(path, cheat_duration)
    solution = 0
    for saving, freq in cheat_scores.items():
        if saving > 99:
            solution += freq
    return(solution)


def get_cheats(path, n):

    cheat_scores = defaultdict(int)
    for i, cheat_start in enumerate(path):
        for j, cheat_exit in enumerate(path[i:]):
            if (abs(cheat_exit[0] - cheat_start[0]) + abs(cheat_exit[1] - cheat_start[1])) < n + 1:
               cheat_scores[j - (abs(cheat_exit[0] - cheat_start[0]) + abs(cheat_exit[1] - cheat_start[1]))] += 1

    return(cheat_scores)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
