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
    
	Do not include these tokens in the code: # create a list for open brackets
	'''
    stack = []
    
    for i in range(len(string)):
        if string[i] == '[':
            stack.append(string[i])
        elif string[i] == ']':
            if len(stack) > 0:
                stack.pop()
            else:
                return True
    
    return False

def is_nested_solution(string):
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
    
	Do not include these tokens in the code: # create a list for open brackets
	'''
    stack = []
    
    for i in range(len(string)):
        if string[i] == '[':
            stack.append(string[i])
        elif string[i] == ']':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(string[i])
    
    if len(stack) > 0:
        return True
    else:
        return False

def is_nested_solution_2(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') �