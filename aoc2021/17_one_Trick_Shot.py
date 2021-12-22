from utils import * ; from aocd import data

# I looked for the largest pair of consecutive triangular numbers that have a difference within the final y range
# (this code only works when the target's minimum y bound is negative)
Y = int(data.split('y=')[1].split('..')[0])
print(Y * (Y + 1) // 2) # Max height is also a triangular number, the smaller of the pair
