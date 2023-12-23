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

seen = [n * [0] for _ in range(m)]
def dfs(i, j):
    if i == m-1:
        return 0
    seen[i][j] = 1
    ans = - (1 << 55) 
    poss = []
    cur = g[i][j]
    if cur == "v":
        poss.append((i+1, j))
    elif cur == "^":
        poss.append((i-1, j))
    elif cur == ">":
        poss.append((i, j+1))
    elif cur == "<":
        poss.append((i, j-1))
    else:
        poss.append((i+1, j))
        poss.append((i-1, j))
        poss.append((i, j+1))
        poss.append((i, j-1))
    for x, y in poss:
        if x in range(m) and y in range(n) and g[x][y] != "#" and not seen[x][y]:
            ans = max(ans, 1+dfs(x, y))
    seen[i][j] = 0
    return ans

print(dfs(0, j))
