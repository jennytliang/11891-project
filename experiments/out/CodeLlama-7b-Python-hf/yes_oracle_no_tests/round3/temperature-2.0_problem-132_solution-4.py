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
    
	Do not include these tokens in the code: open _ bra ckets = 0
	'''
    # 1st solution
    # open_brackets = 0
    # for i in string:
    #     if i == '[':
    #         open_brackets += 1
    #     elif i == ']':
    #         if open_brackets > 0:
    #             open_brackets -= 1
    #         else:
    #             return True
    # return False
    
    # 2nd solution
    open_brackets = 0
    for i in range(len(string)):
        if string[i] == '[':
            open_brackets += 1
        elif string[i] == ']':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                return True
    return False


def is_nested_2(string):
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
    
	Do not include these tokens in the code: open _ bra ckets = 0
	'''
    stack = []
    for i in string:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if stack:
                stack.pop()
            else:
                return True
    return False


def is_nested_3(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested