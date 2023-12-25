import sys, functools, math, re
sys.setrecursionlimit(999999)
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
for j in range(n):
    if g[0][j] == ".":
        break
ans = - (1 << 55)
q = deque([(0, j, 0, set())])
while q:
    i, j, dist, seen = q.popleft()
    if (i, j) in seen:
        continue
    seen.add((i, j))
    if i == m-1:
        print("found", dist)
        ans = max(ans, dist)
        continue
    poss = []
    poss.append((i+1, j))
    poss.append((i-1, j))
    poss.append((i, j+1))
    poss.append((i, j-1))
    for x, y in poss:
        if x in range(m) and y in range(n) and g[x][y] != "#" and (x, y) not in seen:
            q.append((x, y, dist+1, set(*[seen])))
print(ans)
