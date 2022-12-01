from utils import * ; from aocd import lines

b = {'(': ')', '[': ']', '{': '}', '<': '>'}
p = {')': 3, ']': 57, '}': 1197, '>': 25137}

bad = 0
for l in lines:
    s = []
    for c in l:
        if c in b:
            s.append(c)
        elif b[s.pop()] != c:
            bad += p[c]
            break

print(bad)
