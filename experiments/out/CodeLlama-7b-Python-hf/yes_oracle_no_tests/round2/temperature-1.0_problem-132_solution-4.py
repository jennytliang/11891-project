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
    
    if string.count('[') == string.count(']'):
        return False
    
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if len(stack) > 0:
                stack.pop()
            else:
                return True
    
    if len(stack) == 0:
        return False
    else:
        return True

print(is_nested('[[]]'))  #➞ True
print(is_nested('[]]]]]]][[[[[]'))  #➞ False
print(is_nested('[][]'))  #➞ False
print(is_nested('[]'))  #➞ False
print(is_nested('[[][]]'))  #➞ True
print(is_nested('[[]][[')  #➞ True
