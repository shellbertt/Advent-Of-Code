import sys, collections, functools, itertools, math, operator as op, re
eg = '''#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
'''
# eg = '''#.#####
# #..^..#
# #>....#
# #<....#
# #...v.#
# #.....#
# #####.#
# '''
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"[+-]?\d+", s))
stdin = sys.stdin.read().rstrip()
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if re.match(r"^[+-]?\d+$", x) else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin.splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin.split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]
# if eg: stdin = eg

g = grid()
dirs = {'^': -1, 'v': 1, '<': -1j, '>': 1j}
bliz = set([(complex(i - 1, j - 1), dirs[g[i][j]]) for i in range(len(g)) for j in range(len(g[0])) if g[i][j] in "<>^v"])
w, h = len(g[0]) - 2, len(g) - 2

time = math.inf

def inbounds(c):
  return (0 <= c.real < h) and (0 <= c.imag < w)

pos = -1 + 0j
end = complex(h, w - 1)
s = [(pos, 0)]
curt = -1
seen = set()
while s:
  pos, t = s.pop(0)
  if (pos, t) in seen: continue
  seen.add((pos, t))
  if pos + 1 == end:
    time = t + 1
    break

  if t > curt:
    curt = t
    newbliz = set()
    for b, d in bliz:
      new = b + d
      if new.real < 0:
        new = complex(h - 1, new.imag)
      elif new.real >= h:
        new = complex(0, new.imag)
      elif new.imag < 0:
        new = complex(new.real, w - 1)
      elif new.imag >= w:
        new = complex(new.real, 0)
      newbliz.add((new, d))
    bliz = newbliz
  blizl = set([b[0] for b in bliz])

  if inbounds(pos - 1) and pos - 1 not in blizl:
    s.append((pos - 1, t + 1))
  if inbounds(pos + 1) and pos + 1 not in blizl:
    s.append((pos + 1, t + 1))
  if inbounds(pos - 1j) and pos - 1j not in blizl:
    s.append((pos - 1j, t + 1))
  if inbounds(pos + 1j) and pos + 1j not in blizl:
    s.append((pos + 1j, t + 1))
  if pos not in blizl:
    s.append((pos, t + 1))
  
print(time)
