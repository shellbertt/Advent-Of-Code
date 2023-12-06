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

seeds, *maps = chunks()
cur = Ints(seeds[0])
nex = []
for c in maps:
    c = c[1:]
    for x in cur:
        mapped = 0
        for b, a, l in map(Ints, c):
            if a <= x <= a+l:
                nex.append(x-a+b)
                mapped = 1
                break
        if not mapped:
            nex.append(x)
    cur = nex
    nex = [] 
print(min(cur))
