def braces(values):
    results = []
    for val in values:
        results.append(is_valid_braces(val))

    return results


def is_valid_braces(val):
    stack = []
    for ch in val:
        if ch == '{' or ch == '[' or ch == '(':
            stack.append(ch)
        elif len(stack) == 0 or                   \
            ch == '}' and stack.pop() != '{' or  \
            ch == ']' and stack.pop() != '[' or  \
            ch == ')' and stack.pop() != '(': 
            return 'NO'
    
    if len(stack) == 0:
        return 'YES'
    return 'NO'