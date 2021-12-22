from utils import * ; from aocd import lines

def flash(l, o):
    if (l, o) in flashed: return 0
    O[l][o] += 1
    if O[l][o] <= 9: return 0
    flashed.append((l, o))
    O[l][o] = 0
    f = 1

    # L = [l, l - 1, l + 1]
    # oO = [o, o - 1, o + 1]
    # for ll in L:
    #     for oo in oO:
    #         if ll > 0 and oo > 0 and ll < len(lines) - 1 and oo < len(lines[0]) - 1 and (ll, oo) not in flashed:
    #             O[ll][oo] += 1
    #             if O[ll][oo] > 0: f += flash(ll, oo)
    # if l != 0 and (l - 1, o) not in flashed:
    #     O[l - 1][o] += 1
    #     if O[l - 1][o] > 9: f += flash(l - 1, o)

    if l != 0: f += flash(l - 1, o)
    if l != len(lines) - 1: f += flash(l + 1, o)
    if o != 0 and (l, o - 1): f += flash(l, o - 1)
    if o != len(lines[0]) - 1: f += flash(l, o + 1)
    if o != 0 and l != 0: f += flash(l - 1, o - 1)
    if o != len(lines[0]) - 1 and l != len(lines) - 1: f += flash(l + 1, o + 1)
    if o != 0 and l != len(lines) - 1: f += flash(l + 1, o - 1)
    if o != len(lines[0]) - 1 and l != 0: f += flash(l - 1, o + 1)

    return f

O = [[int(o) for o in l] for l in lines]

flashes = 0
for i in range(100):
    flashed = []
    for l in range(len(lines)):
        for o in range(len(lines[0])):
            flashes += flash(l, o)

print(flashes)
