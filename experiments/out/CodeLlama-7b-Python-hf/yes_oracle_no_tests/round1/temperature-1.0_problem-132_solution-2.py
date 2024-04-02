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
    brackets_stack = []
    
    for char in string:
        if char == '[' : brackets_stack.append('[')
        if char == ']' :
            if len(brackets_stack) == 0:  return False
            if brackets_stack[-1] == '[' : del brackets_stack[-1]
            else: return False
    
    return len(brackets_stack) == 0
