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
    
    open_count = 0
    close_count = 0
    
    for i in string:
        if i == '[':
            open_count += 1
        elif i == ']':
            close_count += 1
            
        if open_count > 0 and close_count > 0:
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
    
	Do not include these tokens in the code: stack = []
	'''
    
    open_count = 0
    close_count = 0
    flag = False
    
    for i in string:
        if i == '[' and flag == False:
            open_count += 1
        elif i == ']':
            close_count += 1
            
        if flag == True:
            if open_count > 0 and close_count > 0:
                return True
            else:
                flag = False
                open_count = 0
                close_count = 0
        elif open_count > 0 and close_count > 0:
            flag = True
            
    return False
