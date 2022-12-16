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
  g[v] = n
  flow[v] = Ints(l)[0]

ans = 0
mins = 30
poss = [('AA', 0, set(), 0)]
best = collections.defaultdict(lambda: -1)
best['AA'] = 0
while len(poss):
  v, fl, op, t = poss.pop(0)
  if t == mins:
    continue
  ans = max(ans, fl)
  if flow[v] > 0 and v not in op:
    poss.append((v, fl + (mins - t - 1) * flow[v], op | {v}, t + 1))
  for x in g[v]:
    if best[x] < fl:
      best[x] = fl
      poss.append((x, fl, op.copy(), t + 1))

print(ans)
