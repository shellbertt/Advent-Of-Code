import sys, functools, itertools, math, operator as op, re
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

cards = "AKQT98765432J"

def inds(x):
    return [cards.index(y) for y in x]

def score(h):
    h = list(str(h[0]))
    poss = []
    for c in cards[:-1]:
        poss.append(indscore("".join(h).replace("J", c), h))
    return min(poss)

def indscore(h, orig):
    h = sorted(h, key=lambda s: (-h.count(s), cards.index(s)))
    uniq = len(set(h))
    firstc = h.count(h[0])
    if uniq == 1:
        return (0, inds(orig))
    elif uniq == 2:
        if firstc == 4:
            return (1, inds(orig))
        elif firstc == 3:
            return (2, inds(orig))
    elif uniq == 3:
        if firstc == 3:
            return (3, inds(orig))
        elif firstc == 2:
            return (4, inds(orig))
    elif uniq == 4:
        return (5, inds(orig))
    else:
        return (6, inds(orig))

s = splits()
s.sort(key=score)
ans = sum(s[i][1] * (len(s)-i) for i in range(len(s)))
print(ans)

