import sys, collections, functools, itertools, math, re
input = lambda: sys.stdin.readline().rstrip()
Int = lambda: int(input())
yn = lambda b: print('YES' if b else 'NO')
eg = ''''''
stdin = sys.stdin.read().rstrip()
#################
if eg: stdin = eg
#################
maybeint = lambda x: int(x) if x.isnumeric() else x
lmap = lambda f, *x: list(map(f, *x))
ints = lambda: lmap(maybeint, stdin.splitlines())
strs = lambda: stdin.splitlines()
splits = lambda s: lmap(lambda x: lmap(maybeint, x.split(s)), stdin.splitlines())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin.split('\n\n'))


