import sys, collections, functools, itertools, math, operator as op, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
'''
stdin = lambda: sys.stdin.read().rstrip()
#################
# if eg: stdin = lambda: eg
# #################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if re.match(r"[+-]?\d+", x) else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

g = [[ord(x) - ord('a') for x in r] for r in grid()]
S = ord('S') - ord('a')
E = ord('E') - ord('a')

begin = None
end = None
for i in range(len(g)):
  if S in g[i]:
    begin = (i, g[i].index(S), 0)
  if E in g[i]:
    end = (i, g[i].index(E), -1)
g[begin[0]][begin[1]] = 0
g[end[0]][end[1]] = 25

ans = None
stack = [begin]
seen = {}
while len(stack) > 0:
  x, y, d = stack.pop(0)
  if (x, y) in seen:
    if d + 1 < seen[(x, y)]:
      seen[(x, y)] = d + 1
    else:
      continue
  else:
    seen[(x, y)] = d + 1
  if x == end[0] and y == end[1]:
    ans = d
    break
  if x > 0 and g[x - 1][y] <= g[x][y] + 1:
    stack.append((x - 1, y, d + 1))
  if y > 0 and g[x][y - 1] <= g[x][y] + 1:
    stack.append((x, y - 1, d + 1))
  if x < len(g) - 1 and g[x + 1][y] <= g[x][y] + 1:
    stack.append((x + 1, y, d + 1))
  if y < len(g[0]) - 1 and g[x][y + 1] <= g[x][y] + 1:
    stack.append((x, y + 1, d + 1))

print(ans)
