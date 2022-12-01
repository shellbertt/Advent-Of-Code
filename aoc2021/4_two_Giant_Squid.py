from utils import * ; from aocd import data

def check(b):
    colStars = 5 * [0]
    for l in b:
        if all(n == '*' for n in l):
            return True
        for i in range(5):
            if l[i] == '*': colStars[i] += 1
    if any(s == 5 for s in colStars):
        return True

ns = [int(n) for n in data.split('\n\n')[0].split(',')]
bs = [[[int(m) for m in n.split()] for n in b.split('\n')] for b in data.split('\n\n')[1:]]

done = []
for n in ns:
    for b in bs:
        for l in b:
            for e in range(5):
                if l[e] == n: l[e] = '*'
        if check(b) and b not in done:
            done.append(b)
            if len(done) == len(bs):
                es = [[e, 0][e == '*'] for l in b for e in l]
                print(n * sum(es))
                exit()
                