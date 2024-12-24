import os
import time
import graphviz
from collections import defaultdict


def main(part):

    wire_values = defaultdict(int)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{dir_path}/manual_input.txt", "r") as f:
        initial_values, gate_connections = f.read().split('\n\n')

    for x in initial_values.split('\n'):
        x = x.split(': ')
        wire_values[x[0]] = int(x[1])

    instructions = [tuple(x.split(' ')[:3] + x.split(' ')[4:]) for x in gate_connections.split('\n')]

    if part == 2:
        dot = graphviz.Digraph('Day24', comment='Day 24 Part 2 Visualisation')
        for j in instructions:
            dot.node(str(j[0]), str(j[0]))
            dot.node(str(j[2]), str(j[2]))
            dot.node(str(j[3]), str(j[3]))
            dot.edge(str(j[0]), str(j[3]), label=j[1])
            dot.edge(str(j[2]), str(j[3]), label=j[1])
        dot.render(directory='doctest-output', view=True)
    else:
        while instructions:
            instruction = next(x for x in instructions if (x[0] in wire_values.keys()) and (x[2] in wire_values.keys()))
            if instruction[1] == 'AND':
                wire_values[instruction[-1]] = wire_values[instruction[0]] & wire_values[instruction[2]]
            elif instruction[1] == 'OR':
                wire_values[instruction[-1]] = wire_values[instruction[0]] | wire_values[instruction[2]]
            elif instruction[1] == 'XOR':
                wire_values[instruction[-1]] = wire_values[instruction[0]] ^ wire_values[instruction[2]]
            instructions.remove(instruction)

        output = sorted([x for x in wire_values.keys() if x.startswith('z')], reverse=True)
        output = ''.join(str(wire_values[y]) for y in output)
        output = int(output, 2)
        if part == 1:
            return(output)


if __name__ == "__main__":
    start_time = time.time()
    print(f"Part 1 solution: {main(1)}")
    print("Part 1 finished in %s seconds" % (time.time() - start_time))
    mid_time = time.time()
    print(f"Part 2 solution: {main(2)}")
    print("Part 2 finished in %s seconds" % (time.time() - mid_time))
