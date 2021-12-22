from utils import * ; from aocd import numbers
print(sum(p[0] < p[1] for p in windows(numbers, 2)))
