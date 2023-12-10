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

g = strs()
m = len(g)
n = len(g[0])
dist = [[-1] * len(g[0]) for _ in range(len(g))]
s = None
for i in range(m):
    for j in range(n):
        if g[i][j] == "S":
            s = (i, j)
q = deque([(s, 0)])
ans = 0
north = "S|LJ"
east = "S-LF"
south = "S|F7"
west = "S-J7"
while q:
    cur, d = q.popleft()
    i, j = cur
    if dist[i][j] != -1:
        continue
    dist[i][j] = d
    ans = d
    if g[i][j] in north and i > 0 and g[i-1][j] in south:
        q.append(((i-1, j), ans+1))
    if g[i][j] in south and i < m-1  and g[i+1][j] in north:
        q.append(((i+1, j), ans+1))
    if g[i][j] in west and j > 0 and g[i][j-1] in east:
        q.append(((i, j-1), ans+1))
    if g[i][j] in east and j < n-1 and g[i][j+1] in west:
        q.append(((i, j+1), ans+1))
g2 = [["`"] * 2 * n for _ in range(2 * m)]
d2 = [[-4] * 2 * n for _ in range(2 * m)]
for i in range(m):
    for j in range(n):
        g2[2*i][2*j] = g[i][j]
        d2[2*i][2*j] = dist[i][j]
        if j < n-1 and dist[i][j] > -1 and dist[i][j+1] > -1 and g[i][j] in east and g[i][j+1] in west:
            g2[2*i][2*j+1] = ","
            d2[2*i][2*j+1] = -5
        if i < m-1 and dist[i][j] > -1 and dist[i+1][j] > -1 and g[i][j] in south and g[i+1][j] in north:
            g2[2*i+1][2*j] = ","
            d2[2*i+1][2*j] = -5
q = deque()
for i in range(2*m):
    q.append((i, 0))
    q.append((i, 2*n-1))
for j in range(2*n):
    q.append((0, j))
    q.append((2*m-1, j))
while q:
    cur = q.popleft()
    i, j = cur
    if i < 0 or i == 2*m or j < 0 or j == 2*n:
        continue
    if d2[i][j] not in [-1, -4]:
        continue
    d2[i][j] = -2
    q.append((i+1, j))
    q.append((i-1, j))
    q.append((i, j+1))
    q.append((i, j-1))
ans = 0
for i in range(2*m):
    for j in range(2*n):
        if d2[i][j] == -1:
            ans += 1
print(ans)
