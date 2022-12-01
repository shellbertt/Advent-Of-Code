from utils import * ; from aocd import data

parts = data.split('\n\n')
instructions = parts[1].splitlines()
dots = parts[0].splitlines()

maxX = max(int(d.split(',')[0]) for d in dots)
maxY = max(int(d.split(',')[1]) for d in dots)
plot = []
for y in range(maxY + 1):
    plot.append((maxX + 1) * [0])

for d in dots:
    dot = list(map(int, d.split(',')))
    plot[dot[1]][dot[0]] = 1

for n in instructions:
    line = int(n.split('=')[1])
    if 'y' in n:
        for i in range(1, line + 1):
            plot[line - i] = [plot[line - i][j] | plot[line + i][j] for j in range(len(plot[0]))]
        for i in range(line, len(plot)):
            plot.pop(line)
    if 'x' in n:
        for r in range(len(plot)):
            plot[r] = [plot[r][line - e] | plot[r][line + e] for e in range(line, 0, -1)]

for p in plot:
    print(*[[' ', '▮'][e] for e in p])
