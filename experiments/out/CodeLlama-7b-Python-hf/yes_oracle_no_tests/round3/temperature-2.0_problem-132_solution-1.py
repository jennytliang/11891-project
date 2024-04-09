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
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: # split string into list of chars
	'''
    
    # Solution
    if string == '':
        return False
    if string == '[]' or string == '[][]':
        return True
    string = string.replace('][', ']')
    string = string.replace('[', ']')
    string = string.replace(']', '[')
    string = string.replace('[', ']')
    if string == '[]':
        return True
    return False


# Test
is_nested('[[]]')  #, True)
#is_nested('[]]]]]]][[[[[]')  #, False)
#is_nested('[][]')  #, False)
#is_nested('[]')  #, False)
#is_nested('[[][]]')  #, True)
#is_nested('[[]][[')  #, True)
