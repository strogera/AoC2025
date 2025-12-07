from math import prod

def transpose(d):
    ret = []
    column = [] 
    for i in range(len(d[0])):
        num = ''.join(d[j][i] for j in range(len(d)))
        if num.strip():
            column.append(int(num))
        else:
            ret.append(column)
            column = []
    ret.append(column)
    return ret

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