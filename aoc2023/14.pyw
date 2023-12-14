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

def rot(g):
    return list(map(list, zip(*g[::-1])))

def north(g):
    for i in range(m):
        for j in range(n):
            if g[i][j] != "O":
                continue
            for k in range(i-1, -1, -1):
                if g[k][j] in ("#", "O"):
                    break 
                g[k][j] = "O"
                g[k+1][j] = "."

def weight(g):
    ans = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] == "O":
                ans += m-i
    return ans
    
g = grid()
m = len(g)
n = len(g[0])
c = 1000000000
seen = []
for _ in range(1000):
    north(g)
    g = rot(g)
    north(g)
    g = rot(g)
    north(g)
    g = rot(g)
    north(g)
    g = rot(g)
    w = weight(g)
    seen.append(w)
skip = 100
seen = seen[skip:]
for l in range(1, 200):
    if seen[:l] == seen[l:2*l] == seen[2*l:3*l] == seen[3*l:4*l]:
        break
print(seen[(c - skip - 1) % l])
