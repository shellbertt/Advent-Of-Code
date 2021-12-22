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
        low.append((l, i))

def neigh(l, i):
    N = set()
    if l != 0:
        N.add((l - 1, i))
    if l != len(lines) - 1:
        N.add((l + 1, i))
    if i != 0:
        N.add((l, i - 1))
    if i != len(lines[0]) - 1:
        N.add((l, i + 1))
    return N

bS = []
seen = set()
for L in low:
    B = {L}
    BOLD = set()
    while len(B) != len(BOLD):
        for b in B:
            BOLD.add(b)
        newB = set()
        for p in B:
            for n in neigh(p[0], p[1]):
                if int(lines[n[0]][n[1]]) != 9 and n not in seen:
                    newB.add(n)
                    seen.add(n)
        for b in newB:
            B.add(b)
    bS.append(len(B))

bS.sort()
print(bS[-1] * bS[-2] * bS[-3])
