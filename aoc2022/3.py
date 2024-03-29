import sys, collections, itertools, math
input = lambda: sys.stdin.readline().rstrip()
Int = lambda: int(input())
yn = lambda b: print('YES' if b else 'NO')
eg = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''
stdin = sys.stdin.read().rstrip()
#################
# if eg: stdin = eg
#################
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: list(map(maybeint, stdin.splitlines()))
strs = lambda: stdin.splitlines()
chunks = lambda: list(map(lambda c: list(map(maybeint, c.splitlines())), stdin.split('\n\n')))

ans = 0
for s in strs():
  a, b = s[:len(s) // 2], s[len(s) // 2:]
  for x in a:
    if x in b:
      if x.isupper():
        ans += ord(x) - ord('A') + 1 + 26
      else:
        ans += ord(x) - ord('a') + 1
      break

print(ans)
