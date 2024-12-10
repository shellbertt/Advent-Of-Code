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

ans = 0
for r in splits():
    a = list(map(int, r))
    safe = 1
    for i in range(1, len(r)):
        if abs(a[i-1] - a[i]) not in [1, 2, 3]:
            safe = 0
            break
    if safe and len(set(a[i] - a[i-1] > 0 for i in range(1, len(r)))) == 1:
        ans += 1
print(ans)
