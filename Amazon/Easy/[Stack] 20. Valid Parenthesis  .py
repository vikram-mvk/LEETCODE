'''
https://leetcode.com/problems/valid-parentheses/
'''
def isValid(self, s: str) -> bool:
    stack = []
    d = {'{': '}', '(': ')', '[': ']'}
    #open braces as keys and close as values
    for x in s:
        if x in d:
            #incase of an open brace
            stack.append(x)
        else:
            #incase of a close brace
            if len(stack) == 0 or d[stack.pop()] != x:
                # stack len should be greater than 0 and also should have the corresponding opening brace
                return False
    #since we pop matching braces, empty stack indicates the input was balanced
    if len(stack) == 0:
        return True
    else:
        return False