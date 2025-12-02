def isInvalid(n):
    n = str(n)
    return n[:len(n)//2] == n[len(n)//2:]

def isInvalidP2(n):
    n = str(n)
    for i in range(1, len(n)//2 + 1):
        if len(n) % i != 0:
            continue
        j = 0
        while j + i <= len(n) and n[j:j + i] == n[:i]:
            j += i
        if j == len(n):
            return True
    return False

with open("input.txt", "r") as inputFile:
    ranges = [map(int, r.split('-')) for r in inputFile.read().strip().split(',')]
    p1 = 0
    p2 = 0
    for x, y in ranges:
        i = x
        while i <= y:
            if isInvalid(i):
                p1 += i
            if isInvalidP2(i):
                p2 += i
            i += 1
    print(p1)
    print(p2)