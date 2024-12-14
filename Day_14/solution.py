import os
import time
import re
import math

def main(part):

    robot_info = []
    width = 101
    height = 103
    sim_length = 100

    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        while len(line := f.readline()) != 0:
            l = re.findall(r'(-?\d+),(-?\d+)', line)
            robot_info.append((int(l[0][0]), int(l[0][1]), int(l[1][0]), int(l[1][1])))

    final_positions = []
    if part == 1:
        for data in robot_info:
            final_pos = ((data[0] + sim_length * data[2]) % width, (data[1] + sim_length * data[3]) % height)
            final_positions.append(final_pos)
        
        quadrant_counts = [0,0,0,0]
        for pos in final_positions:
            # Top left
            if pos[0] < width//2 and pos[1] < height//2:
                quadrant_counts[0] += 1
            # Top right
            elif pos[0] > width//2 and pos[1] < height//2:
                quadrant_counts[1] += 1
            # Bottom left
            elif pos[0] < width//2 and pos[1] > height//2:
                quadrant_counts[2] += 1
            # Bottom right
            elif pos[0] > width//2 and pos[1] > height//2:
                quadrant_counts[3] += 1

        return(math.prod(quadrant_counts))

    else:
        with open(f"{dir_path}/output.txt", "w") as f2:
            for n in range(10000):
                positions = set()
                diagram = [['.' for _ in range(width)] for _ in range(height)]
                for data in robot_info:
                    pos_x = (data[0] + n * data[2]) % width
                    pos_y = (data[1] + n * data[3]) % height
                    positions.add((pos_x, pos_y))
                    diagram[pos_y][pos_x] = '#'
                if len(positions) == len(robot_info):
                    f2.write(str(n) + '\n')
                    for line in diagram:
                        for val in line:
                            f2.write(val)
                        f2.write('\n')
                    return(n)

if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
