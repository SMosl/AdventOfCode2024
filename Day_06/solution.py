import os
import time

def main(part):

	solution = 0
	graph = []
	visited_points = set()
	i = -1
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		while(len(line := f.readline()) != 0):
			i += 1
			line = list(line.strip())
			graph.append(line)
			if '^' in line:
				start = (line.index('^'), i)
				visited_points.add(start)

	directions = [(0,-1), (1,0), (0,1), (-1,0)]
	d = 0
	on_map = True
	curr_pos = (start[0], start[1])

	# Run through the simulation once, recording every visited point on the map
	while on_map:
		next_pos = (curr_pos[0] + directions[d][0], curr_pos[1] + directions[d][1])
		if (next_pos[0] < 0) or (next_pos[0] > len(graph[0]) - 1) or (next_pos[1] < 0) or (next_pos[1] > len(graph) - 1):
			on_map = False
		elif graph[next_pos[1]][next_pos[0]] == '#':
			d = (d + 1) % 4
		else:
			visited_points.add(next_pos)
			curr_pos = next_pos

	if part == 1:
		return len(visited_points)
	else:
		visited_points.remove((start[0], start[1]))
		# Only need to consider adding an obstacle on locations visited in part 1
		for point in visited_points:
			on_map = True
			curr_pos = (start[0], start[1])
			visited_points_2 = {(start[0], start[1], 0)}
			d = 0
			graph[point[1]][point[0]] = '#'
			# Traverse the grid, recording the direction travelled in addition to the position in order to identify loops
			while on_map:
				next_pos = (curr_pos[0] + directions[d][0], curr_pos[1] + directions[d][1], d)
				if (next_pos[0], next_pos[1], d) in visited_points_2:
					solution += 1
					on_map = False
				else:
					if (next_pos[0] < 0) or (next_pos[0] > len(graph[0]) - 1) or (next_pos[1] < 0) or (next_pos[1] > len(graph) - 1):
						on_map = False
					elif graph[next_pos[1]][next_pos[0]] == '#':
						d = (d + 1) % 4
					else:
						visited_points_2.add(next_pos)
						curr_pos = next_pos
			# Remember to reset the graph/remove the obstacle
			graph[point[1]][point[0]] = '.'
		
		return solution


if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
