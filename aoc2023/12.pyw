import sys, functools, math, re
from itertools import *
from collections import *
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
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n + 1, s)]

ans = 0
for r, l in splits():
    # try without padding "."s with counting total?
    r = "." + r + "?" + r + "?" + r + "?" + r + "?" + r + "."
    #r = "." + r + "."
    l = ["." + x * "#" + "." for x in 5 * eval(l)]
    c = 0
    i = [0]
    print(r, l)
    while i:
        #print(r, i, len(i), l, ans) 
        if i[-1] >= len(r):
            i.pop()
            if not i:
                break
        elif all(i[-1] + k < len(r) and r[i[-1] + k] in (l[len(i) - 1][k], "?") for k in range(len(l[len(i) - 1]))):
            #print(r[i[-1]:], l[len(i) - 1])
            i.append(i[-1] + len(l[len(i) - 1]) - 1)
            i[-1] -= 1
        if len(i) > len(l):
            #print(r, i, len(i), l, ans) 
            #print("BAM")
            i.pop()
            inside = []
            for j in range(len(i)):
                #print(j, i[j], len(l[j]), list(range(i[j], len(l[j]) + 1)))
                inside.extend(range(i[j], i[j] + len(l[j])))
            outside = [x for x in range(len(r)) if x not in inside]
            #print(inside)
            #print(outside)
            if sum(r[j] == "#" for j in set(range(len(r))) - set(inside)) + r[:i[0]].count("#") + r[i[-1] + len(l[-1]):].count("#") == 0:
                c += 1
        if i[-1] == "#":
            i.pop()
            if not i:
                break
        i[-1] += 1
    ans += c
    print(c)
print(ans)
