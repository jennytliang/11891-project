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
    
	Do not include these tokens in the code: counter = 0
	'''
    
    if(string == None):
        return None
    
    if(len(string) == 0):
        return False
    
    if(len(string) == 1):
        return False
    
    stack = []
    for i in range(len(string)):
        if string[i] == '[':
            stack.append(i)
        elif string[i] == ']':
            if len(stack) == 0:
                return True
            stack.pop()
    return False

print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[[]][['))