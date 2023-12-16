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

g = grid()
m, n = len(g), len(g[0])
q = deque([(complex(0, 0), 1)])
seen = set()
while q:
    cur, d = q.popleft()
    j, i = map(int, [cur.real, cur.imag])
    if not (-1 < i < m and -1 < j < n):
        continue
    if (cur, d) in seen:
        continue
    seen.add((cur, d))
    x = g[i][j]
    if x == "/":
        if d == 1:
            q.append((cur - 1j, -1j))
        elif d == 1j:
            q.append((cur - 1, -1))
        elif d == -1:
            q.append((cur + 1j, 1j))
        elif d == -1j:
            q.append((cur + 1, 1))
    elif x == "\\":
        if d == 1:
            q.append((cur + 1j, 1j))
        elif d == 1j:
            q.append((cur + 1, 1))
        elif d == -1:
            q.append((cur - 1j, -1j))
        elif d == -1j:
            q.append((cur - 1, -1))
    elif x == "-":
        if d == 1j:
            q.append((cur - 1, -1))
            q.append((cur + 1, +1))
        elif d == -1j:
            q.append((cur + 1, +1))
            q.append((cur - 1, -1))
        else:
            q.append((cur + d, d))
    elif x == "|":
        if d == 1:
            q.append((cur + 1j, +1j))
            q.append((cur - 1j, -1j))
        elif d == -1:
            q.append((cur + 1j, +1j))
            q.append((cur - 1j, -1j))
        else:
            q.append((cur + d, d))
    elif x == ".":
        q.append((cur + d, d))
print(len(set(x[0] for x in seen)))
