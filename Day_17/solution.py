import os
import time
import re
from collections import deque

def main(part):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/input.txt", "r") as f:
        data = f.read()

    input = re.match(r"Register A: (\d+)\s*Register B: (\d+)\s*Register C: (\d+)\s*Program: ([\d,]+)", data).groups()
    instructions = [int(x) for x in input[3].split(',')]
    part_2_substrings = {','.join([str(x) for x in instructions[y:]]) for y in range(1, len(instructions) - 1)}

    if part == 1:
        return(find_output(input[0], instructions))
    else:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # A = 24, 25, 29 and 31 all return "3,0"
        # the next value in the seqence will be found by using A = A * 8 + x for some small x
        queue = deque([24, 25, 29, 31])
        while queue:
            in_A = queue[0]
            queue.popleft()
            for n in range(10):
                next_A = (in_A * 8) + n
                out_A = find_output(next_A, instructions)
                if out_A in part_2_substrings:
                    queue.append(next_A)
                elif out_A == ','.join([str(x) for x in instructions]):
                    return next_A


def find_output(reg_A, instructions):
    A = int(reg_A)
    B = 0
    C = 0

    pointer = 0
    output = []
    while pointer < len(instructions):
        opcode = instructions[pointer]
        operand = instructions[pointer + 1]
        A, B, C, pointer, out = run_instruction(A, B, C, opcode, operand, pointer)
        if type(out) == int:
            output.append(out)

    solution = ''
    for x in output:
        solution += str(x) + ','
    solution = ','.join([str(x) for x in output])
    return(solution)


def run_instruction(A, B, C, opcode, operand, pointer):
    pointer += 2
    out = False

    if 0 <= operand <= 3:
        combo_operand = operand
    elif operand == 4:
        combo_operand = A
    elif operand == 5:
        combo_operand = B
    elif operand == 6:
        combo_operand = C
    elif operand == 7:
        print('Part 1 says this shouldn\'t really happen...')

    match opcode:
        case 0:
            A = A // (2 ** combo_operand)
        case 1:
            B = B ^ operand
        case 2:
            B = combo_operand % 8
        case 3:
            if A != 0:
                pointer = operand
        case 4:
            B = B ^ C
        case 5:
            out = combo_operand % 8
        case 6:
            B = A // (2 ** combo_operand)
        case 7:
            C = A // (2 ** combo_operand)

    return(A, B, C, pointer, out)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
