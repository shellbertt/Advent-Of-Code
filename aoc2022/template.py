import sys, collections, itertools, math
input = lambda: sys.stdin.readline().rstrip()
Int = lambda: int(input())
yn = lambda b: print('YES' if b else 'NO')
eg = ''''''
stdin = sys.stdin.read().rstrip()
#################
if eg: stdin = eg
#################
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: list(map(maybeint, stdin.splitlines()))
strs = lambda: stdin.splitlines()
chunks = lambda: list(map(lambda c: list(map(maybeint, c.splitlines())), stdin.split('\n\n')))


