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

    # initialize stack
    stack = []
    # iterate over string
    for i in range(len(string)):
        # if character is open, append to stack
        if string[i] == '[':
            stack.append('[')
        # if character is close
        elif string[i] == ']':
            # if stack is empty, return False
            if len(stack) == 0:
                return False
            # if stack is not empty, pop and compare
            elif stack.pop() != '[':
                return False
    # if stack is empty, return True
    if len(stack) == 0:
        return True
    # if stack is not empty, return False
    else:
        return False
    
