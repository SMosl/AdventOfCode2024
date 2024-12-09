import os
import time

def main(part):

    solution = part
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        return "test"

if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
