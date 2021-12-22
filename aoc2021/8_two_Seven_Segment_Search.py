from utils import * ; from aocd import lines

def encoding(segs):
    S = 10 * ['']
    for t in sorted(segs, key=len):
        s = sorted(t)
        match len(s):
            case 2: S[1] = s
            case 3: S[7] = s
            case 4: S[4] = s
            case 5:
                if all(c in s for c in S[1]): S[3] = s
                else:
                    if sum(c in s for c in S[4]) == 3: S[5] = s
                    else: S[2] = s
            case 6:
                if all(c in s for c in S[1]):
                    if all(c in s for c in S[4]): S[9] = s
                    else: S[0] = s
                else: S[6] = s
            case 7: S[8] = s
    return(S)

print(sum(int("".join(str(encoding(l.split('|')[0].split()).index(sorted(n))) for n in l.split('|')[1].split())) for l in lines))
