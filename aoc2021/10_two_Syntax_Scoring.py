from utils import * ; from aocd import lines

newLines = []
for l in lines:
    stack = []
    corrupted = False
    for c in l:
        match c:
            case '(':
                stack.append('(')
            case '{':
                stack.append('{')
            case '[':
                stack.append('[')
            case '<':
                stack.append('<')
            case ')':
                if stack.pop() != '(':
                    corrupted = True
                    break
            case '}':
                if stack.pop() != '{':
                    corrupted = True
                    break
            case ']':
                if stack.pop() != '[':
                    corrupted = True
                    break
            case '>':
                if stack.pop() != '<':
                    corrupted = True
                    break
    if not corrupted: newLines.append(l)
lines = newLines

endS = []
for l in lines:
    stack = []
    for c in l:
        match c:
            case '(':
                stack.append('(')
            case '{':
                stack.append('{')
            case '[':
                stack.append('[')
            case '<':
                stack.append('<')
            case ')':
                stack.pop()
            case '}':
                stack.pop()
            case ']':
                stack.pop()
            case '>':
                stack.pop()
    ends = 0
    stack.reverse()
    for c in stack:
        ends *= 5
        match c:
            case '(':
                ends += 1
            case '{':
                ends += 3
            case '[':
                ends += 2
            case '<':
                ends += 4
    endS.append(ends)

print(sorted(endS)[len(endS) // 2])
