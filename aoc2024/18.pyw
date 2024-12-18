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

a = [eval(x) for x in strs()]
h, w = 6, 6
h, w = 70, 70
corrupt = set()
for j in range(len(a)):
    good = 0
    dist = 0
    q = deque([(0, 0), -1])
    seen = set()
    while len(q) > 1:
        cur = q.popleft()
        if cur == -1:
            dist += 1
            q.append(-1)
            continue
        if cur in seen:
            continue
        seen.add(cur)
        if cur in corrupt:
            continue
        x, y = cur
        if not (0 <= x <= w and 0 <= y <= h):
            continue
        if x == w and y == h:
            good = 1
            break
        d = [-1, 0, 1, 0]
        for i in range(4):
            q.append((x+d[i], y+d[(i+1)%4]))
    if not good:
        print(",".join(map(str, a[j-1])))
        break
    corrupt.add(a[j])
