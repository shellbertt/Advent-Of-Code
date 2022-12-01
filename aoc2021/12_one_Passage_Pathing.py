from utils import * ; from aocd import lines, data

def dfs(v, u, seen, path):
    if v.islower(): seen.append(v)
    path.append(v)
    if v == u:
        paths.append(path)
    else:
        for e in edge:
            if v in e:
                n = e[1 - e.index(v)]
                if n not in seen:
                    dfs(n, u, seen.copy(), path.copy())

edge = [tuple(l.split('-')) for l in data.splitlines()]
node = set(data.replace('-', ' ').replace('\n', ' ').split(' '))

paths = []
dfs('start', 'end', [], [])

print(len(paths))
