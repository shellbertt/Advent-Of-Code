import sys, collections, functools, itertools, math, operator as op, re
eg = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
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

m, D = chunks()
width = max([len(r) for r in m])
m = lmap(lambda s: s.ljust(width), m)

pos = None
for i in range(len(m)):
  if '.' in m[i]:
    pos = complex(i, m[i].index('.'))
    break

sidelength = len(m) // 3
dirs = [1j, 1, -1j, -1]
di = 0
dis = None
for d in re.findall(r"(\d+|[LR])", D[0]):
  if int(pos.real) <= sidelength:
    face = 1
  elif sidelength < int(pos.real) <= 2 * sidelength:
    face = 2 + int(pos.imag) // sidelength
  elif 2 * sidelength < int(pos.real):
    face = 3 + int(pos.imag) // sidelength

  try:
    dis = int(d)
  except:
    di = (di + (1 if d == 'R' else -1)) % 4

  while dis > 0:
    oldpos = pos
    olddi = di
    pos += dirs[di]

    if int(pos.real) >= len(m) or int(pos.imag) >= len(m[0]) or m[int(pos.real)][int(pos.imag)] == ' ':
      if face == 1:
        if di == 0: # to 6
          other = sidelength - int(pos.real) + 2 * sidelength
          new = width - 1
          pos = complex(other, new)
          while m[other][new] not in '.#':
            new -= 1
            pos = complex(other, new)
          di = 2
        elif di == 2: # to 3
          other = sidelength + int(pos.imag) - 2 * sidelength
          new = 0
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new += 1
            pos = complex(new, other)
          di = 1
        elif di == 3: # to 2
          other = sidelength - (int(pos.imag) - 2 * sidelength)
          new = 0
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new += 1
            pos = complex(new, other)
          di = 1
      elif face == 2:
        if di == 1: # to 5
          other = width - 1 -sidelength - int(pos.real)
          new = len(m) - 1
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new -= 1
            pos = complex(new, other)
          di = 3
        elif di == 2: # to 6
          other = width - 1 -(int(pos.real) - sidelength)
          new = width - 1
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new -= 1
            pos = complex(new, other)
          di = 3
        elif di == 3: # to 1
          other = sidelength - int(pos.real) + 2 * sidelength
          new = 0
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new += 1
            pos = complex(new, other)
          di = 1
      elif face == 3:
        if di == 1: # to 5
          other = int(pos.imag) - sidelength + 2 * sidelength
          new = 0
          pos = complex(other, new)
          while m[other][new] not in '.#':
            new += 1
            pos = complex(other, new)
          di = 0
        elif di == 3: # to 1
          other = int(pos.imag) - sidelength
          new = 0
          pos = complex(other, new)
          while m[other][new] not in '.#':
            new += 1
            pos = complex(other, new)
          di = 1
      elif face == 4:
        if di == 0: # to 6
          other = width - 1 - int(pos.real) % sidelength
          new = 0
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new += 1
            pos = complex(new, other)
          di = 1
      elif face == 5:
        if di == 1: # to 2
          other = sidelength - 1 - (int(pos.imag) - 2 * sidelength)
          new = len(m) - 1
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new -= 1
            pos = complex(new, other)
          di = 3
        elif di == 2:
          other = int(pos.imag) - sidelength + 2 * sidelength
          new = len(m) - 1
          pos = complex(new, other)
          while m[new][other] not in '.#':
            new -= 1
            pos = complex(new, other)
          di = 3
      elif face == 6:
        if di == 0: # to 1
          other = sidelength - int(pos.real) - 2 * sidelength
          new = width - 1
          pos = complex(other, new)
          while m[other][new] not in '.#':
            new -= 1
            pos = complex(other, new)
          di = 1
        elif di == 1: # to 2
          other = width - 1 -int(pos.imag) + sidelength
          new = 0
          pos = complex(other, new)
          while m[other][new] not in '.#':
            new += 1
            pos = complex(other, new)
          di = 0
        elif di == 3: # to 4
          other = sidelength + width - int(pos.imag)
          new = width - 1
          pos = complex(other, new)
          while m[other][new] not in '.#':
            new -= 1
            pos = complex(other, new)
          di = 2
      elif di == 0:
        new = 0
        while m[int(pos.real)][new] not in '.#':
          new += 1
        pos = complex(int(pos.real), new)
      elif di == 2:
        new = width - 1
        while m[int(pos.real)][new] not in '.#':
          new -= 1
        pos = complex(int(pos.real), new)
      elif di == 1:
        new = 0
        while m[new][int(pos.imag)] not in '.#':
          new += 1
        pos = complex(new, int(pos.imag))
      elif di == 3:
        new = len(m) - 1
        while m[new][int(pos.imag)] not in '.#':
          new -= 1
        pos = complex(new, int(pos.imag))

    dis -= 1
    if m[int(pos.real)][int(pos.imag)] == '#':
      pos = oldpos
      di = olddi
      dis = 0
      break

print(pos, di)
print(int((pos.real + 1) * 1000 + (pos.imag + 1) * 4 + di))
