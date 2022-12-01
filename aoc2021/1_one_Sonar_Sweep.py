from aocd import numbers
print(sum([this > last for last, this in zip(numbers, numbers[1:])]))
