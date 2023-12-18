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

s = [(["R", "D", "L", "U"][int(c[-2])], int(c[2:7], 16)) for a, b, c in splits()]
n = len(s)
i, j = 0.5, 0.5
clock = []
anti = []
for k in range(len(s)):
    dir, dist = s[k]
    prevdir = s[k-1][0]
    if prevdir == "R":
        if dir == "U":
            cy = i-.5
            cx = j-.5
            ay = i+.5
            ax = j+.5
        elif dir == "D":
            cy = i-.5
            cx = j+.5
            ay = i+.5
            ax = j-.5
    elif prevdir == "L":
        if dir == "U":
            cy = i+.5
            cx = j-.5
            ay = i-.5
            ax = j+.5
        elif dir == "D":
            cy = i+.5
            cx = j+.5
            ay = i-.5
            ax = j-.5
    elif prevdir == "U":
        if dir == "R":
            cy = i-.5
            cx = j-.5
            ay = i+.5
            ax = j+.5
        elif dir == "L":
            cy = i+.5
            cx = j-.5
            ay = i-.5
            ax = j+.5
    elif prevdir == "D":
        if dir == "R":
            cy = i-.5
            cx = j+.5
            ay = i+.5
            ax = j-.5
        elif dir == "L":
            cy = i+.5
            cx = j+.5
            ay = i-.5
            ax = j-.5
    clock.append((cx, cy))
    anti.append((ax, ay))

    if dir == "R":
        j += dist
    elif dir == "L":
        j -= dist
    elif dir == "U":
        i -= dist
    else:
        i += dist

area = lambda p: int(abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(p, p[1:] + p[:1]))) / 2)
print(area(clock))
print(area(anti))
