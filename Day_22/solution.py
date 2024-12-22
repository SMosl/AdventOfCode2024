import os
import time
from collections import deque
from collections import defaultdict


def main(part):

    secret_numbers = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while len(line := f.readline()) > 0:
            secret_numbers.append(int(line))

    if part == 1:
        secret_generated = defaultdict(int)
        for initial_num in secret_numbers:
            new_num = initial_num
            for _ in range(2000):
                new_num = get_next_num(new_num)
            secret_generated[initial_num] = new_num
        return(sum(secret_generated.values()))
    else:
        sequences = defaultdict(int)
        curr_sequence = deque([], maxlen=4)
        for curr_num in secret_numbers:
            individual_prices = defaultdict(int)
            visited = set()
            for _ in range(2000):
                new_num = get_next_num(curr_num)
                curr_sequence.append((new_num % 10) - (curr_num % 10))
                converted_sequence = tuple(curr_sequence)
                # We only care about the first time each sequence of differences occurs
                if converted_sequence not in visited:
                    visited.add(converted_sequence)
                    individual_prices[converted_sequence] = max(individual_prices[converted_sequence], new_num % 10)
                curr_num = new_num
            for seq, val in individual_prices.items():
                sequences[seq] += val
        return(max(y for x, y in sequences.items() if len(x) == 4))


def get_next_num(old_num):
    new_num = ((old_num * 64) ^ old_num) % 16777216
    new_num = ((new_num // 32) ^ new_num) % 16777216
    new_num = ((new_num * 2048) ^ new_num) % 16777216
    return(new_num)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
