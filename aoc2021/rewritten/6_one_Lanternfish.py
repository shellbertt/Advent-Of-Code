from utils import * ; from aocd import data

numbers = list(map(int, data.split(',')))
counts = [numbers.count(i) for i in range(9)]

for i in range(80):
    counts.append(counts.pop(0))
    counts[6] += counts[8]

print(sum(counts))