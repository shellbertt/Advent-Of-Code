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

inp = lmap(lambda x: 811589153 * x, ints())
n = len(inp)

ans = list(zip(inp, range(n)))
for _ in range(10):
  i = 0
  moved = 0
  need = 0
  while moved < n:
    if ans[i][1] != need:
      i = (i + 1) % n
      continue
    newi = (i + ans[i][0]) % (n - 1)
    ans.insert(newi, ans.pop(i))
    need += 1
    moved += 1

zi = [x[0] for x in ans].index(0)
print(sum([ans[(1000 + zi) % len(ans)][0], ans[(2000 + zi) % len(ans)][0], ans[(3000 + zi) % len(ans)][0]]))
