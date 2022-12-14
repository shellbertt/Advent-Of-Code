import sys, collections, functools, itertools, math, operator as op, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
'''
stdin = lambda: sys.stdin.read().rstrip()
#################
# if eg: stdin = lambda: eg
#################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if re.match(r"[+-]?\d+", x) else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

h = 300
g = [['.'] * 1000 for i in range(h)]
for s in lmap(lambda s: s.split('->'), strs()):
  prev = eval(s[0])
  for c in s[1:]:
    d = eval(c)
    for i in range(min(prev[0], d[0]), max(prev[0], d[0]) + 1):
      for j in range(min(prev[1], d[1]), max(prev[1], d[1]) + 1):
        g[j][i] = '#'
    prev = d

rest = 0
s = [500, 0]
p = [*s]
while True:
  if p[1] == h - 1:
    break
  if g[p[1] + 1][p[0]] == '.':
    p[1] += 1
  elif g[p[1] + 1][p[0] - 1] == '.':
    p[1] += 1
    p[0] -=1 
  elif g[p[1] + 1][p[0] + 1] == '.':
    p[1] += 1
    p[0] += 1 
  else:
    g[p[1]][p[0]] = 'o'
    p = [*s]
    rest += 1

print(rest)
