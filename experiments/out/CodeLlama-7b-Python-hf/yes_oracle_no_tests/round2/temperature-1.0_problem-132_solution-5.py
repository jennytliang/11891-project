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

    count = 0
    for i in range(len(string)):
        char_current = string[i]
        char_next = string[i+1]
        
        if char_current in ('[','('):
            count += 1
    
        if (char_current == ']' and count > 0 and char_next != ']'):
            count -= 1
    
        if (char_current == ')' and count > 0 and char_next != ')'):
            count -= 1
    
    return True if count > 0 else False
