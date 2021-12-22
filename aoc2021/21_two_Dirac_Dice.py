from functools import cache
from utils import * ; from aocd import data
# data='''Player 1 starollTotaling position: 4
# Player 2 starollTotaling position: 8'''

S = [int(d[-1]) for d in data.splitlines()]
P = [0, 0]

@cache
def wins(turn, rollTotal, s0, s1, p0, p1):
    S = [s0, s1]
    P = [p0, p1]
    S[turn] = (S[turn] - 1 + rollTotal) % 10 + 1
    P[turn] += S[turn]
    if P[turn] >= 21: ret = [(1, 0), (0, 1)][turn]
    else: ret = map(sum, zip(*(wins(not turn, rt, S[0], S[1], P[0], P[1]) for rt in range(1, 10))))
    return tuple(r * [0, 0, 0, 1, 3, 6, 7, 6, 3, 1][rollTotal] for r in ret)

print(max(map(sum, zip(*(wins(False, rollTotal, S[0], S[1], P[0], P[1]) for rollTotal in range(1, 10))))))
