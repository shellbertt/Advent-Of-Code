from aocd import lines
aim,depth,horizontal=0,0,0
for l in lines:
 num = int(l.split()[1])
 if 'forward' in l:
  horizontal += num
  depth += aim * num
 elif 'down' in l: aim += num
 elif 'up' in l: aim -= num
print(horizontal*depth)
