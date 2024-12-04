import os
import time

def main(part):
	wordsearch = []
	
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		while(len(line := f.readline()) != 0):
			wordsearch.append(line.strip())

	if part == 1:
		return(part1(wordsearch))
	else:
		return(part2(wordsearch))



def part1(wordsearch):
	
	solution = 0
	# Horizontal
	for row in wordsearch:
		for x in range(len(row) - 3):
			if row[x:x+4] in ('XMAS','SAMX'):
				solution += 1
	# Vertical
	for y in range(len(wordsearch[0]) - 3):
		for x in range(len(wordsearch[0])):
			if wordsearch[y][x] + wordsearch[y+1][x] + wordsearch[y+2][x] + wordsearch[y+3][x] in ('XMAS','SAMX'):
				solution += 1
	# Diagonal (bottom left - top right)
	for y in range(3, len(wordsearch)):
		for x in range(len(wordsearch[0]) - 3):
			if wordsearch[y][x] + wordsearch[y-1][x+1] + wordsearch[y-2][x+2] + wordsearch[y-3][x+3] in ('XMAS','SAMX'):
				solution += 1
	# Diagonal (top left - bottom right)
	for y in range(len(wordsearch) - 3):
		for x in range(len(wordsearch[0]) - 3):
			if wordsearch[y][x] + wordsearch[y+1][x+1] + wordsearch[y+2][x+2] + wordsearch[y+3][x+3] in ('XMAS','SAMX'):
				solution += 1
	
	return(solution)



def part2(wordsearch):
	
	solution = 0
	for y in range(1, len(wordsearch) - 1):
		for x in range(1, len(wordsearch[0]) - 1):
			if (wordsearch[y+1][x-1] + wordsearch[y][x] + wordsearch[y-1][x+1] in ('MAS','SAM')) and \
				(wordsearch[y-1][x-1] + wordsearch[y][x] + wordsearch[y+1][x+1] in ('MAS','SAM')):
				solution += 1
	
	return(solution)



if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
