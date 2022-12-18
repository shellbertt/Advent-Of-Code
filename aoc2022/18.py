import sys, collections, functools, itertools, math, operator as op, re
eg = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
'''
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
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]
# if eg: stdin = lambda: eg

g = set(lmap(eval, strs()))
ans = len(g) * 6

for x, y, z in g:
  ans -= (x + 1, y, z) in g
  ans -= (x - 1, y, z) in g
  ans -= (x, y + 1, z) in g
  ans -= (x, y - 1, z) in g
  ans -= (x, y, z + 1) in g
  ans -= (x, y, z - 1) in g

print(ans)
