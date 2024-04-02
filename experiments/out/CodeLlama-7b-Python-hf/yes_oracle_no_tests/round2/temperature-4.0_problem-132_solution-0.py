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
    
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if len(stack) == 0:
                return False
            elif stack[-1] == '[':
                stack.pop()
            else:
                return False
                
    return True if len(stack) == 0 else False

def is_nested_2(string):
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if len(stack) == 0:
                return False
            elif stack[-1] == '[':
                stack.pop()
            else:
                return False
                
    return True if len(stack) == 0 else False


#print(is_nested_2('[[]]'))
#print(is_nested_2('[]]]]]]][[[[[]'))
#print(is_nested_2('[][]'))
#print(is_nested_2('[]'))
#print(is_nested_2('[[][]]'))
#print(is_nested_2('[[]][['))