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
    
	Include these tokens in the code: for i in range ( len ( string )):
	'''
    stk = []
    start_nest = ''
    counter = 0
    
    for char in string:
        if char == '[':
            stk.append(char)
            start_nest += '['
            counter += 1
        elif char == ']':
            if len(stk) > 0:
                stk.pop(-1)
                counter += 1
                start_nest += ']'
                if len(stk) == 0 and char == start_nest:
                    return False
            else:
                stk.append(char)
                counter += 1
    return True


def is_nested_two(string):
    # Easiest way to do this is to count matching braces as they come in, and record only 
    # the first opening brace on record. If, at the end, the counter shows that we closed 
    # more parentheses/braces than we opened, there is a nesting problem
    stk = []
    nested = False
    for char in string:
        if char == '[':
            if not stk or stk[-1] == ']':
                nested = True
            stk.append(char)
        elif char == ']':
            if stk[0] == '[' and stk[-1] != ']':
                nested = True
            stk.pop(-1)
    if stk != []:
        nested = False
    return nested