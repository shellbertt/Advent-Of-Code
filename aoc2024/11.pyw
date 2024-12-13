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

a = Counter(Ints(stdin()))
for _ in range(75):
    b = Counter()
    for x in a:
        if x == 0:
            b[1] += a[x]
        elif len(str(x)) % 2 == 0:
            y = str(x)
            m = int(y[:len(y)//2])
            n = int(y[len(y)//2:])
            b[m] += a[x]
            b[n] += a[x]
        else:
            b[2024 * x] += a[x]
    a = b
print(sum(a.values()))
