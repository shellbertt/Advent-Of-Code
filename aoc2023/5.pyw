import sys, functools, itertools, math, operator as op, re
from collections import *
from time import sleep
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

seeds, *maps = chunks()
seeds = Ints(seeds[0])
cur = []
for a, l in slide(seeds, 2, 2):
    cur.append((a, a+l))
nex = []
for c in maps:
    c = c[1:]
    for x in cur:
        le, ri = x
        if le > ri:
            continue
        mapped = 0
        for b, a, l in map(Ints, c):
            nle = max(le, a)
            nri = min(ri, a+l)
            if nle <= nri:
                nex.append((nle-a+b, nri-a+b))
                if le < a:
                    cur.append((le, nle-1))
                if ri > a+l:
                    cur.append((ri, nri+1))
                mapped = 1
        if not mapped:
            nex.append((le, ri))
    cur = nex
    nex = [] 
print(min(cur)[0])
