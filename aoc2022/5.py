import sys, collections, functools, itertools, math, re
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''
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

inp = strs()
s = [[] for i in range(9)]
for r in inp[:8][::-1]:
  i = 0
  r += '  '
  for c in slide(r, 4, 4):
    x = c.strip()
    if x != '': s[i].append(x)
    i += 1
for m in inp[10:]:
  n, f, t = Ints(m)
  for i in range(n):
    s[t - 1].append(s[f - 1].pop())

print(''.join(x[-1] for x in s).replace('[','').replace(']',''))
