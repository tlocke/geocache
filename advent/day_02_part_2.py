from itertools import count


def compute(prog):
    for pos in count(step=4):
        opcode = prog[pos]
        if opcode == 99:
            break

        o1 = prog[prog[pos + 1]]
        o2 = prog[prog[pos + 2]]
        rpos = prog[pos + 3]

        if opcode == 1:
            val = o1 + o2
        elif opcode == 2:
            val = o1 * o2

        prog[rpos] = val

    return prog[0]


for x in range(100):
    for y in range(100):
        prog = [
            1, x, y, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 1,
            9, 19, 23, 2, 13, 23, 27, 2, 27, 13, 31, 2, 31, 10, 35, 1, 6, 35,
            39, 1, 5, 39, 43, 1, 10, 43, 47, 1, 5, 47, 51, 1, 13, 51, 55, 2,
            55, 9, 59, 1, 6, 59, 63, 1, 13, 63, 67, 1, 6, 67, 71, 1, 71, 10,
            75, 2, 13, 75, 79, 1, 5, 79, 83, 2, 83, 6, 87, 1, 6, 87, 91, 1, 91,
            13, 95, 1, 95, 13, 99, 2, 99, 13, 103, 1, 103, 5, 107, 2, 107, 10,
            111, 1, 5, 111, 115, 1, 2, 115, 119, 1, 119, 6, 0, 99, 2, 0, 14, 0
        ]

        if compute(prog) == 19690720:
            print("Result", x * 100 + y)
