from utils import * ; from aocd import data

def cost(nums, pos):
    return sum((abs(n - pos) * (abs(n - pos) + 1)) / 2 for n in nums)

numbers = list(map(int, data.split(',')))

costs = []
for i in range(min(numbers), max(numbers)):
    costs.append(cost(numbers, i))

print(int(min(costs)))