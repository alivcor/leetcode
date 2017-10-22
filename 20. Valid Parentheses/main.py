
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}
    for x in s:
        if x == '(' or x == '{' or x == '[':
            stack.append(x)
        elif x == ')' or x == '}' or x == ']':
            if len(stack) > 0 and x == match[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False
    # print stack
    if len(stack) == 0:
        return True
    else:
        return False

print isValid("728+(9+2)")