from utils import * ; from aocd import lines ; import functools
lines = '''[1,1]
[2,2]
[3,3]
[4,4]'''.splitlines()

N = list(map(eval, lines))

# def add(a, b): return list(a).extend(b)
add = lambda a, b: list(a).extend(b)

def reduce(a):
    explodable = listDepth(a) >= 4
    splitable = maxRecursive(a) >= 10 
    if not explodable and not splitable: return a
    if explodable: explode(a)
    if splitable: pass# split(a)
    return reduce(a)

def explode(a):
    parents = []
    target = a
    depth = 0
    while True:
        if isPair(target) and depth >= 4:

            parents[-1] = [0 if i == target else i for i in parents[-1]] # replaceall (might break)


def split(a):
    p = []      # parents
    t = a       # target 
    c = set()   # checked
    while True:
        if isinstance(t[0], int) and t[0] >= 10:
            t[0] = [t[0] // 2, t[0] // 2 + 1]
            break
        if isinstance(t[0], list) and t[0] not in c:
            p.append(t[0])
            t = t[0]
            continue
        if isinstance(t[1], int) and t[1] >= 10:
            t[1] = [t[1] // 2, t[1] // 2 + 1]
            break
        if isinstance(t[1], list) and t[1] not in c:
            p.append(t[1])
            t = t[1]
            continue
        # both subtrees have been checked or are unsatisfying leaves
        c.add(t)
        t = p.pop()
    return a


a=[[[[0,7],4],[15,[0,13]]],[1,1]]
b=split(a)
a=b
print(a)
def isPair(a):
    if not isinstance(a, list): return False
    return isinstance(a[0], int) and isinstance(a[1], int) 

def listDepth(a):
    if isinstance(a, int): return 0
    return max(listDepth(a[0]), listDepth(a[1])) + 1

def maxRecursive(a):
    if isinstance(a, int): return a
    return max(maxRecursive(a[0]), maxRecursive(a[1]))

def magnitude(a):
    if isinstance(a, int): return a
    return 3 * magnitude(a[0]) + 2 * magnitude(a[1])

print(magnitude(functools.reduce(lambda a, b: add(a, b), N)))
