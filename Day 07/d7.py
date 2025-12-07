cache = {}
def dfs(i, j, inp):
    if (i, j) in cache:
        return 0, cache[(i, j)]
    if i not in range(len(inp)):
        return 0, 1
    if j not in range(len(inp)):
        return 0, 0
    p1, p2 = 0, 0
    if inp[i][j] == '^':
        p1, p2 = map(sum, zip(dfs(i, j+1, inp), dfs(i, j-1, inp)))
        p1 += 1
    else:
        p1, p2 = dfs(i+1, j, inp)
    cache[(i, j)] = p2
    return p1, p2

with open("input.txt", "r") as inputFile:
    inp = inputFile.read().splitlines()
    startingPos = (0, 0)
    for i in range(len(inp)):
        if j := inp[i].index('S'):
            startingPos = (i, j)
            break

    p1, p2 = dfs(*startingPos, inp)

    print(p1)
    print(p2)