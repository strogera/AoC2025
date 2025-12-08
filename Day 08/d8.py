from math import prod

def findComponent(comps, box):
    for c in comps:
        if box in c:
            return c
    return set()

def distance(a, b):
    return sum((x-y)**2 for x, y in zip(a, b))

with open("input.txt", "r") as inputFile:
    inp = [tuple(int(x) for x in line.split(',')) for line in inputFile.read().splitlines()]
    pairs = set()
    for b1 in inp:
        for b2 in inp:
            if b1 == b2:
                continue
            d = distance(b1, b2)
            pairs.add((d, tuple(sorted([b1, b2]))))
    pairs = sorted(pairs)
    p1 = 0
    cur = pairs.pop(0)[1]
    comp = [set(cur)]
    i = 0
    while len(comp[0]) != len(inp):
        i += 1
        if i == 1000:
            p1 = prod(sorted(list(map(len, comp)))[-3:])

        cur = pairs.pop(0)[1]
        c1, c2 = findComponent(comp, cur[0]), findComponent(comp, cur[1])
        cur = set(cur)
        if not c1 and not c2 :
            comp.append(cur)
        elif c1 and c2:
            comp.remove(c1)
            if c1 != c2:
                comp.remove(c2)
            comp.append(c1 | c2)
        elif c1:
            c1 |= cur
        else:
            c2 |= cur
    print(p1)
    print(prod(x[0] for x in cur))


        

