from aocd import data ; from functools import reduce
# data='C200B40A82'
# data = '04005AC33890'
# data='880086C3E88112'
# data = 'CE00C43D881120'
# data='D8005AC2A8F0'
# data='F600BC2D8F'
# data='9C005AC2F8F0'
data ='9C0141080250320F1802104A08'

h2b = lambda x: bin(int(str(x), 16))[2:].zfill(4)
B = ''.join(h2b(h) for h in data)   # Bytes

stack = []
todo = [0, 1]   # [bits, packets]
while B != '' and int(B, 16) > 0:
    subBits = 0
    bits = 0
    V = int(B[:3], 2)   # version
    T = int(B[3:6], 2)  # Type
    bits += 6
    B = B[6:]
    if T == 4:
        value = ''
        while True:
            value += B[1:5]
            last = not int(B[:1])
            bits += 5
            B = B[5:]
            if last: break
        stack.append((V, T, int(value, 2), bits))
    else:
        LT = int(B[:1])             # Length Type
        LVL = [15, 11][LT]          # Length Value Length
        LV = int(B[1:LVL + 1], 2)   # Length Value
        if LT == 1: todo[1] += LV
        else: subBits = LV
        bits += LVL + 1
        B = B[LVL + 1:]
        stack.append((V, T, LT, LV, bits))
    todo[0] = max(0, todo[0] - bits) + subBits
    todo[1] = max(0, todo[1] - 1)
    if any(t == 0  for t in todo) and len(stack) > 1:
        exprsn = []
        while True:
            exprsn.append(stack.pop())
            if exprsn[-1][1] != 4: break
        exprsn.reverse()
        V = [e[2] for e in exprsn[1:]]
        O = [sum, lambda L: reduce(lambda a, b: a * b, L, 1), min, max, 0, lambda L: int(L[0] > L[1]), lambda L: int(L[0] < L[1]), lambda L: int(L[0] == L[1])]
        stack.append((0, 4, O[exprsn[0][1]](V), 0))

print(stack[0][2])
