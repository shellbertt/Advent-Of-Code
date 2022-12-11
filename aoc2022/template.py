import sys, collections, functools, itertools, math, operator as op, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = ''''''
stdin = lambda: sys.stdin.read().rstrip()
#################
if eg: stdin = lambda: eg
#################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if re.match(r"[+-]?\d+", x) else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]


