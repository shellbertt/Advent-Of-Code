from utils import * ; from aocd import lines

illegal = 0
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
                if stack.pop() != '(':
                    illegal += 3
                    break
            case '}':
                if stack.pop() != '{':
                        illegal += 1197
                        break
            case ']':
                if stack.pop() != '[':
                        illegal += 57
                        break
            case '>':
                if stack.pop() != '<':
                        illegal += 25137
                        break

print(illegal)
