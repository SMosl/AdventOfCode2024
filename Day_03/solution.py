import os
import time
import re

def main(part):
	solution = 0
	dir_path = os.path.dirname(os.path.realpath(__file__))
	with open(f"{dir_path}/input.txt", "r") as f:
		text = f.read().replace('\n', '')
		if part == 1:
			# Find all occurrences of 'mul(x,y)' where x and y are numbers
			valid_formats = re.findall(r'mul\((\d+)\,(\d+)\)', text)
			for pair in valid_formats:
				solution += int(pair[0]) * int(pair[1])
			return solution
		else:
			text = text.split("don't()")
			# At the beginning of the program, mul instructions are enabled
			first_section = re.findall(r'mul\((\d+)\,(\d+)\)', text[0])
			for pair in first_section:
				solution += int(pair[0]) * int(pair[1])
			# For each section beginning with "don't()", only consider the section after the first "do()"
			for section in text[1:]:
				if 'do()' in section:
					enabled_section = ''.join(section.split("do()")[1:])
					valid_formats = re.findall(r'mul\((\d+)\,(\d+)\)', enabled_section)
					for pair in valid_formats:
						solution += int(pair[0]) * int(pair[1])
			return solution


if __name__ == "__main__":
	start_time = time.time()
	print(f"Part 1 solution: {main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
