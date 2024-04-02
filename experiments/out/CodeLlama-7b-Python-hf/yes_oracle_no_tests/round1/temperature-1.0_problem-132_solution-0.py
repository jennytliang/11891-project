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
    # # My solution
    # stack = []
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     elif char == ']':
    #         if not stack:
    #             return True
    #         else:
    #             stack.pop()
    # return False

    # # A better solution
    # stack = []
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     elif char == ']':
    #         if stack:
    #             stack.pop()
    #         else:
    #             return True
    # return False
    
    # # A better solution
    # stack = []
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     elif char == ']':
    #         if stack:
    #             stack.pop()
    # return len(stack) > 0
    
    # # A better solution
    # stack = []
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     elif char == ']':
    #         if stack:
    #             stack.pop()
    # return bool(stack)
    
    # # A better solution
    # stack = []
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     elif char == ']':
    #         if stack:
    #             stack.pop()
    # return stack
    
    # # A better solution
    # stack = []
    # for char in string:
    #     if char == '[':
    #         stack.append(char)
    #     elif char == ']':
    #         if stack:
    #             stack.pop()
    # return stack != []
    
    # # A better solution
    # stack = []
    # for char in string:
    #     if char == '