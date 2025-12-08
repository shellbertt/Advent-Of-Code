import functools, math, operator, re, sys
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



a = list(map(eval, strs()))
n = len(a)

# Union fund data structure
r = list(range(n))
s = n * [1]
def find(u):
    if r[u] == u:
        return u
    r[u] = max(r[u], find(r[u]))
    return r[u]
def merge(u, v):
    fu = find(u)
    fv = find(v)
    if fu == fv:
        return
    m = max(r[fu], r[fv])
    r[fu] = m
    r[fv] = m
    s[fu] += s[fv]
    s[fv] = s[fu]

# Edges
def dist(p, q):
    a = abs(p[0] - q[0])
    b = abs(p[1] - q[1])
    c = abs(p[2] - q[2])
    return (a ** 2 + b ** 2 + c ** 2) ** .5
e = sorted([(dist(a[i], a[j]), i, j) for i in range(n) for j in range(i+1, n)])

# Unionise!
ans = -1
i = 0
while len(set(find(i) for i in range(n))) > 1:
    ans = a[e[i][1]][0] *  a[e[i][2]][0]
    merge(e[i][1], e[i][2])
    i += 1

print(ans)
