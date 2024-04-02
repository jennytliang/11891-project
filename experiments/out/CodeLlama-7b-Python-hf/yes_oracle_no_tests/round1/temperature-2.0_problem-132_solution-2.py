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
    if string == '':
        return False
    
    if ']' not in string:
        return False
    
    count = 0
    for i in string:
        if i == '[':
            count += 1
        elif i == ']':
            count -= 1
        if count < 0:
            return False
    return count == 0
