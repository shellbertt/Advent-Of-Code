from utils import * ; from aocd import lines

b = {'(': ')', '[': ']', '{': '}', '<': '>'}
p = {')': 1, ']': 2, '}': 3, '>': 4}

newL = []
for l in lines:
    s = []
    bad = False
    for c in l:
        if c in b: s.append(c)
        elif b[s.pop()] != c:
            bad = True
            break
    if not bad: newL.append(l)
lines = newL

End = []
for l in lines:
    s = []
    for c in l:
        if c in b: s.append(c)
        else: s.pop()
    end = 0
    for c in reversed(s):
        end *= 5
        end += p[b[c]]
    End.append(end)

print(sorted(End)[len(End) // 2])
