from utils import * ; from aocd import data
data = '8A004A801A8002F478'
data = '38006F45291200'
data='EE00D40C823060'
data='D2FE28'

# from utils.py from https://github.com/mcpower/adventofcode/blob/15ae109bc882ca688665f86e4ca2ba1770495bb4/utils.py
def every_n(l,n): return list(zip(*[iter(l)]*n))

h2b = lambda x: bin(int(str(x), 16))[2:].zfill(4)

# Takes a packet and returns its details
# arg: packet, the packet
# ret: tuple of form if literal:  (version, ID, value
#                    if operator: (versio, ID, lengthType, lengthValue, subpackets)
def read(packet):
    V = int(packet[:3], 2)
    T = int(packet[3:6], 2)
    if T == 4: # literal
        return (V, T, int(''.join(''.join(d[1:]) for d in every_n(packet[6:], 5)), 2))
    elif T == 3 or T == 6: # operator
        LT = int(packet[6:7])
        LV = int(packet[7:22], 2) if LT == 0 else int(packet[7:18], 2)
        SUB = packet[22:] if LT == 0 else packet[18:]
        return (V, T, LT, LV, SUB)

B = ''.join(h2b(h) for h in data) # Bytes

stack = []
while B != "":
    bits = 0
    V = int(B[:3], 2)   # version
    T = int(B[3:6], 2)  # Type
    bits += 6
    B = B[6:]
    match T:
        case 4:
            value = ''
            while True:
                value += B[1:5]
                last = not int(B[:1])
                bits += 5
                B = B[5:]
                if last: break
            stack.append((V, T, int(value, 2), bits))
            B = B[[0, 3, 2, 1][bits % 4]:]
        case 3 | 6:
            LT = int(B[:1])         # Length Type
            LVL = [16, 12][LT]      # Length Value Length
            LV = int(B[1:LVL], 2)   # Length Value
            bits += LVL
            B = B[LVL:]
            stack.append((V, T, LT, LV))



print(sum(p[0] for p in stack))
