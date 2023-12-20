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

ww, p = chunks()
w = defaultdict(list)
for x in ww:
    a, b = x.split("{")
    b = b[:-1].split(",")
    for y in b:
        if ":" not in y:
            y += ":"
        m, n = y.split(":")
        w[a].append((m, n))
ans = 0
for y in p:
    x, m, a, s = Ints(y)
    print(y)
    cur = "in"
    while cur not in ("A", "R"):
        curd = w[cur]
        print(cur, curd)
        for z in curd:
            ss, t = z
            if not t:
                cur = ss
                break
            elif ">" in ss or "<" in ss:
                print(ss, eval(ss))
                if eval(ss):
                    print(cur ,"becomes",t)
                    cur = t
                    break
    print(cur)
    if cur == "A":
        ans += x+m+a+s
print(ans)
