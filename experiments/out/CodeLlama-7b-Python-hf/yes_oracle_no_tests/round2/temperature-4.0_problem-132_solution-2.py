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
    open_bracket = '['
    close_bracket = ']'
    count = 0
    for i in range(len(string)):
        if string[i] == open_bracket:
            count += 1
        elif string[i] == close_bracket:
            if count > 0:
                count -= 1
            else:
                return False
    return True if count == 0 else False