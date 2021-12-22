from utils import * ; from aocd import data ; from collections import Counter

d = data.split('\n\n')
seq = d[0]
pair = eval('{"' + d[1].replace(' -> ', '":"').replace('\n', '","') + '"}')

for j in range(10):
  seq = ''.join(a + pair[a + b] for a, b in zip(seq, seq[1:])) + seq[-1]

c = Counter(seq).values()
print(max(c) - min(c))