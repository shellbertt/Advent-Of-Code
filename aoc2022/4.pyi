import sys, collections, functools, itertools, math, re
input = lambda: sys.stdin.readline().rstrip()
Int = lambda: int(input())
yn = lambda b: print('YES' if b else 'NO')
eg = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''
stdin = sys.stdin.read().rstrip()
#################
# if eg: stdin = eg
#################
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: list(map(maybeint, stdin.splitlines()))
strs = lambda: stdin.splitlines()
chunks = lambda: list(map(lambda c: list(map(maybeint, c.splitlines())), stdin.split('\n\n')))

# exta solution
ans = 0
for s in strs():
  # a, b = map(lambda x: eval('set(range(' + x.replace('-', ',') + '+1))'), s.split(','))
  # ans += a <= b or b <= a
  a, b = map(lambda x: eval('set(range(' + x.replace('-', ',') + '+1))'), s.split(','))
  ans += len(a & b) > 0
print(ans)
