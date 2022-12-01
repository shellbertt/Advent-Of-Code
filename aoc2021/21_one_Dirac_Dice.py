from utils import * ; from aocd import data
# data='''Player 1 starting position: 4
# Player 2 starting position: 8'''

S = [int(d[-1]) for d in data.splitlines()]
P = [0, 0]

turn = False
i = 1
j = 0
while max(P) < 1000:
    S[turn] = (S[turn] - 1 + 3 * i + 3) % 10 + 1
    P[turn] += S[turn]
    turn = not turn
    i = (i - 1 + 3) % 100 + 1
    j += 3

print(min(P) * j)
