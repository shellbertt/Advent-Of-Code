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
for y in range(m):
    for x in range(n):
        if g[y][x] == "^":
            break
    if g[y][x] == "^":
        break
g[y][x] = "."
def go(a, b):
    tmp = g[a][b]
    g[a][b] = "#"
    d = 0
    seen = set()
    ans = 0
    i, j = y, x
    while i in range(m) and j in range(n):
        if (i, j, d) in seen:
            ans = 1
            break
        seen.add((i, j, d))
        if d == 0:
            if i-1 in range(m):
                if g[i-1][j] != "#":
                    i -= 1
                else:
                    d += 1
            else:
                break
        elif d == 1:
            if j+1 in range(n):
                if g[i][j+1] != "#":
                    j += 1
                else:
                    d += 1
            else:
                break
        elif d == 2:
            if i+1 in range(m):
                if g[i+1][j] != "#":
                    i += 1
                else:
                    d += 1
            else:
                break
        elif d == 3:
            if j-1 in range(n):
                if g[i][j-1] != "#":
                    j -= 1
                else:
                    d = 0
            else:
                break
    g[a][b] = tmp
    return ans
ans = 0
for i in range(m):
    for j in range(n):
        ans += go(i, j)
print(ans)
