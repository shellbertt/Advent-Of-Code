from utils import * ; from aocd import data

numbers = list(map(int, data.split(',')))

for i in range(80):
    new = numbers.count(0)
    numbers = [[x - 1, 6][x == 0] for x in numbers]
    for i in range(new): numbers.append(8)

print(len(numbers))
