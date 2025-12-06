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
m = len(g)
n = len(g[0])
g = [["."] * n, *g, ["."] * n]
m = len(g)
for i in range(m):
    g[i] = ["."] + g[i] + ["."]
n = len(g[0])
ans = 0
progress = 1
while progress == 1:
    progress = 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            if g[i][j] != "@":
                continue
            if sum([g[k][j-1:j+2].count("@") for k in [i-1, i, i+1]]) < 5:
                g[i][j] = "."
                progress = 1
                ans += 1
print(ans)
