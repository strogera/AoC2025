
with open("input.txt", "r") as inputFile:
    inp = [tuple(map(int, line.split(","))) for line in inputFile.read().splitlines()]

    area = lambda a, b: (abs(a[0] - b[0]) + 1) * abs((a[1] - b[1]) + 1)

    part1, part2 = 0, 0
    for p1 in inp:
        for p2 in inp:
            ar = area(p1, p2)
            part1 = max(part1, ar)

            if ar <= part2:
                continue

            curIndex = 0
            x, y = sorted((p1[0], p2[0])), sorted((p1[1], p2[1]))
            while curIndex < len(inp):
                np1 = inp[curIndex]
                np2 = inp[(curIndex + 1) % len(inp)]
                nx, ny = sorted((np1[0], np2[0])), sorted((np1[1], np2[1]))
                if nx[0] < x[1] and nx[1] > x[0] and ny[0] < y[1] and ny[1] > y[0]:
                    break
                curIndex += 1
            if curIndex >= len(inp):
                part2 = ar
    print(part1)
    print(part2)