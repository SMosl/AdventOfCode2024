import os
import time
import re
import functools
from collections import defaultdict

def main(part):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        f = f.read().split('\n\n')
        available_towels = frozenset([x for x in f[0].split(', ')])
        designs = {x for x in f[1].split('\n')}

    num_possibilities = defaultdict(int)
    for design in designs:
        num_possibilities[design] = find_possibilities(design, available_towels)

    if part == 1:
        return(sum(x > 0 for x in num_possibilities.values()))
    else:
        return(sum(x for x in num_possibilities.values()))

@functools.cache
def find_possibilities(design, available_towels):

    num_possibilities = 0
    for towel in available_towels:
        if design == towel:
            num_possibilities += 1
        if re.match(towel, design):
            design_remaining = design[len(towel):]
            num_possibilities += find_possibilities(design_remaining, available_towels)

    return(num_possibilities)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
