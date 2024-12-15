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

g, move = chunks()
g = list(map(lambda s: list(s.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")), g))
move = "".join(move)
h, w = len(g), len(g[0])
for y in range(h):
    for x in range(w):
        if g[y][x] == "@":
            break
    if g[y][x] == "@":
        g[y][x] = "."
        break
def go(a, b, c, d):
    global g
    tmp = g[a][b]
    g[a][b] = "."
    ans = None
    if g[c][d] == "#":
        ans = (a, b)
    elif g[c][d] == ".":
        ans = (c, d)
    else:
        xd = d-b
        yd = c-a
        if yd == 0:
            if go(c, d, c+yd, d+xd) == (c, d):
                ans = (a, b)
            else:
                ans = (c, d)
        else:
            c2, d2 = c, d+[-1, 1][g[c][d] == "["]
            backup = [_[:] for _ in g]
            if go(c, d, c+yd, d+xd) == (c, d) or go(c2, d2, c2+yd, d2+xd) == (c2, d2):
                g = backup
                ans = (a, b)
            else:
                ans = (c, d)
    g[ans[0]][ans[1]] = tmp
    return ans
for m in move:
    if m == "^":
        y, x = go(y, x, y-1, x)
    elif m == ">":
        y, x = go(y, x, y, x+1)
    elif m == "<":
        y, x = go(y, x, y, x-1)
    elif m == "v":
        y, x = go(y, x, y+1, x)
ans = 0
for y in range(h):
    for x in range(w):
        if g[y][x] == "[":
            ans += 100 * y + x
print(ans)
