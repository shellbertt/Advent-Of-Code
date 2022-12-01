execfile('utils.py') ; from aocd import lines
gamma = ""
epsilon = ""
counts = 12 * [0]
for l in lines:
    for i, d in enumerate(str(l)):
        if d == '1':
            counts[i] += 1
for c in counts:
    if c > len(lines) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
print(int(gamma, 2) * int(epsilon, 2))
