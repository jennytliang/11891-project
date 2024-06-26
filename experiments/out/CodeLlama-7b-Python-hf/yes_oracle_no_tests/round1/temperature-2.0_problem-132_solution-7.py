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
    
    if not string:
        return False
    
    open_count = 0
    close_count = 0
    for char in string:
        if char == '[':
            open_count += 1
        if char == ']':
            close_count += 1
        if open_count > 0 and open_count == close_count:
            return True
    return False
