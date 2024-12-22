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

a = Ints(stdin())
def evolve(x):
    m = 16777216
    x = (x ^ (64 * x)) % m
    x = (x ^ (x // 32)) % m
    x = (x ^ (2048 * x)) % m
    return x
n = len(a)
b = [[a[i] % 10] for i in range(n)]
for i, x in enumerate(a):
    for _ in range(2000):
        x = evolve(x)
        b[i].append(x % 10)
c = [[b[i][j] - b[i][j-1] for j in range(1, len(b[i]))] for i in range(n)]
r = defaultdict(lambda: [None for _ in range(n)])
for i in range(n):
    for j in range(len(c[0])-3):
        w = tuple(c[i][j:j+4])
        if r[w][i] is None:
            r[w][i] = b[i][j+4]
print(max([sum([0 if x is None else x for x in v]) for k, v in r.items()]))
