import sys, collections, functools, itertools, math, operator as op, re
eg = '''....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
'''
# eg='''.....
# ..##.
# ..#..
# .....
# ..##.
# .....
# '''
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

s = strs()
elves = set([complex(i, j) for i in range(len(s)) for j in range(len(s[0])) if s[i][j] == '#'])
dirs = [-1, 1, -1j, 1j]
for _ in range(10000000):
  ec = 0
  props = collections.defaultdict(list)
  for e in elves:
    N = {e - 1, e - 1 + 1j, e - 1 - 1j}
    S = {e + 1, e + 1 + 1j, e + 1 - 1j}
    W = {e - 1j, e - 1j - 1, e - 1j + 1}
    E = {e + 1j, e + 1j - 1, e + 1j + 1}
    if not (N | S | W | E) & elves:
      ec += 1
      continue
    for d in dirs:
      match d:
        case -1:
          if not N & elves:
            props[e - 1].append(e)
            break
        case 1:
          if not S & elves:
            props[e + 1].append(e)
            break
        case -1j:
          if not W & elves:
            props[e - 1j].append(e)
            break
        case 1j:
          if not E & elves:
            props[e + 1j].append(e)
            break
  for k, v in props.items():
    if len(v) == 1:
      elves.remove(v[0]) 
      elves.add(k)   
  dirs = dirs[1:] + dirs[:1]
  if ec == len(elves):
    print(_ + 1)
    exit()
