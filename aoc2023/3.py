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

sym = lambda c: not type(c) is int and c != "."
g = grid()
ans = 0
for i in range(len(g)):
    before = -1
    for j in range(len(g[0])):
        c = g[i][j]
        if not type(c) is int or j == len(g[0])-1:
            part = 0
            if i > 0:
                if any(sym(x) for x in g[i-1][max(before, 0):j+1]):
                    part = 1
            if i < len(g)-1:
                if any(sym(x) for x in g[i+1][max(before, 0):j+1]):
                    part = 1
            if before != -1:
                part |= sym(g[i][before])
            if sym(g[i][j]):
                part = 1
            if part:
                poss = "".join(map(str, g[i][before+1:j+(type(c) is int)]))
                if poss:
                    ans += int(poss)
            before = j

print(ans)

