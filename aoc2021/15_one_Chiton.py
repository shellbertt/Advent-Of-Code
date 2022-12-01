from utils import * ; from aocd import lines

W = [[int(s) for s in l] for l in lines]
m = len(lines)
n = len(lines[0])
temp = []
for i in range(m): temp.append(n * [float('inf')])

temp[0][0] = 1
temp[0][1] = W[0][1]
temp[1][0] = W[1][0]

old = []
while temp != old:
    old = copy.deepcopy(temp)
    for r in range(len(temp)):
        for e in range(len(temp[0])):
            possible = []
            if r > 0: possible.append(temp[r - 1][e])
            if r < len(temp) - 1: possible.append(temp[r + 1][e])
            if e > 0: possible.append(temp[r][e - 1])
            if e < len(temp[0]) - 1: possible.append(temp[r][e + 1])
            temp[r][e] = min([temp[r][e]] + [p + W[r][e] for p in possible])

print(temp[-1][-1])
