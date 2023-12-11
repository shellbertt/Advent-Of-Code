import sys, functools, math, re
from itertools import *
from collections import *
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"[+-]?\d+", s))
stdin = lambda: sys.stdin.read().rstrip()
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if re.match(r"^[+-]?\d+$", x) else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n + 1, s)]

g = grid()
m = len(g)
n = len(g[0])
exrows = []
excols = []
for i in range(m):
    if all(x == "." for x in g[i]):
        exrows.append(i)
for i in range(n):
    if all(g[j][i] == "." for j in range(m)):
        excols.append(i)

ans = 0
gals = []
for i in range(m):
    for j in range(n):
        if g[i][j] == "#":
            gals.append((i, j))

for i in range(len(gals)):
    y1, x1 = gals[i]
    for j in range(i+1, len(gals)):
        y2, x2 = gals[j]
        for i in range(min(x1, x2), max(x1, x2)):
            ans += 1
            if i in excols:
                ans += 1000000-1
        for i in range(min(y1, y2), max(y1, y2)):
            ans += 1
            if i in exrows:
                ans += 1000000-1

print(ans)
