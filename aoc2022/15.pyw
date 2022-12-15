import sys, collections, functools, itertools, math, operator as op, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"[+-]?\d+", s))
Int = lambda: int(input())
eg = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
'''
stdin = lambda: sys.stdin.read().rstrip()
###################
# if eg: stdin = lambda: eg
###################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if re.match(r"^[+-]?\d+$", x) else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

# b = 21
b = 4000001
s = [[] for i in range(b)]
for c in lmap(Ints, strs()):
  sx, sy, bx, by = c
  d = abs(sx - bx) + abs(sy - by)
  for y in range(max(sy - d, 0), min(sy + d + 1, b)):
    am = d - abs(y - sy)
    newr = (sx - am, sx + am)
    newsy = []
    for r in s[y]:
      if not (r[1] < newr[0] or newr[1] < r[0]):
        newr = (min(newr[0], r[0]), max(newr[1], r[1]))
      else:
        newsy.append(r)
    s[y] = newsy
    s[y].append(newr)

for y in range(len(s)):
  if len(s[y]) > 1:
    print((min(max(s[y])) - 1) * 4000000 + y)
    break
