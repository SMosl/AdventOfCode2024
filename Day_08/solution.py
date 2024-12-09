import os
import time
from itertools import combinations

def main(part):

	antennas = {}
	antinodes_1 = set()
	antinodes_2 = set()

	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		lines = f.read().splitlines()
		max_x = len(lines[0])
		max_y = len(lines)
		for y, line in enumerate(lines):
			for i in range(len(line)):
				if line[i] != '.':
					if line[i] in antennas.keys():
						antennas[line[i]].add((i, y))
						antinodes_2.add((i, y))
					else:
						antennas[line[i]] = {(i, y)}
						antinodes_2.add((i, y)) 

	for frequency in antennas:
		for pair in combinations(antennas[frequency], 2):
			dx = pair[0][0] - pair[1][0]
			dy = pair[0][1] - pair[1][1]

			if part == 1:
				if (-1 < pair[1][0] - dx < max_x) and (-1 < pair[1][1] - dy < max_y):
					antinodes_1.add((pair[1][0] - dx, pair[1][1] - dy))
				if (-1 < pair[0][0] + dx < max_x) and (-1 < pair[0][1] + dy < max_y):
					antinodes_1.add((pair[0][0] + dx, pair[0][1] + dy))
			else:
				pos = (pair[0][0], pair[0][1])
				while (-1 < pos[0] < max_x) and (-1 < pos[1] < max_y):
					antinodes_2.add(pos)
					pos = (pos[0] - dx, pos[1] - dy)
				pos = (pair[0][0], pair[0][1])
				while (-1 < pos[0] < max_x) and (-1 < pos[1] < max_y):
					antinodes_2.add(pos)
					pos = (pos[0] + dx, pos[1] + dy)

	if part == 1:
		return len(antinodes_1)
	else:
		return len(antinodes_2)

if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
