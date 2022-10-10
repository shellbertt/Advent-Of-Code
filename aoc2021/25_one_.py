from utils import * ; from aocd import data
data='''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>'''

def step(C):
    for i in range(len(C)):
        for j in range(len(C[0])):
            if C[i][j] == '.': continue
            if C[i][j] == '>' and C[i][(j + 1) % len(C[0])] == '.':
                C[i][j] = '.'
                C[i][(j + 1) % len(C[0])] = '>'
    for i in range(len(C)):
        for j in range(len(C[0])):
            if C[i][j] == '.': continue
            if C[i][j] == 'v' and C[(i + 1) % len(C)][j] == '.':
                C[i][j] = '.'
                C[(i + 1) % len(C)][j] = 'v'
    return C

C = [list(d) for d in data.splitlines()]

P = []
i = 0
while C != P:
    P = C
    C = step(C)
    i += 1

print(i)
