import sys, collections, functools, itertools, math, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''30373
25512
65332
33549
35390'''
stdin = lambda: sys.stdin.read().rstrip()
#################
# if eg: stdin = lambda: eg
#################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

g = grid()
ans = [[0 for c in range(len(g[0]))] for r in range(len(g))]

for i in range(len(g)):
  m = -1
  for j in range(len(g[0])):
    if g[i][j] > m:
      ans[i][j] = 1
      m = g[i][j]

for i in range(len(g)):
  m = -1
  for j in range(len(g[0]) - 1, -1, -1):
    if g[i][j] > m:
      ans[i][j] = 1
      m = g[i][j]

for j in range(len(g[0])):
  m = -1
  for i in range(len(g)):
    if g[i][j] > m:
      ans[i][j] = 1
      m = g[i][j]

for j in range(len(g[0])):
  m = -1
  for i in range(len(g) - 1, -1, -1):
    if g[i][j] > m:
      ans[i][j] = 1
      m = g[i][j]

print(sum(sum(r) for r in ans))
