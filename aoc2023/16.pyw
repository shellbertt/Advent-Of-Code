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
def go(a, b):
    q = deque([(a, b)])
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
    return (len(set(x[0] for x in seen)))
ans = 0
for i in range(m):
        ans = max(ans, go(complex(0, i), 1))
        ans = max(ans, go(complex(n-1, i), -1))
for j in range(n):
        ans = max(ans, go(complex(j, 0), 1j))
        ans = max(ans, go(complex(j, m-1), -1j))
print(ans)
