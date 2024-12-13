import os
import time
import re
import sympy as sym

def main(part):

    conversion_error = 10000000000000 * (part - 1)
    solution = 0
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    with open(f"{dir_path}/input.txt", "r") as f:
        f = f.read().split('\n\n')
        
    for group in f:
        instructions = [int(x) for x in re.findall(r"(\d+)", group)]
        x,y = sym.symbols('x,y')
        eq1 = sym.Eq(instructions[0] * x + instructions[2] * y, conversion_error + instructions[4])
        eq2 = sym.Eq(instructions[1] * x + instructions[3] * y, conversion_error + instructions[5])
        result = sym.solve([eq1, eq2], (x, y))
        if type(result[x]) == type(result[y]) == sym.core.numbers.Integer:
            solution += result[x] * 3 + result[y]
    
    return(solution)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
