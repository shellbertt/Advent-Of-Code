import sys, collections, functools, itertools, math, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''
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

seen = set([(0,0)])
k = [[0,0] for i in range(10)]
m = {'R':(1, 0), 'L':(-1, 0), 'U':(0,1),'D':(0,-1)}
for a, b in splits():
  i = 0
  while i < b:
    k[0][0] += m[a][0]
    k[0][1] += m[a][1]
    for j in range(9):
      while abs(k[j][0] - k[j + 1][0]) > 1 or abs(k[j][1] - k[j + 1][1]) > 1:
        if abs(k[j][0] - k[j + 1][0]) > 0:
          if k[j][0] - k[j + 1][0] > 0:
            k[j + 1][0] += 1
          else:
            k[j + 1][0] -= 1
        if abs(k[j][1] - k[j + 1][1]) > 0:
          if k[j][1] - k[j + 1][1] > 0:
            k[j + 1][1] += 1
          else:
            k[j + 1][1] -= 1
    seen.add(tuple(k[-1]))
    i += 1

print(len(seen))
