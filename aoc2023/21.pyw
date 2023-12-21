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

def p1():
    g = grid()
    m = len(g)
    n = len(g[0])
    for i in range(m):
        for j in range(n):
            if g[i][j] == "S":
                break
        if g[i][j] == "S":
            break
    poss = set([(i, j)])
    for _ in range(64):
        new = set()
        for p in poss:
            i, j = p
            if i not in range(m) or j not in range(n) or g[i][j] == "#":
                 continue
            if i+1 < m: new.add((i+1, j)) 
            if i-1 > -1: new.add((i-1, j)) 
            if j+1 < n: new.add((i, j+1)) 
            if j-1 > -1: new.add((i, j-1)) 
        poss = new
        new = set()
    for p in poss:
        i, j = p
        if i not in range(m) or j not in range(n) or g[i][j] == "#":
             continue
        new.add((i, j))
    print(len(new))
            


p1()
