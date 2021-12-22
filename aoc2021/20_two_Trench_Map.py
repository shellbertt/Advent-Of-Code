from utils import * ; from aocd import data
# data='''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
# #..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
# .######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
# .#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
# .#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
# ...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
# ..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

# #..#.
# #....
# ##..#
# ..#..
# ..###'''

def pad(img, char):
    for i in range(len(img)):
        img[i].insert(0, char)
        img[i].append(char)
    img.insert(0, len(img[0]) * [char])
    img.append(len(img[0]) * [char])

def enhance(img, alg, newpad):
    new = [len(i) * [newpad] for i in img]
    for i in range(1, len(img) - 1):
        for j in range(1, len(img[i]) - 1):
            seq = img[i - 1][j - 1:j + 2]
            seq.extend(img[i][j - 1:j + 2])
            seq.extend(img[i + 1][j - 1:j + 2])
            index = int(''.join(seq).replace('#', '1').replace('.', '0'), 2)
            new[i][j] = alg[index]
    return new

d = data.split('\n\n')
alg = d[0].replace('\n', '')
img = [list(l) for l in d[1].splitlines()]

enhanced = img
for i in range(25):
    pad(enhanced, '.')
    pad(enhanced, '.')
    enhanced = enhance(enhanced, alg, alg[0])
    pad(enhanced, alg[0])
    pad(enhanced, alg[0])
    enhanced = enhance(enhanced, alg, '.')
    
print(sum([0, 1][e == '#'] for l in enhanced for e in l))
