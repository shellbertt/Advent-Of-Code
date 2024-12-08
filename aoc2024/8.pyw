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
ans = [[0] * n for _ in range(m)]
def check(i, j, k, l):
    if g[i][j] != g[k][l]:
        return
    yd = abs(i-k)
    xd = abs(j-l)
    if j < l:
        cury, curx = i, j
        while 0 <= cury and 0 <= curx:
            ans[cury][curx] = 1
            curx -= xd
            cury -= yd
        cury, curx = k, l
        while m > cury and n > curx:
            ans[cury][curx] = 1
            curx += xd
            cury += yd
    else:
        cury, curx = i, j
        while 0 <= cury and n > curx:
            ans[cury][curx] = 1
            curx += xd
            cury -= yd
        cury, curx = k, l
        while m > cury and 0 <= curx:
            ans[cury][curx] = 1
            curx -= xd
            cury += yd
for i in range(m):
    for j in range(n):
        if g[i][j] == ".":
            continue
        for l in range(j+1, n):
            check(i, j, i, l)
        for k in range(i+1, m):
            for l in range(n):
                check(i, j, k, l)
print(sum(sum(r) for r in ans))
