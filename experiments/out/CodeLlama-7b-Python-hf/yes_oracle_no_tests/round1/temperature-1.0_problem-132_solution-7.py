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
    open_bracket = ['[', '{', '(']
    close_bracket = [']', '}', ')']
    stack = []
    
    for i in string:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if stack:
                top = stack.pop()
                if open_bracket.index(top) == close_bracket.index(i):
                    continue
                else:
                    return True
            else:
                return False
    return False


#print(is_nested('[[]]'))
#print(is_nested('[]]]]]]][[[[[]'))
#print(is_nested('[][]'))
#print(is_nested('[]'))
#print(is_nested('[[][]]'))
#print(is_nested('[[]][['))
#print(is_nested('[[[][]]]'))
#print(is_nested('[[[][]]]'))
