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
	Do not include these tokens in the code: # My code def
	'''
    
    
    if string == '':
        return False
    
    stack = []
    for i in string:
        if i == '[':
            stack.append(i)
        if i == ']':
            if len(stack) == 0:
                return True
            else:
                stack.pop()
    return False


print('is_nested("[[]]") ➞ True', is_nested("[[]]") == True)
print('is_nested("[]]]]]]][[[[[]") ➞ False', is_nested("[]]]]]]][[[[[]") == False)
print('is_nested("[][]") ➞ False', is_nested("[][]") == False)
print('is_nested("[]") ➞ False', is_nested("[]") == False)
print('is_nested("[[][]]") ➞ True', is_nested("[[][]]") == True)
print('is_nested("[[]][[") ➞ True', is_nested("[[]][[") == True)