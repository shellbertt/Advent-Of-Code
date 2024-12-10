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
def dfs(i, j, h):
    if not 0 <= i < m or not 0 <= j < n:
        return 0
    if h != g[i][j]:
        return 0
    if h == 9:
        if not seen[i][j]:
            seen[i][j] = True
            return 1
        else:
            return 0
    ans = 0
    d = [-1, 0, 1, 0] 
    for k in range(4):
        ans += dfs(i+d[k], j+d[(k+1)%4], h+1)
    return ans
ans = 0
for i in range(m):
    for j in range(n):
        seen = [[False] * n for _ in range(m)]
        ans += dfs(i, j, 0)
print(ans)
