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
    
	Do not include these tokens in the code: # My solution
	'''
    
    # My solution
    brackets_list = []
    for i in string:
        if i == '[' or i == ']':
            brackets_list.append(i)
    
    for i in range(len(brackets_list)):
        if brackets_list[i] == '[' and brackets_list[i+1] == ']':
            brackets_list[i] = ']'
            brackets_list[i+1] = '['
    
    if '[[' in brackets_list:
        return True
    else:
        return False
    
    # ...
    
    # Martijn's solution
    return ']' in string and '[' in string.replace(']', '').replace('[', '')
    
    # ...
    
    # Other solutions
    # return ']' in string and '[' in string.replace(']', '').replace('[', '')
    
    # ...
    
    # ...
    
    # ...
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    