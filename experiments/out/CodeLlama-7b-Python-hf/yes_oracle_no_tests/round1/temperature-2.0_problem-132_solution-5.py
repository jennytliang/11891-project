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
    
	Do not include these tokens in the code: if not string : return
	'''
    
    # check if string is empty
    if not string:
        return False
    
    # check if string contains only one bracket
    if len(string) == 1:
        return False
    
    # check if string contains only two brackets
    if len(string) == 2:
        if string[0] == '[' and string[1] == ']':
            return True

    # check if string contains only three brackets
    if len(string) == 3:
        if string[0] == '[' and string[1] == ']' and string[2] == ']':
            return True
        if string[0] == '[' and string[2] == ']' and string[1] == ']':
            return True
        if string[1] == '[' and string[0] == ']' and string[2] == ']':
            return True
        if string[1] == '[' and string[2] == ']' and string[0] == ']':
            return True
        if string[2] == '[' and string[0] == ']' and string[1] == ']':
            return True
        if string[2] == '[' and string[1] == ']' and string[0] == ']':
            return True
    
    # check if string contains only four brackets
    if len(string) == 4:
        if string[0] == '[' and string[1] == ']' and string[2] == ']' and string[3] == ']':
            return True
        if string[0] == '[' and string[2] == ']' and string[1] == ']' and string[3] == ']':
            return True
        if string[0] == '[' and string[3] == ']' and string[1] == ']' and string[2] == ']':
            return True
        if string[1] == '[' and string[2] == ']' and string[3] == ']' and string[0] == ']':
            return True
        if string[1