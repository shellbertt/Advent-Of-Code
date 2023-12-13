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
for c in chunks():
    m = len(c)
    n = len(c[0])
    hcans = 0
    vcans = 0
    for i in range(m-1):
        if sum(sum(x != y for x, y in zip(c[i-j], c[i+1+j])) for j in range(min(i, m-2-i)+1)) == 1:
            vcans += 100 * (i+1)
    for i in range(n-1):
        if sum(sum(x != y for x, y in zip([c[k][i-j] for k in range(m)], [c[k][i+1+j] for k in range(m)])) for j in range(min(i, n-2-i)+1)) == 1:
            hcans += (i+1)
    ans += vcans + hcans
print(ans)
