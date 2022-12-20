import sys, collections, functools, itertools, math, operator as op, re
eg = '''1
2
-3
3
-2
0
4
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

inp = ints()
n = len(inp)
seen = set()
ans = list(zip(inp, range(n)))
i = 0
moved = 0
seen = set()
while moved < n:
  # print(ans)
  if ans[i][1] in seen:
    i += 1
    continue
  newi = (i + ans[i][0]) % (n - 1)
  seen.add(ans[i][1])
  ans.insert(newi, ans.pop(i))
  i += newi == 0
  moved += 1

zi = [x[0] for x in ans].index(0)
print(sum([ans[(1000 + zi) % len(ans)][0], ans[(2000 + zi) % len(ans)][0], ans[(3000 + zi) % len(ans)][0]]))
