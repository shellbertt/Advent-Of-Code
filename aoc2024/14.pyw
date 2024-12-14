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

r = [Ints(line) for line in strs()]
m, n = 103, 101
#m, n = 7, 11
check = 417
for _ in range(7083):
    for i in range(len(r)):
        x, y, vx, vy = r[i]
        r[i][0] = (x+vx+n)%n
        r[i][1] = (y+vy+m)%m
    if _+1 == check:
        g = [[0] * n for _ in range(m)]
        for x, y, vx, vy in r:
            g[y][x] += 1
        for row in g:print(*[" " if tmp == 0 else "#" for tmp in row], sep="")
        print(_+1)
        check += 101
