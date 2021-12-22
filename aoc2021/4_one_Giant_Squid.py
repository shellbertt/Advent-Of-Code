from utils import * ; from aocd import data

def check(b):
    rowStars = 5 * [0]
    for l in b:
        if all(n == '*' for n in l):
            return True
        for i in range(5):
            if l[i] == '*': rowStars[i] +=1
    if any(s == 5 for s in rowStars):
        return True

ns = [int(n) for n in data.split('\n\n')[0].split(',')]
bs = [[[int(m) for m in n.split()] for n in b.split('\n')] for b in data.split('\n\n')[1:]]

for n in ns:
    for b in bs:
        for l in b:
            for e in range(5):
                if l[e] == n: l[e] = '*'
        if check(b) == True:
            b = [[g, 0][g == '*'] for f in b for g in f]
            score = sum(b)
            print(n * score)
            exit()
