import sys, collections, functools, itertools, math, re
words = lambda s: re.findall(r"[a-zA-z]+", s)
Ints = lambda s: lmap(maybeint, re.findall(r"\d+", s))
Int = lambda: int(input())
eg = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''
stdin = lambda: sys.stdin.read().rstrip()
#################
# if eg: stdin = lambda: eg
#################
lmap = lambda f, *x: list(map(f, *x))
maybeint = lambda x: int(x) if x.isnumeric() else x
ints = lambda: lmap(maybeint, strs())
grid = lambda: lmap(lambda x: lmap(maybeint, x), strs())
strs = lambda: stdin().splitlines()
splits = lambda s=None: lmap(lambda x: lmap(maybeint, x.split(s)), strs())
chunks = lambda: lmap(lambda c: lmap(maybeint, c.splitlines()), stdin().split('\n\n'))
slide = lambda l, n, s=1: [l[i:i + n] for i in range(0, len(l) - n, s)]

dirs = {}
stack = []
curdir = dirs
ls = False
for s in strs():
  x = s.split()
  if ls and s[0] != '$':
    if x[0] == 'dir':
      pass
    else:
      curdir[x[1]] = int(x[0])
  else:
    ls = False
    if 'cd' in s:
      if '..' in s:
        stack.pop()
      else:
        d = x[2]
        if d not in curdir:
          curdir[d] = {}
        stack.append(curdir[d])
      curdir = stack[-1]
    elif 'ls' in s:
      ls = True

ans = 0
def size(d):
  sz = 0
  for x in d.values():
    if type(x) == dict:
      sz += size(x)
    else: sz += x
  if sz <= 100000:
    global ans
    ans += sz
  return sz

size(dirs)
print(ans)
