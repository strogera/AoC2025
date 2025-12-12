from math import prod 

with open("input.txt", "r") as inputFile:
    *shapes, regions = inputFile.read().split('\n\n')
    shapes = [x.splitlines() for x in shapes]
    p1 = 0
    shapeArea = len(shapes[0][0])*len(shapes[0])
    for r in regions.splitlines():
        area, fill = r.split(':')
        p1 += (prod(map(int, area.split('x'))) >= shapeArea*sum(map(int, fill.split())))
    print(p1)