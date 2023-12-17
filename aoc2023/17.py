import sys, functools, math, re
from itertools import *
from collections import *
from heapq import heappush, heappop
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
m, n = len(g), len(g[0])
seen = [[[n * [False] for _ in range(m)] for _ in range(4)] for _ in range(5)]
q = [(0, 0, 0, 0, 0)]
while q:
    dist, i, j, dir, steps = heappop(q)
    if not (-1 < i < m and -1 < j < n and steps <= 3 and not seen[dir][steps][i][j]):
        continue
    seen[dir][steps][i][j] = 1
    if i == m-1 and j == n-1:
        print(dist)
        break
    if dir != 2 and j < n-1: heappush(q, (dist+g[i][j+1], i, j+1, 1, steps+1 if dir == 1 else 1))
    if dir != 1 and j > 0:   heappush(q, (dist+g[i][j-1], i, j-1, 2, steps+1 if dir == 2 else 1))
    if dir != 4 and i < m-1: heappush(q, (dist+g[i+1][j], i+1, j, 3, steps+1 if dir == 3 else 1))
    if dir != 3 and i > 0:   heappush(q, (dist+g[i-1][j], i-1, j, 4, steps+1 if dir == 4 else 1))

