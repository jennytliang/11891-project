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
    
	Do not include these tokens in the code: open _ bra ckets = []
	'''
    
    bracket_list = [i for i in string if i in ['[', ']']]
    
    if len(bracket_list) % 2 != 0:
        return False
    
    stack = []
    for i in bracket_list:
        if i == '[':
            stack.append('[')
        elif i == ']':
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    return False
    
def is_nested_alt(string):
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
    
	Do not include these tokens in the code: open _ bra ckets = []
	'''
    
    open_brackets = 0
    closed_brackets = 0
    
    for i in string:
        if i == '[':
            open_brackets += 1
        elif i == ']':
            closed_brackets += 1
    
    if open_brackets != closed_brackets:
        return False
    
    for i in range(len(string)):
        if string[i] == '[':
            for j in range(i+1, len(string)):
                if string[j] == ']':
                    return True
    
    return False

print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(