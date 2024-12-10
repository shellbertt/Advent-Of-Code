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

S = "MAS"
N = len(S)

s = strs()
m, n = len(s), len(s[0])
ans = 0

for i in range(m):
    for j in range(n):
        w = [x[j:j+N] for x in s[i:i+N]]
        if len(w) != N or len(w[0]) != N:
            continue
        for _ in range(4):
            if w[0][0] == w[0][2] == "M" and w[1][1] == "A" and w[2][0] == w[2][2] == "S":
                ans += 1
            w = list(map("".join, zip(*w[::-1])))

print(ans)
