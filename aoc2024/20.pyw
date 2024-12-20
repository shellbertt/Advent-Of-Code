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
for y in range(h):
    for x in range(w):
        if g[y][x] == "S":
            sy, sx = y, x
        if g[y][x] == "E":
            ey, ex = y, x
def bfs(y, x):
    q = deque([(y, x), -1])
    dist = 0
    best = [[-1] * w for _ in range(h)]
    while len(q) > 1:
        cur = q.popleft()
        if cur == -1:
            dist += 1
            q.append(-1)
            continue
        y, x = cur
        if not (0 <= y < h and 0 <= x < w):
            continue
        if g[y][x] == "#":
            continue
        if best[y][x] != -1:
            continue
        best[y][x] = dist
        d = [-1, 0, 1, 0]
        for k in range(4):
            q.append((y+d[k], x+d[(k+1)%4]))
    return best
def go(cy, cx):
    seen = set()
    perm = 20
    q = deque([(cy, cx), -1])
    dist = 0
    ans = set()
    while len(q) > 1:
        cur = q.popleft()
        if cur == -1:
            dist += 1
            q.append(-1)
            continue
        if dist > perm:
            break
        y, x = cur
        if not (0 <= y < h and 0 <= x < w):
            continue
        if g[y][x] != "#":
            if from_start[cy][cx]+dist+to_end[y][x] <= honest-save:
                ans.add((cy, cx, y, x))
        if (y, x) in seen:
            continue
        seen.add((y, x))
        d = [-1, 0, 1, 0]
        for k in range(4):
            q.append((y+d[k], x+d[(k+1)%4]))
    return ans
from_start = bfs(sy, sx)
honest = from_start[ey][ex]
to_end = bfs(ey, ex)
ans = set()
save = 72
save = 100
for i in range(h):
    for j in range(w):
        if g[i][j] == "#":
            continue
        ans.update(go(i, j))
print(len(ans))
