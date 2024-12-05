import sys, functools, math, re
from itertools import *
from collections import *
import copy
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

a, b = chunks()
a = [eval(x.replace("|",",")) for x in a]
orig_inc = defaultdict(list)
for x in a:
    orig_inc[x[1]].append(x[0])
orig_out = defaultdict(list)
for x in a:
    orig_out[x[0]].append(x[1])

bad = []
for r in b:
    r = eval(r)
    n = len(r)
    inc = copy.deepcopy(orig_inc)
    out = copy.deepcopy(orig_out)
    for x in r:
        if any(y in inc[x] for y in r):
            bad.append(r)
            break
        for y in out[x]:
            inc[y].remove(x)

ans = 0
for r in bad:
    r = list(r)
    n = len(r)
    inc = copy.deepcopy(orig_inc)
    out = copy.deepcopy(orig_out)
    correct = []
    while len(r) > 0:
        for x in r:
            if not (set(inc[x]) & set(r)):
                correct.append(x)
                r.remove(x)
                break
    ans += correct[n//2]

print(ans)
