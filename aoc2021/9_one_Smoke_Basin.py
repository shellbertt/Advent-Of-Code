from utils import * ; from aocd import lines

# lines ='''2199943210
# 3987894921
# 9856789892
# 8767896789i
# 9899965678'''.splitlines()

low = []
lowCan = []

for l in range(len(lines)):
    for i in range(len(lines[l])):
        if (i == 0 or lines[l][i - 1] > lines[l][i]) and (i == len(lines[l]) - 1 or lines[l][i] < lines[l][i + 1]):
            lowCan.append((l, i))

for p in lowCan:
    l,i=p
    if (l == len(lines) - 1 or lines[l+1][i] > lines[l][i]) and (l == 0 or lines[l-1][i] > lines[l][i]):
        low.append(lines[l][i])

print(sum(int(l) + 1 for l in low))
