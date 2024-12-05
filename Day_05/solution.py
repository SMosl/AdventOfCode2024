import os
import time
from functools import cmp_to_key

class Day4:
	def __init__(self):		
		self.rules = {}
		self.updates = []
		self.solution_1 = 0
		self.solution_2 = 0


	def main(self, part):
		# Open the file and read the contents
		dir_path = os.path.dirname(os.path.realpath(__file__))
		with open(f"{dir_path}/input.txt", "r") as f:
			raw_input = f.read().split('\n\n')
			# Convert the first section into a dictionary matching a page with all pages that must be printed after
			for rule in raw_input[0].split('\n'):
				rule = rule.split('|')
				if int(rule[0]) in self.rules.keys():
					self.rules[int(rule[0])].add(int(rule[1]))
				else:
					self.rules[int(rule[0])] = {int(rule[1])}
			# Convert the second section into lists of integers
			for line in raw_input[1].split('\n'):
				self.updates.append([int(x) for x in line.split(',')])

		broken_updates = []
		for upd in self.updates:
			for i, val in enumerate(upd):
				# Check if an update has any element that is out of order
				if (val in self.rules.keys()) and (any(x in upd[:i] for x in self.rules[val])):
					if part == 1:
						break
					elif upd not in broken_updates:
						broken_updates.append(upd)
			# If there are no elements out of order, add the middle element to the part 1 solution
			else:
				self.solution_1 += upd[int((len(upd) - 1) / 2)]

		if part == 1:
			return self.solution_1
		else:
			for bupd in broken_updates:
				# Sort the elements in each broken update by the rules dictionary
				sorted_bupd = sorted(bupd, key=cmp_to_key(self.compare))
				self.solution_2 += sorted_bupd[int((len(sorted_bupd) - 1) / 2)]
			return self.solution_2


	def compare(self, x, y):
		if x in self.rules.keys():
			if y in self.rules[x]:
				return -1
			else:
				return 1
		else:
			return 1



if __name__ == "__main__":
	
	sol = Day4()
	start_time = time.time()
	print(f"Part 1 solution: {sol.main(1)}")
	print("Part 1 finished in %s seconds" % (time.time() - start_time))
	mid_time = time.time()
	print(f"Part 2 solution: {sol.main(2)}")
	print("Part 2 finished in %s seconds" % (time.time() - mid_time))
