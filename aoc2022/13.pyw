import sys, collections, functools, itertools, math, operator as op, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
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

def comp(x, y):
  if type(x) == int and type(y) == int:
    return y - x
  if type(x) == list and type(y) == int:
    return comp(x, [y])
  if type(x) == int and type(y) == list:
    return comp([x], y)
  if len(x) == 0 and len(y) == 0:
    return 0
  if len(x) == 0:
    return 1
  if len(y) == 0:
    return -1
  c = comp(x[0], y[0])
  if c == 0:
    return comp(x[1:], y[1:])
  elif c > 0:
    return 1
  return -1 

a = lmap(eval, filter(lambda s: s, strs())) + [[[2]]] + [[[6]]]
for i in range(1, len(a)):
  for j in range(i, 0, -1):
    if comp(a[j], a[j - 1]) > 0:
      a[j], a[j - 1] = a[j - 1], a[j]

print((a.index([[2]]) + 1) * (a.index([[6]]) + 1))
