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
d = {}
state = {}
for x in s:
    w = words(x)
    d[w[0]] = [x[0], w[1:]]
    if x[0] == "&":
        state[w[0]] = {}
    elif x[0] == "%":
        state[w[0]] = False
for k, v in d.items():
    for x in v[1]:
        if x in d and d[x][0] == "&":
            state[x][k] = False

c = []
n = 1000
i = 0
seen = set()
while i < n:
    s = str(state)
    if s in seen:
        break
    seen.add(s)
    q = deque([("broadcaster", False)])
    seenq = set()
    cc = [1, 0]
    while q:
        cur, level = q.popleft()
        type = d[cur][0]
        if type == "b":
            out = 0
        elif type == "%":
            if level:
                continue
            else:
                state[cur] = not state[cur]
            out = state[cur]
        elif type == "&":
            out = not all(x for x in state[cur].values())
        for x in d[cur][1]:
            cc[out] += 1
            if x not in d:
                continue
            if d[x][0] == "&":
                state[x][cur] = out
            q.append((x, out))
    i += 1
    c.append(cc)
d, r = divmod(n, len(c))
print((d * sum(x[0] for x in c) + sum(x[0] for x in c[:r])) * (d * sum(x[1] for x in c) + sum(x[1] for x in c[:r])))
