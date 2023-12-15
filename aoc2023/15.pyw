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

def H(s):
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans = ans % 256
    return ans

boxes = [[] for _ in range(256)]
ans = 0
S = stdin()
bans = 0
for s in S.split(","):
    if "=" in s:
        label, val = s.split("=")
        h = H(label)
        found = 0
        for i in range(len(boxes[h])):
            a, b = boxes[h][i]
            if label == a:
                found = 1
                break
        if found:
            boxes[h][i] = (label, val)
        else:
            boxes[h].append((label, val))
    elif "-" in s:
        label, val = s.split("-")
        h = H(label)
        found = 0
        for i in range(len(boxes[h])):
            a, b = boxes[h][i]
            if label == a:
                found = 1
                break
        if found:
            boxes[h].pop(i)
for i, b in enumerate(boxes):
    for j, v in enumerate(b):
        bans += (i+1) * (j+1) * int(v[1])
print(bans)
