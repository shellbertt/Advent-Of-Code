import sys, functools, itertools, math, operator as op, re
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
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

ans = 0
S = strs()
have = len(S) * [1]
for i, s in enumerate(S):
    a, b = s.split("|")
    a = Ints(a)[1:]
    b = Ints(b)
    c = sum(x in a for x in b)
    ans += have[i]
    for j in range(i+1, min(len(have), i+c+1)):
        have[j] += have[i]
print(ans)

