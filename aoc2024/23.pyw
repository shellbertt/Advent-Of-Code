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

s = strs()
g = defaultdict(set)
for u, v in [x.split("-") for x in s]:
    g[u].add(v)
    g[v].add(u)
ans = ""
for poss in [{k}|v for k, v in g.items()]:
    for k in range(len(poss)):
        for c in combinations(poss, k):
            good = 1
            for u in c:
                for v in c:
                    if u == v:
                        continue
                    if v not in g[u]:
                        good = 0
                        break
                if not good:
                    break
            if good:
                guess = ",".join(sorted(c))
                if len(guess) > len(ans):
                    ans = guess
                break
print(ans)
