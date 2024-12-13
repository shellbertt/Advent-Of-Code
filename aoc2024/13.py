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

c = chunks()
def go(x):
    ax, ay = Ints(x[0])
    bx, by = Ints(x[1])
    x, y = Ints(x[2])
    @functools.cache
    def rec(x, y):
        if x == 0 and y == 0:
            return 0
        elif x < 0 or y < 0:
            return float("inf")
        return min(rec(x-ax, y-ay)+3, rec(x-bx, y-by)+1)
    ans = rec(x, y)
    if ans == float("inf"):
        return 0
    return ans
ans = 0
for x in c:
    ans += go(x)
print(ans)
