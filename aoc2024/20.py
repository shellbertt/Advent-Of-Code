import functools, math, re, sys
from collections import *; from heapq import *; from itertools import *;
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
for sy in range(h):
    for sx in range(w):
        if g[sy][sx] == "S":
            break
    if g[sy][sx] == "S":
        break
def go():
    seen = set()
    q = deque([(sy, sx, 2), -1])
    dist = 0
    while len(q) > 1:
        cur = q.popleft()
        if cur == -1:
            dist += 1
            q.append(-1)
            continue
        y, x, c = cur
        if (y, x) in seen:
            continue
        seen.add((y, x))
        if not (0 <= y < h and 0 <= x < w):
            continue
        if g[y][x] == "#":
            continue
            if c == 0:
                continue
            c -= 1
        if g[y][x] == "E":
            break
        d = [-1, 0, 1, 0]
        for i in range(4):
            q.append((y+d[i], x+d[(i+1)%4], c))
    return dist
honest = go()
ans = 0
save = 38
save = 100
for i in range(h-1):
    for j in range(w-1):
        a = (i, j, i, j+1)
        if g[i][j] == "#" and g[i][j+1] != "#":
            tmp = (g[i][j], g[i][j+1])
            g[i][j], g[i][j+1] = ".."
            if honest - go() >= save:
                ans += 1
            g[i][j], g[i][j+1] = tmp
        b = (i, j, i+1, j)
        if g[i][j] == "#" and g[i+1][j] != "#":
            tmp = (g[i][j], g[i+1][j])
            g[i][j], g[i+1][j] = ".."
            if honest - go() >= save:
                ans += 1
            g[i][j], g[i+1][j] = tmp
print(ans)
