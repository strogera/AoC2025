from math import prod
from itertools import groupby

def transpose(d):
    ret = [int(x) if x.strip() else -1 for x in map(''.join, zip(*d))]
    return [list(group) for key, group in groupby(ret, lambda k: k != -1) if key]

with open("input.txt", "r") as inputFile:
    apply = {'+': sum, '*': prod}
    *inp, ops = inputFile.read().splitlines()
    groupsP2 = transpose(inp)
    groupsP1 = list(zip(*[map(int, line.split()) for line in inp]))

    p1, p2 = 0, 0
    for op, g1, g2 in zip(ops.split(), groupsP1, groupsP2):
        p1 += apply[op](g1)
        p2 += apply[op](g2)
    print(p1)
    print(p2)