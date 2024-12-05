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

S = "XMAS"
N = len(S)

def diag(s):
    m, n = len(s), len(s[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            k = 0
            for l in range(N):
                if i+l in range(m) and j+l in range(n) and S[k] == s[i+l][j+l]:
                    k += 1
                else:
                    break
            if k == N:
                ans += 1
    return ans

s = strs()
ans = 0

for _ in range(4):
    ans += sum(x.count("XMAS") for x in s)
    ans += diag(s)
    s = list(map("".join, zip(*s[::-1])))

print(ans)
