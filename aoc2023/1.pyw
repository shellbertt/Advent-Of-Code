import sys, collections, functools, itertools, math, operator as op, re
eg = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
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
#if eg: stdin = lambda: eg

ans = 0
w = "one two three four five six seven eight nine".split()
for s in strs():
    l = -1
    li = 1<<100
    for i in range(1, 10):
        j = s.find(w[i-1])
        if j == -1: continue
        if j < li:
            li = j
            l = i
    for i in range(1, 10):
        j = s.find(str(i))
        if j == -1: continue
        if j < li:
            li = j
            l = i
    r = l
    ri = 0
    for i in range(1, 10):
        j = s.rfind(w[i-1])
        if j == -1: continue
        if j > ri:
            ri = j
            r = i
    for i in range(1, 10):
        j = s.rfind(str(i))
        if j == -1: continue
        if j > ri:
            ri = j
            r = i
    x = int(str(l) + str(r))
    ans += x
print(ans)
