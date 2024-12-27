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

s = ["=".join(x.split("->")[::-1]).strip() for x in stdin().replace(":","=").replace("AND","&").replace("XOR","^").replace("OR","|").splitlines()]
z = set()
for x in s:
    try:
        exec(x)
    except:
        s.append(x)
    if x and x[0] == "z":
        z.add(x.split("=")[0])
sz = sorted(z, key=lambda y:int(y[1:]))
b = "".join(map(str, map(eval, sz)))[::-1]
ans = int(b, 2)
print(ans)
