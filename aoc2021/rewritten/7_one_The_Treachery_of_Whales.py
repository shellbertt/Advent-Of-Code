from utils import * ; from aocd import data

N = list(map(int, data.split(',')))

cost = lambda pos: sum(abs(n - pos) for n in N)
print(min(cost(i) for i in range(min(N), max(N) + 1)))
