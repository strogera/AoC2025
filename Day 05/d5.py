with open("input.txt", "r") as inputFile:
    fresh, avail = inputFile.read().split('\n\n')
    fresh = sorted([tuple(map(int, line.split('-'))) for line in fresh.splitlines()])
    
    p1, p2 = 0, 0
    for id in avail.splitlines():
        left, right = 0, len(fresh) - 1
        id = int(id)
        while left <= right:
            mid = (left + right) // 2
            x, y = fresh[mid]
            if id in range(x, y + 1):
                p1 += 1
                break
            if id < x:
                right = mid - 1
            else:
                left = mid + 1

    rangeLen = lambda a, b: b - a + 1
    prevx, prevy = fresh[0]
    for x, y in fresh[1:]:
        if prevx in range(x, y + 1) or x in range(prevx, prevy + 1):
            prevx, prevy = min(x, prevx), max(y, prevy)
        else:
            p2 += rangeLen(prevx, prevy)
            prevx, prevy = x, y
    p2 += rangeLen(prevx, prevy)

    print(p1)
    print(p2)