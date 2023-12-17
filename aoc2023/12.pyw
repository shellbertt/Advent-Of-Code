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
    r = "?".join(5 * [r])
    m = len(r)
    r += "."
    l = 5 * eval(l)
    n = len(l)

    @functools.cache
    def rec(i, j):
        if i >= m:
            return j == n
        if j == n:
            return all(r[x] != "#" for x in range(i, m))
        ans = 0
        for k in range(i, m+1-l[j]):
            if all(r[x] in "#?" for x in range(k, k+l[j])) and r[k+l[j]] != "#":
                x = rec(k+l[j]+1, j+1)
                ans += x
            if r[k] == "#":
                break
        return ans
    x = rec(0, 0)
    ans += x
print(ans)
