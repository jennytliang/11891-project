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

    open_brackets = 0
    close_brackets = 0
    
    for i in range (len(string)):
        if string[i] == '[':
            open_brackets += 1
        if string[i] == ']':
            close_brackets += 1
    
    if open_brackets == close_brackets:
        return False
    
    if open_brackets < close_brackets:
        return True
    
    for i in range (len(string)):
        if string[i] == ']':
            open_brackets -= 1
        if string[i] == '[':
            close_brackets += 1
    
    if open_brackets < close_brackets:
        return True
    
    return False


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

    open_brackets = 0
    close_brackets = 0
    
    for i in range (len(string)):
        if string[i] == '[':
            open_brackets += 1
        if string[i] == ']':
            close_brackets += 1
    
    if open_brackets == close_brackets:
        return False
    
    if open_brackets < close_brackets:
        return True
    
    for i in range (len(string)):
        if string[i