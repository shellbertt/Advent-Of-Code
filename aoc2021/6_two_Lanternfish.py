from utils import * ; from aocd import data

numbers = list(map(int, data.split(',')))
counts = [numbers.count(i) for i in range(9)]

for i in range(256):
    counts.append(counts[0])
    n = counts.pop(0)
    counts[6] += n

print(sum(counts))
