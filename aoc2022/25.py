import sys, collections, functools, itertools, math, operator as op, re
eg = '''1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
'''
# eg = '''2=-01'''
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

d = dict(zip('210-=', [2, 1, 0, -1, -2]))
e = dict(zip([2, 1, 0, -1, -2], '210-='))

def to(s):
  n = 0
  for i in range(len(s)):
    n += 5 ** (len(s) - 1 - i) * d[s[i]]
  return n

def From(n):
  if n < 3: return e[n]
  p = 0
  while 5 ** p // 10 < n:
    p += 1
  s = (p - 1) * ['0']
  i = 0
  while n:
    if n % 5 in e:
      put = to(s[i]) + to(e[n % 5])
      if put < 3:
        s[i] = str(put)
      elif put == 3:
        s[i] = '='
        s[i + 1] = '1'
      elif put == 4:
        s[i] = '-'
        s[i + 1] = '1'
    else:
      s[i] = From(to(s[i]) + to(e[n % 5 - 5]))
      s[i + 1] = '1'
    n //= 5
    i += 1
  return ''.join(s[::-1])

Sum = 0
for s in strs():
  Sum += to(s)

print(From(Sum))
assert(Sum == to(From(Sum)))
