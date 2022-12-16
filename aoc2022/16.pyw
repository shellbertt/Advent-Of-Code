import sys, collections, functools, itertools, math, operator as op, re
eg = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
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

g = {}
flow = {}
for l in strs():
  v, *n = re.findall(r"[A-Z][A-Z]", l)
  g[v] = dict(zip(n, len(n) * [1]))
  flow[v] = Ints(l)[0]

again = True
while again:
  again = False
  rem = []
  for v, n in g.items():
    if v == 'AA':
      continue
    if len(n) == 2 and flow[v] == 0:
      a, b = n
      g[a][b] = min(n[a] + n[b], math.inf if b not in g[a] else g[a][b])
      g[a].pop(v)
      g[b][a] = min(n[a] + n[b], math.inf if b not in g[b] else g[b][a])
      g[b].pop(v)
      rem.append(v)
      again = True
      break
  for r in rem:
    g.pop(r)
    flow.pop(r)

ans = 0

mins = 26
poss = [('AA', 'AA', 0, set(), 0, 0, 0, '')]
best = collections.defaultdict(lambda: -1)
while len(poss):
  v, ve, fl, op, t, hbusy, ebusy, debug = poss.pop(0)
  if t == mins:
    continue
  best[tuple(sorted((v, ve)))] = max(best[tuple(sorted((v, ve)))], fl)
  ans = max(ans, fl)

  human = []
  ele = []
  if hbusy:
    human.append((v, 0, -1, hbusy, f'h busy {v} at {t}'))
  else:
    if flow[v] > 0 and v not in op:
      human.append((v, (mins - t - 1) * flow[v], v, 1, f'(h open {v} at {t})'))
    for x in g[v]:
      if best[tuple(sorted([ve, x]))] < fl:
        human.append((x, 0, -1, g[v][x], f'(h go {x} at {t})'))
  if ebusy:
    ele.append((ve, 0, -2, ebusy, f'e busy {v} at {t}'))
  else:
    if flow[ve] > 0 and ve not in op:
      ele.append((ve, (mins - t - 1) * flow[ve], ve, 1, f'(e open {ve} at {t})'))
    for x in g[ve]:
      if best[tuple(sorted([v, x]))] < fl:
        ele.append((x, 0, -2, g[ve][x], f'(e go {x} at {t})'))

  for i in range(len(human)):
    for j in range(len(ele)):
      v, newfh, oh, hb, debuga = human[i]
      ve, newfe, oe, eb, debugb = ele[j]
      if oh != oe:
        poss.append((v, ve, fl + newfh + newfe, op | {oh, oe}, t + 1, max(hb - 1, 0), max(eb - 1, 0), debug + debuga + debugb))

print(ans)
