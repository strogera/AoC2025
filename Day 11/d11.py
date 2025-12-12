from functools import cache
    
with open("input.txt", "r") as inputFile:
    inp = {}
    for line in inputFile.read().splitlines():
        device, output = line.split(':') 
        inp[device] = output.split()

    @cache
    def dfs(cur, dac, fft):
        if cur == 'out':
            return dac and fft
        if cur == 'dac':
            dac = True
        if cur == 'fft':
            fft = True
        return sum(dfs(next, dac, fft) for next in inp[cur])

    p1 = dfs('you', True, True)
    p2 = dfs('svr', False, False)
    print(p1)
    print(p2)
