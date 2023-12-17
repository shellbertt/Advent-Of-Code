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
for r, l in splits():
    l = eval(l)
    c = 0
    for i in product(*repeat(range(len(r)), len(l))):
        if list(i) != sorted(i):
            continue
        s = ""
        bad = 0
        for j in range(len(i)):
            if len(s) > i[j]:
                bad = 1
                break
            s = s.ljust(i[j], ".")
            if s and s[-1] == "#":
                bad = 1
                break
            s += l[j] * "#"
        s = s.ljust(len(r), ".")
        if bad:
            continue
        if len(s) == len(r) and all(x == "?" or x == y for x, y in zip(r, s)):
            c += 1
    ans += c
print(ans)
