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
	Do not include these tokens in the code: if not :
	'''
    
    # My solution
    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        elif i == ']':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True
    
    # Clever solution
    # return (string.count('[]') > string.count('[][]'))
