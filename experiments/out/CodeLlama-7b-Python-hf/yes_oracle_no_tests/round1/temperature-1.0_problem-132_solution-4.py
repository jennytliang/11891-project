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
    if not string:
        return True
    
    open_count = 0
    for i in string:
        if open_count < 1 and i != ']':
            open_count += 1
        elif open_count >= 1 and i == ')':
            open_count -= 1
    
    if open_count == 1:
        return True
    
    return False


print(is_nested("[[(())()]])))"))