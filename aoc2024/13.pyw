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
    n = 10000000000000
    x += n; y += n
    axay = ax / ay
    q = (x - y * axay) / (bx - by * axay)
    ans = float("inf")
    for q in [math.floor(q), math.ceil(q)]:
        if (x - q * bx) % ax == 0 and (y - q * by) % ay == 0:
            p = (x - q * bx) // ax
            p2 = (y - q * by) // ay
            if p != p2:
                continue
            ans = min(ans, q + 3 * p)
    if ans == float("inf"):
        return 0
    return ans
ans = 0
for x in c:
    ans += go(x)
print(ans)
