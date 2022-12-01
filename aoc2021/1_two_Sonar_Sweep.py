from aocd import numbers
print(sum([numbers[i] + numbers[i - 1] + numbers[i - 2] > numbers[i - 1] + numbers[i - 2] + numbers[i - 3] for i in range(3, len(numbers))]))
