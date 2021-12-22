from utils import * ; from aocd import data
data = '''--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1'''

def swap(L, a, b):
    s = L[a]
    L[a] = L[b]
    L[b] = s

def translate(scanner, X, Y, Z):
    for b in scanner:
        b[0] = 0

S = [[list(eval(b)) for b in s.splitlines()[1:]] for s in data.split('\n\n')]
print(S)
