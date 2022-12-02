import sys, collections, itertools, math
input = lambda: sys.stdin.readline().rstrip()
Int = lambda: int(input())
yn = lambda b: print('YES' if b else 'NO')
stdin = sys.stdin.read().rstrip()
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: list(map(maybeint, stdin.splitlines()))
strs = lambda: stdin.splitlines()
chunks = lambda: list(map(lambda c: list(map(maybeint, c.splitlines())), stdin.split('\n\n')))
stdin = '''A Y
B X
C Z'''
s = 0
for S in strs():
  a, b = S.split()
  if a == 'A':
    if b == 'X': s += 3
    elif b == 'Y': s+= 6
  elif a == 'B':
    if b == 'Y': s += 3
    elif b == 'Z': s+= 6
  elif a == 'C':
    if b == 'X': s += 6
    elif b == 'Z': s+= 3
  if b == 'X':
    s += 1
  elif b == 'Y':
    s += 2
  elif b == 'Z':
    s += 3
print(s)
