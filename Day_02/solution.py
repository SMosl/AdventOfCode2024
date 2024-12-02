import os
import time

def main(part):

	reports = []
	solution = 0
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		while(len(line := f.readline()) != 0):
			reports.append([int(x) for x in line.split()])

	for report in reports:
		if part == 1:
			solution += is_safe(report)
		else:
			if is_safe(report) == 0:
				solution += int(any([is_safe(report[:i] + report[i+1:]) for i in range(len(report))]))
			else:
				solution += 1
	return solution

def is_safe(report):
	# Increasing
	if report[0] < report[1] < report[0] + 4:
		for i in range(len(report) - 2):
			if report[i+1] >= report[i+2]:
				return 0
			elif (report[i+1] + 4) <= report[i+2]:
				return 0
		return 1
	# Decreasing
	elif report[0] > report[1] > report[0] - 4:
		for i in range(len(report) - 2):
			if report[i+1] <= report[i+2]:
				return 0
			elif report[i+1] - 4 >= report[i+2]:
				return 0
		return 1
	# First two items are the same
	else:
		return 0


if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
