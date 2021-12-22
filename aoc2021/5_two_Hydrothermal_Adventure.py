from utils import * ; from aocd import lines

vs = [list(map(lambda x: list(map(int, x.split(','))), l.split('->'))) for l in lines if int(l.split('->')[0].split(',')[0]) - int(l.split('->')[1].split(',')[0]) == 0 or int(l.split('->')[0].split(',')[1]) - int(l.split('->')[1].split(',')[1]) == 0]

dvs = [list(map(lambda x: list(map(int, x.split(','))), l.split('->'))) for l in lines if list(map(lambda x: list(map(int, x.split(','))), l.split('->'))) not in vs]

maxX = max([max([int(l[0][0]), int(l[1][0])]) for l in vs])

maxY = max([max([int(l[0][1]), int(l[1][1])]) for l in vs])

flr = []
for i in range(maxY + 1): flr.append((maxX + 1) * [0])

for v in vs:
    for x in range(min(v[0][0], v[1][0]), max(v[0][0], v[1][0]) + 1):
        for y in range(min(v[0][1], v[1][1]), max(v[0][1], v[1][1]) + 1):
            flr[y][x] += 1

for d in dvs:
    x = d[0][0]
    y = d[0][1]
    while min(d[0][0], d[1][0]) <= x and x <= max(d[0][0], d[1][0]) and min(d[0][1], d[1][1]) <= y and y <= max(d[0][1], d[1][1]):
        flr[y][x] += 1
        x += [-1, 1][d[0][0] < d[1][0]]
        y += [-1, 1][d[0][1] < d[1][1]]

print(sum(p >= 2 for l in flr for p in l))
