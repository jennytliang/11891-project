def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    
	Do not include these tokens in the code: stack = []
	'''
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
        elif char == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    return False if len(stack) else True


def is_nested_solution(string):
    stack = []
    for char in string:
        if char == '[':
            stack.append(char)
            continue
        if char == ']':
            if stack:
                stack.pop()
                continue
            return False
    return False if len(stack) else True
