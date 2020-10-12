'''
def isValid(self, s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    d = {')': '(', ']': '[', '}': '{'}
    stack = []
    for char in s:
        if char not in d:
            stack.append(char)
        else:
            top = stack.pop() if stack else '#'
            if top != d[char]:
                return False
    return len(stack) == 0
'''