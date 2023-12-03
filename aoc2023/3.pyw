import sys, functools, itertools, math, operator as op, re
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
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

sym = lambda c: c == "*"
g = grid()
gears = defaultdict(list)
ans = 0
for i in range(len(g)):
    before = -1
    for j in range(len(g[0])):
        c = g[i][j]
        if not type(c) is int or j == len(g[0])-1:
            part = 0
            loc = []
            if i > 0:
                for k in range(max(before, 0), j+1):
                    x = g[i-1][k]
                    if sym(x):
                        part = 1
                        loc.append((i-1, k))
            if i < len(g)-1:
                for k in range(max(before, 0), j+1):
                    x = g[i+1][k]
                    if sym(x):
                        part = 1
                        loc.append((i+1, k))
            if before != -1:
                if sym(g[i][before]):
                    part = 1
                    loc.append((i, before))
            if sym(g[i][j]):
                part = 1
                loc.append((i, j))
            if part:
                poss = "".join(map(str, g[i][before+1:j+(type(c) is int)]))
                if poss:
                    for e in loc:
                        gears[e].append(int(poss))
            before = j
for k, v in gears.items():
    if len(v) == 2:
        ans += v[0]*v[1]
print(ans)

