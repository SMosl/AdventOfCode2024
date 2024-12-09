import os
import time

def main(part):

    # free_space is a list of (x,y) where x is the starting index of the free space and y is the length of the free space
    free_space = []
    # files and compact_files are lists of (x,y,z) where x is the starting index of a file, y is the length of the file block, and z is the ID
    files = []
    compact_files = []
    ind = 0
    val = 0
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        f = f.readline()
        for i, file in enumerate(f):
            if i % 2:
                if int(file) != 0:
                    free_space.append((ind, int(file)))
                ind += int(file)
            else:
                files.insert(0, (ind, int(file), val))
                ind += int(file)
                val += 1

    if part == 1:
        for file in files:
            for i in range(file[1]):
                if file[0] + file[1] - i > free_space[0][0]:
                    compact_files.append((free_space[0][0], 1, file[2]))
                    free_space[0] = (free_space[0][0] + 1, free_space[0][1] - 1)
                    if free_space[0][1] == 0:
                        free_space.pop(0)
                else:
                    compact_files.append((file[0] + file[1] - 1 - i, 1, file[2]))
    else:
        for file in files:
            space_to_take = next((x for x in free_space if x[0] < file[0] and x[1] >= file[1]), None)
            if space_to_take:
                new_index = free_space.index(space_to_take)
                free_space.append((file[0], file[1]))
                compact_files.append((space_to_take[0], file[1], file[2]))
                if space_to_take[1] > file[1]:
                    free_space[new_index] = (space_to_take[0] + file[1], space_to_take[1] - file[1])
                else:
                    free_space.pop(new_index)
            else:
                compact_files.append(file)
  
    solution = 0
    for x in compact_files:
        solution += sum([(x[0] + i) * x[2] for i in range(x[1])])
    return(solution)

if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
