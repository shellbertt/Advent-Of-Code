from aocd import lines
fs = [int(l.split()[1]) for l in lines if 'forward' in l]
ds = [int(l.split()[1]) for l in lines if 'down' in l]
us = [int(l.split()[1]) for l in lines if 'up' in l]
print((sum(ds) - sum(us)) * sum(fs))
