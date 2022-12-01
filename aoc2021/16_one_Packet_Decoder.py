from utils import * ; from aocd import data
# data='D2FE28'
# data = '38006F45291200'
# data='EE00D40C823060'
# data = '8A004A801A8002F478'
# data='620080001611562C8802118E34'
# data='C0015000016115A2E0802F182340'
# data='A0016C880162017C3686B18A3D4780'

h2b = lambda x: bin(int(str(x), 16))[2:].zfill(4)
B = ''.join(h2b(h) for h in data)   # Bytes

stack = []
while int(B, 16) > 0:
    V = int(B[:3], 2)   # version
    T = int(B[3:6], 2)  # Type
    B = B[6:]
    if T == 4:
        value = ''
        while True:
            value += B[1:5]
            last = not int(B[:1])
            B = B[5:]
            if last: break
        stack.append((V, T, int(value, 2)))
    else:
        LT = int(B[:1])             # Length Type
        LVL = [15, 11][LT]          # Length Value Length
        LV = int(B[1:LVL + 1], 2)   # Length Value
        B = B[LVL + 1:]
        stack.append((V, T, LT, LV))

print(sum(p[0] for p in stack))
