import os
import time
from collections import deque
import math

def main(part):

	equations = {}
	solution = 0
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		while(len(line := f.readline()) != 0):
			eq = line.split(':')
			equations[int(eq[0])] = [int(x) for x in eq[1].split()]

	for test_value in equations.keys():
		nums = deque(equations[test_value][1:])
		possibilities = deque([equations[test_value][0]])
		while nums:
			for _ in range(len(possibilities)):
				if part == 1:
					possibilities.extend([possibilities[0] * nums[0], possibilities[0] + nums[0]])
					possibilities.popleft()
				else:
					possibilities.extend([possibilities[0] * nums[0], possibilities[0] + nums[0], possibilities[0] * 10 ** math.floor(math.log10(nums[0]) + 1) + nums[0]])
					possibilities.popleft()
			nums.popleft()
		if test_value in possibilities:
			solution += test_value
	return solution



if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
