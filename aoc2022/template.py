import sys, collections, functools, itertools, math, re
ints = lambda s=None: lmap(maybeint, input().split(s))
Int = lambda: int(input())
eg = ''''''
stdin = sys.stdin.read().rstrip()
#################
if eg: stdin = eg
#################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda s=stdin: s.splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin.split('\n\n'))


