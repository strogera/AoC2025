with open("input.txt", "r") as inputFile:
    cur = 50
    p1 = 0
    p2 = 0
    for inp in inputFile.read().split():
        n = int(inp.replace('R', '').replace('L', '-'))
        cur += n
        p2 += abs((cur - (n < 0)) // 100) - (n < 0 and cur - n == 0)
        cur %= 100
        if cur == 0:
            p1 += 1
    print(p1)
    print(p2)