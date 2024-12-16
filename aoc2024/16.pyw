import sys, functools, math, re
from itertools import *
from collections import *
from heapq import *
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
h, w = len(g), len(g[0])
for y in range(h):
    for x in range(w):
        if g[y][x] == "S":
            break
    if g[y][x] == "S":
        g[y][x] = "."
        break
d = [-1, 0, 1, 0]
q = [(0, y, x, 1, (y, x))]
seen = [[[0] * 4 for _ in range(w)] for _ in range(h)]
best = 1<<32
pred = defaultdict(set)
q2 = []
while len(q):
    dist, y, x, i, prev = heappop(q)
    cur = (y, x, i)
    if dist > best:
        break
    if g[y][x] == "#":
        continue
    pred[cur].add(prev)
    if g[y][x] == "E":
        best = min(best, dist)
        q2.append((y, x, i))
    if seen[y][x][i]:
        pass
    seen[y][x][i] = 1
    ynew, xnew = y+d[i], x+d[(i+1)%4]
    if not seen[ynew][xnew][i]:
        heappush(q, (dist+1, ynew, xnew, i, cur))
    if not seen[y][x][(i-1)%4]:
        heappush(q, (dist+1000, y, x, (i-1)%4, cur))
    if not seen[y][x][(i+1)%4]:
        heappush(q, (dist+1000, y, x, (i+1)%4, cur))
good = set()
while len(q2):
    cur = q2.pop()
    if cur in good:
        continue
    good.add(cur)
    q2.extend(pred[cur])
good = set([x[:2] for x in good])
print(len(good))
