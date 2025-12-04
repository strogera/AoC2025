
def getNeighbors(grid, i, j):
    dir = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    ret = []
    for dx, dy in dir:
        if i + dx in range(len(grid)) and j + dy in range(len(grid[i])):
            if grid[i + dx][j + dy] == '@':
                ret.append((i + dx, j + dy))
    return ret

with open("input.txt", "r") as inputFile:
    grid = inputFile.read().splitlines()

    adjCount = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue
            adjCount[(i, j)] = len(getNeighbors(grid, i, j))

    remove = [x for x, y in adjCount.items() if y < 4 and y > -1]
    p1 = len(remove)
    p2 = 0
    while remove:
        p2 += len(remove)
        for i, j in remove:
            adjCount[(i, j)] = -1
            for adj in getNeighbors(grid, i, j):
                adjCount[adj] -= 1 
        remove = [x for x, y in adjCount.items() if y < 4 and y > -1]
    print(p1)
    print(p2)
