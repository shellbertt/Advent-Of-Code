import sys, collections, itertools, math
input = lambda: sys.stdin.readline().rstrip()
ints = lambda: list(map(int, sys.stdin.readlines()))
strs = lambda: list(lambda l: l.rstrip(), sys.stdin.readlines)
Int = lambda: int(input())
yn = lambda b: print('YES' if b else 'NO')

a = []
c = 0
for l in sys.stdin:
  if l.rstrip() != '':
    c += int(l)
  else:
    a.append(c)
    c = 0
print(sum(sorted(a)[-3:]))
