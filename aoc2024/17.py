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

r, p = chunks()
r = list(map(lambda x: Ints(x)[0], r))
p = Ints(p[0])
def combo(op):
    if op <= 3:
        return op
    else:
        return r[op-4]
inst = 0
out = []
while inst < len(p)-1:
    op = p[inst]
    op2 = p[inst+1]
    if op == 0:
        r[0] = r[0] // 2 ** combo(op2)
    elif op == 1:
        r[1] = r[1] ^ op2
    elif op == 2:
        r[1] = combo(op2) % 8
    elif op == 3:
        if r[0] != 0:
            inst = op2
            continue
    elif op == 4:
        r[1] = r[1] ^ r[2]
    elif op == 5:
        out.append(combo(op2) % 8)
    elif op == 6:
        r[1] = r[0] // 2 ** combo(op2)
    elif op == 7:
        r[2] = r[0] // 2 ** combo(op2)
    inst += 2
print(",".join(map(str, out)))
