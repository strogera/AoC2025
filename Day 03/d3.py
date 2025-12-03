def solution(bank, length):
    num = ''
    fi = 0
    for limit in range(length - 1, -1, -1): 
        n = '0'
        for i in range(fi, len(bank) - limit):
            if n < bank[i]:
                n = bank[i]
                fi = i + 1
        num += n
    return int(num)

with open("input.txt", "r") as inputFile:
    p1, p2 = 0, 0
    for bank in inputFile.read().splitlines():
            p1 += solution(bank, 2)
            p2 += solution(bank, 12)
    print(p1)
    print(p2)