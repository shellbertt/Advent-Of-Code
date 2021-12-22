from utils import * ; from aocd import lines

def danger(I, a):
    return [[(e + a - 1) % 9 + 1 for e in i] for i in I]

w = [[int(s) for s in l] for l in lines]
W = copy.deepcopy(w)
for l in range(len(w)):
    for i in range(1, 5):
        W[l].extend([(e + i - 1) % 9 + 1 for e in w[l]])
b = copy.deepcopy(W)
for i in range(1, 5):
    W.extend(danger(b, i))
pass
        
m = len(W)
n = len(W[0])
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
