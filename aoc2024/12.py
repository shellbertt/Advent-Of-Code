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
m, n = len(g), len(g[0])
seen = [[0] * n for _ in range(m)]
def dfs(y, x, c):
    if not 0 <= y < m or not 0 <= x < n or g[y][x] != c:
        return (0, 1)
    if seen[y][x]:
        return (0, 0)
    seen[y][x] = 1
    a = 1
    p = 0
    d = [-1, 0, 1, 0]
    for i in range(4):
        Y = y+d[i]
        X = x+d[(i+1)%4]
        A, P = dfs(Y, X, c)
        a += A
        p += P
    return (a, p)
ans = 0
for i in range(m):
    for j in range(n):
        a, p = dfs(i, j, g[i][j])
        if a > 0:
            ans += a * p
print(ans)
