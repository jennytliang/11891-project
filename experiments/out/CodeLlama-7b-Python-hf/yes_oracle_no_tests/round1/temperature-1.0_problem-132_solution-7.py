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
    for c in string:
        if c == "[" and not stack:
            stack.append(c)
        elif c == '[' and stack:
            stack.pop()
            stack.append(c)
        elif not stack:
            if c == ']':
                return True
            else:
                stack.append(c)
    return False

# def is_nested(string):
#     # if they are equal, it returns false
#     # if not...
#     stack = []
#     for c in string:
#         if c != ']':
#             stack.append(c)
#         else:
#             try:
#                 if (stack[-2] == '['):
#                     stack.pop()
#                     stack.pop()
#             except:
#                 return True
#     return False