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

d = 50
ans = 0
for l in strs():
    start = d
    d = d + int(l[1:]) * (-1 if l[0] == "L" else 1)
    if d not in range(1, 100):
        if d >= 99:
            clicks = d // 100
            ans += clicks
        elif d <= 0:
            clicks = abs((d-1) // 100)
            if start == 0 and d < 0:
                clicks -= 1
            ans += clicks
        d %= 100
print(ans)
