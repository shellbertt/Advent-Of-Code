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

s = strs()
l = [x.split(":") for x in s]
res = [int(x[0]) for x in l]
inp = [[int(y) for y in x[1].split()] for x in l]
ans = 0
def go(i, x, j):
    if j < 0:
        return 0
    if x == inp[i][j] and j == 0:
        return 1
    if x % inp[i][j] == 0:
        tmp = go(i, x // inp[i][j], j-1)
        if tmp:
            return 1
    if x >= inp[i][j]:
        tmp = go(i, x - inp[i][j], j-1)
        if tmp:
            return 1
    return 0
for i in range(len(res)):
    tmp = go(i, res[i], len(inp[i])-1)
    if tmp:
        ans += res[i]
print(ans)
