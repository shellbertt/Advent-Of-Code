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

s = stdin()
n = len(s)
a = []
file = True
fid = 0
for i in range(n):
    if file:
        a.append([fid, int(s[i])])
        fid += 1
    else:
        a.append([-1, int(s[i])])
    file = not file
i = 0
while i < len(a):
    if a[i] == -1:
        x = a.pop()
        while x == -1:
            x = a.pop()
        if i < len(a):
            a[i] = x
        else:
            a.append(x)
    i += 1
i = len(a)-1
while i > -1:
    x = a[i]
    if x[0] == -1:
        i -= 1
        continue
    for j in range(i):
        if a[j][0] == -1:
            if a[j][1] >= x[1]:
                a[j][1] -= x[1]
                a.insert(j, x[:])
                i += 1
                a[i][0] = -1
                break
    i -= 1
b = []
for x in a:
    b.extend([x[0]] * x[1])
ans = 0
for i in range(len(b)):
    if b[i] != -1:
        ans += i * b[i]
print(ans)
