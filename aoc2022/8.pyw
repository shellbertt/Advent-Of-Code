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
ans = -1

for i in range(len(g)):
  for j in range(len(g[0])):
    h = g[i][j]
    a, b, c, d = 0, 0, 0, 0
    for k in range(i - 1, -1, -1):
      a += 1
      if g[k][j] >= h: break
    for l in range(i + 1, len(g)):
      b += 1
      if g[l][j] >= h: break
    for m in range(j - 1, -1, -1):
      c += 1
      if g[i][m] >= h: break
    for n in range(j + 1, len(g[0])):
      d += 1
      if g[i][n] >= h: break
    ans = max(a * b * c * d, ans)

print(ans)
