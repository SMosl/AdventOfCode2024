import os
import time
from collections import Counter

def main(part):

	solution = 0
	left_list = []
	right_list = []

	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		while(len(line := f.readline()) != 0):
			vals = line.split()
			left_list.append(int(vals[0]))
			right_list.append(int(vals[1]))

	if part == 1:
		left_list.sort()
		right_list.sort()
		solution = sum([abs(b - a) for a, b in zip(left_list, right_list)])

	else:
		item_counts = Counter(right_list)
		solution = sum([x * item_counts[x] for x in left_list])

	return(solution)

if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
