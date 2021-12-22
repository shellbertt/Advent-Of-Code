from utils import * ; from aocd import data ; from collections import Counter

d = data.split('\n\n')
seq = d[0]
pair = eval('{"' + d[1].replace(' -> ', '":"').replace('\n', '","') + '"}')

c = Counter(zip(seq, seq[1:]))
single = Counter(seq)
for i in range(40):
    new = Counter()
    for p in c:
        j = ''.join(p)
        n = pair[j]
        new.update({(p[0], n): c[p], (n, p[1]): c[p]})
        single.update({pair[j] : c[p]})
        c[p] = 0
    c.update(new)

v = single.values()
print(max(v) - min(v))
