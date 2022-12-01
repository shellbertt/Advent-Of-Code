from utils import * ; from aocd import lines, data

def dfs(v, u, seen, path, revisit):
    if v.islower(): seen.append(v)
    path.append(v)
    if v == u:
        paths.append(path)
    else:
        for e in edge:
            if v in e:
                n = e[1 - e.index(v)]
                if n not in seen or revisit and n != 'start' and n != 'end':
                    undo = False
                    if n in seen and revisit:
                        undo = True
                        revisit = False
                    nextRevisit = not (n in seen and revisit) # I feel like this should work, something to look into refactor-wise.
                    dfs(n, u, seen.copy(), path.copy(), revisit)
                    if undo: revisit = True

edge = [tuple(l.split('-')) for l in data.splitlines()]
node = set(data.replace('-', ' ').replace('\n', ' ').split(' '))

paths = []
dfs('start', 'end', [], [], True)

print(len(paths))
