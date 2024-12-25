import os
import time


def main(part):

    instructions = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        f = f.read().split('\n\n')

    if part == 1:
        grid = [[x for x in y] for y in f[0].split('\n')]
    else:
        grid = []
        for line in f[0].split('\n'):
            row = []
            for val in line:
                if val == '#':
                    row += ['#', '#']
                elif val == '.':
                    row += ['.', '.']
                elif val == 'O':
                    row += ['[', ']']
                elif val == '@':
                    row += ['@', '.']
            grid.append(row)

    instructions = [x for x in f[1] if x != '\n']
    y = next(i for i in range(len(grid)) if '@' in grid[i])
    x = grid[y].index('@')

    if part == 1:
        for instruction in instructions:
            grid, x, y = next_state((x, y), grid, instruction)
    else:
        for instruction in instructions:
            grid, x, y = next_state_part_2((x, y), grid, instruction)

    boxes = []
    for y, line in enumerate(grid):
        for x, val in enumerate(line):
            if val in {'O','['}:
                boxes.append((x,y))
    
    return(sum([100 * n[1] + n[0] for n in boxes]))


def next_state(pos, grid, instruction):
    directions = {
        '^' : (0, -1),
        'v' : (0, 1),
        '<' : (-1, 0),
        '>' : (1, 0)
    }

    next_pos = (pos[0] + directions[instruction][0], pos[1] + directions[instruction][1])
    if grid[next_pos[1]][next_pos[0]] == '.':
        grid[pos[1]][pos[0]] = '.'
        grid[next_pos[1]][next_pos[0]] = '@'
        pos = next_pos
    elif grid[next_pos[1]][next_pos[0]] == 'O':
        match instruction:
            case '^':
                next_non_box = [i for i in range(pos[1] + 1) if grid[pos[1] - i][pos[0]] in {'#', '.'}][0]
                if grid[pos[1] - next_non_box][pos[0]] == '.':
                    grid[pos[1]][pos[0]] = '.'
                    grid[pos[1] - next_non_box][pos[0]] = 'O'
                    pos = next_pos
                    grid[pos[1]][pos[0]] = '@'
            case 'v':
                next_non_box = [i for i in range(len(grid) - pos[1]) if grid[pos[1] + i][pos[0]] in {'#', '.'}][0]
                if grid[pos[1] + next_non_box][pos[0]] == '.':
                    grid[pos[1]][pos[0]] = '.'
                    grid[pos[1] + next_non_box][pos[0]] = 'O'
                    pos = next_pos
                    grid[pos[1]][pos[0]] = '@'
            case '<':
                next_non_box = [i for i in range(1, pos[0] + 1) if grid[pos[1]][pos[0] - i] in {'#', '.'}][0]
                if grid[pos[1]][pos[0] - next_non_box] == '.':
                    grid[pos[1]][pos[0]] = '.'
                    grid[pos[1]][pos[0] - next_non_box] = 'O'
                    pos = next_pos
                    grid[pos[1]][pos[0]] = '@'
            case '>':
                next_non_box = [i for i in range(len(grid[0]) - pos[0]) if grid[pos[1]][pos[0] + i] in {'#', '.'}][0]
                if grid[pos[1]][pos[0] + next_non_box] == '.':
                    grid[pos[1]][pos[0]] = '.'
                    grid[pos[1]][pos[0] + next_non_box] = 'O'
                    pos = next_pos
                    grid[pos[1]][pos[0]] = '@'
    
    return grid, pos[0], pos[1]


def next_state_part_2(pos, grid, instruction):
    directions = {
        '^' : (0, -1),
        'v' : (0, 1),
        '<' : (-1, 0),
        '>' : (1, 0)
    }

    next_pos = (pos[0] + directions[instruction][0], pos[1] + directions[instruction][1])
    if grid[next_pos[1]][next_pos[0]] == '.':
        grid[pos[1]][pos[0]] = '.'
        grid[next_pos[1]][next_pos[0]] = '@'
        pos = next_pos
    elif grid[next_pos[1]][next_pos[0]] in {'[', ']'}:
        match instruction:
            case '^':
                if (positions := find_conected_above(grid, pos)):
                    changes = set()
                    for p, val in [(p, grid[p[1]][p[0]]) for p in positions]:
                        changes.add((p[0],p[1] - 1, val))
                    for x in positions:
                        grid[x[1]][x[0]] = '.'
                    for c in changes:
                        grid[c[1]][c[0]] = c[2]
                    grid[pos[1]][pos[0]] = '.'
                    pos = next_pos
            case 'v':
                if (positions := find_conected_below(grid, pos)):
                    changes = set()
                    for p, val in [(p, grid[p[1]][p[0]]) for p in positions]:
                        changes.add((p[0],p[1] + 1, val))
                    for x in positions:
                        grid[x[1]][x[0]] = '.'
                    for c in changes:
                        grid[c[1]][c[0]] = c[2]
                    grid[pos[1]][pos[0]] = '.'
                    pos = next_pos
            case '<':
                if (positions := find_conected_left(grid, pos)):
                    for p, val in [(p, grid[p[1]][p[0]]) for p in positions]:
                        grid[p[1]][p[0] - 1] = val
                    grid[pos[1]][pos[0]] = '.'
                    pos = next_pos
            case '>':
                if (positions := find_conected_right(grid, pos)):
                    for p, val in [(p, grid[p[1]][p[0]]) for p in positions]:
                        grid[p[1]][p[0] + 1] = val
                    grid[next_pos[1]][next_pos[0]] = '@'
                    grid[pos[1]][pos[0]] = '.'
                    pos = next_pos
    
    return grid, pos[0], pos[1]


def find_conected_left(grid, pos):
    positions = {pos}
    next_val = False
    next_pos = (pos[0] - 1, pos[1])
    
    while next_val != '.':
        next_val = grid[next_pos[1]][next_pos[0]]
        if next_val == ']':
            positions = positions | {next_pos, (next_pos[0] - 1, next_pos[1])}
            next_pos = (next_pos[0] - 2, next_pos[1])
        elif next_val == '#':
            return False

    return(positions)


def find_conected_right(grid, pos):
    positions = {pos}
    next_pos = (pos[0] + 1, pos[1])
    next_val = False

    while next_val != '.':
        next_val = grid[next_pos[1]][next_pos[0]]
        if next_val == '[':
            positions = positions | {next_pos, (next_pos[0] + 1, next_pos[1])}
            next_pos = (next_pos[0] + 2, next_pos[1])
        elif next_val == '#':
            return False
    return(positions)


def find_conected_above(grid, pos):
    positions = {pos}
    top_layer = {pos}
    available_space = 0
    output = {pos}

    while available_space < len(top_layer):
        new_positions = set()
        for p in positions:
            if grid[p[1] - 1][p[0]] == '[':
                new_positions = new_positions | {(p[0], p[1] - 1), (p[0] + 1, p[1] - 1)}
                top_layer = top_layer | {(p[0], p[1] - 1), (p[0] + 1, p[1] - 1)}
                top_layer.remove(p)
            elif grid[p[1] - 1][p[0]] == ']':
                new_positions = new_positions | {(p[0], p[1] - 1), (p[0] - 1, p[1] - 1)}
                top_layer = top_layer | {(p[0], p[1] - 1), (p[0] - 1, p[1] - 1)}
                top_layer.remove(p)
            elif grid[p[1] - 1][p[0]] == '#':
                return(False)
            else:
                available_space += 1
        positions = new_positions
        output = output | new_positions
    return(output)


def find_conected_below(grid, pos):
    positions = {pos}
    bottom_layer = {pos}
    available_space = 0
    output = {pos}

    while available_space < len(bottom_layer):
        new_positions = set()
        for p in positions:
            if grid[p[1] + 1][p[0]] == '[':
                new_positions = new_positions | {(p[0], p[1] + 1), (p[0] + 1, p[1] + 1)}
                bottom_layer = bottom_layer | {(p[0], p[1] + 1), (p[0] + 1, p[1] + 1)}
                bottom_layer.remove(p)
            elif grid[p[1] + 1][p[0]] == ']':
                new_positions = new_positions | {(p[0], p[1] + 1), (p[0] - 1, p[1] + 1)}
                bottom_layer = bottom_layer | {(p[0], p[1] + 1), (p[0] - 1, p[1] + 1)}
                bottom_layer.remove(p)
            elif grid[p[1] + 1][p[0]] == '#':
                return(False)
            else:
                available_space += 1
        positions = new_positions
        output = output | new_positions
    return(output)    


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
