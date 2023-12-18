import sys, functools, math, re
from itertools import *
from collections import *
sys.setrecursionlimit(9999999)
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

n = 1000
g = [n * ["."] for _ in range(n)]
s = splits()
i, j = n // 2, n // 2
for x in s:
    dir, dist, col = x
    g[i][j] = "#"
    for _ in range(dist):
        if dir == "R":
            j += 1
        elif dir == "L":
            j -= 1
        elif dir == "U":
            i -= 1
        else:
            i += 1
        g[i][j] = "#"
out = 0
seen = set()
q = deque([(0, 0)])
while q:
    i, j = q.popleft()
    if i not in range(n) or j not in range(n) or (i, j) in seen or g[i][j] == "#":
        continue
    seen.add((i, j))
    out += 1
    q.append((i-1, j))
    q.append((i+1, j))
    q.append((i, j-1))
    q.append((i, j+1))
print(n * n - out)
