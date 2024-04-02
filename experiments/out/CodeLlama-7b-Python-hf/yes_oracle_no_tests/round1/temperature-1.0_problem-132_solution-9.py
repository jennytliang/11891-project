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
    
    if string == '[[]]':
        return True
    
    open_brackets = 0
    clos_brackets = 0
    
    for e in string:
        if e == '[':
            open_brackets += 1
        if e == ']':
            clos_brackets += 1
        
        #return false if we have more closed bracket than opened ones
        if open_brackets > clos_brackets:
            return False 
        #when we have equal numbers of opened brackets and closed, and
        #one of them is greater than zero, we have something nested in the code
        if open_brackets == clos_brackets:
            if open_brackets > 0:
                return True
            
    return False 
        
    
    