import sys, collections, functools, itertools, math, operator as op, re
eg = '''root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
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

d = {}
for s in lmap(lambda s: s.replace(' ', ''), strs()):
  k, v = s.split(':')
  d[k] = v

root = d['root'].replace('+', '==')
while len(words(root)) > 1:
  for w in words(root):
    if w == 'humn': continue
    root = root.replace(w, '(' + d[w] + ')')

lo, hi, = 0, 9999999999999999999999
humn = (lo + hi) // 2
left = root.find('humn') < root.find('==')
while lo <= hi:
  humn = (lo + hi) // 2
  # I just manually swapped the inequalities since I noticed they were wrong (can be either in general, could do a pass to check which helps)
  if eval(root.replace('==', '>')):
    if left: lo = humn + 1
    else: hi = humn - 1
  elif eval(root.replace('==', '<')):
    if not left: lo = humn + 1
    else: hi = humn - 1
  else: break

print(humn)
