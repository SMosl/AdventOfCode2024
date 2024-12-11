import os
import time
from collections import defaultdict

def main(part):

    blinks = (50 * (part - 1)) + 25
    stones = defaultdict(lambda: 0)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        for val in f.readline().split():
            stones[val] = 1

    for _ in range(blinks):
        after_iteration = defaultdict(lambda: 0)
        for val in stones.keys():
            if val == '0':
                after_iteration['1'] += stones[val]
            elif len(val) % 2 == 0:
                mid_index = int(len(val)/2)
                after_iteration[max(val[:mid_index].lstrip('0'), '0')] += stones[val]
                after_iteration[max(val[mid_index:].lstrip('0'), '0')] += stones[val]
            else:
                after_iteration[str(int(val) * 2024)] += stones[val]
        stones = after_iteration

    return(sum(stones.values()))


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
