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
for i in range(m):
    for j in range(n):
        if g[i][j] != "O":
            continue
        for k in range(i-1, -1, -1):
            if g[k][j] in ("#", "O"):
                break 
            g[k][j] = "O"
            g[k+1][j] = "."
ans = 0
for i in range(m):
    for j in range(n):
        if g[i][j] == "O":
            ans += m-i
print(ans)
