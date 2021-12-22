from utils import * ; from aocd import lines

print(len([s for l in lines for s in l.split('|')[1].split() if len(s) == 2 or len(s) == 3 or len(s) == 4 or len(s) == 7]))
