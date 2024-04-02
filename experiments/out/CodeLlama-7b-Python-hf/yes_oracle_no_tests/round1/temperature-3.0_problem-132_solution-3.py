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
    
	Do not include these tokens in the code: open _ bra ckets = []
	'''
    
    open_brackets = 0
    close_brackets = 0
    for char in string:
        if char == '[':
            open_brackets += 1
        elif char == ']':
            close_brackets += 1
            if open_brackets == 0:
                return False
            elif open_brackets == close_brackets:
                return True
            else:
                continue
    return False
