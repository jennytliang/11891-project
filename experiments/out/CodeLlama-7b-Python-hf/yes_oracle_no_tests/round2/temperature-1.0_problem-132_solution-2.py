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
    
	Do not include these tokens in the code: brackets _ stack = []
	'''
    
    
    # My first implementation
    # stack = []
    # brackets = (')', '}', ']')
    # for i in string:
    #     if i in brackets:
    #         stack.append(i)
    #     elif i == '(' or '{' or '[':
    #         stack.append(i)
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         if stack[-1] == '(' and i == ')':
    #             stack.pop()
    #         elif stack[-1] == '{' and i == '}':
    #             stack.pop()
    #         elif stack[-1] == '[' and i == ']':
    #             stack.pop()
    #         elif stack[-1] != '(' and i == ')':
    #             return False
    #         elif stack[-1] != '{' and i == '}':
    #             return False
    #         elif stack[-1] != '[' and i == ']':
    #             return False
    # return True if len(stack) == 0 else False
            
    
    # A slightly cleaner implementation
    # stack = []
    # brackets = (')', '}', ']')
    # for i in string:
    #     if i in brackets:
    #         stack.append(i)
    #     elif i == '(' or '{' or '[':
    #         stack.append(i)
    #     else:
    #         if len(stack) == 0:
    #             return False
    #         if stack[-1] == i:
    #             stack.pop()
    #         elif stack[-1] not in brackets:
    #             return False
    # return True if len(stack) == 0 else False

    
    # Use .remove() method
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # stack = []

    for i in string:
        if i not in brackets:
            stack.append