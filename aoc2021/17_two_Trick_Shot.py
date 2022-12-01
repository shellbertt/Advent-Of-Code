from utils import * ; from aocd import data

d = data[13:].split(', ')
x = tuple(map(int, d[0][2:].split('..')))
y = tuple(map(int, d[1][2:].split('..')))

vc = 0
for i in range(68):
    for j in range(-215, 216):         
            if any(x[0] <= (X := i * (i + 1) / 2 - (i - min(t, i)) * (i - min(t, i) + 1) / 2) and X <= x[1] and y[0] <= (Y := sum(j - T for T in range(t))) and Y <= y[1] for t in range(999)): vc += 1

print(vc)
