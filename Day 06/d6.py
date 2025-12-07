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
    inp = inputFile.read().splitlines()
    ops = inp[-1].split()
    inp = inp[:-1]
    inpP2 = transpose(inp)
    inp = list(zip(*[map(int, line.split()) for line in inp]))

    p1, p2 = 0, 0
    for i, op in enumerate(ops):
        p1 += sum(inp[i]) if op =='+' else prod(inp[i])
        p2 += sum(inpP2[i]) if op =='+' else prod(inpP2[i])
    print(p1)
    print(p2)