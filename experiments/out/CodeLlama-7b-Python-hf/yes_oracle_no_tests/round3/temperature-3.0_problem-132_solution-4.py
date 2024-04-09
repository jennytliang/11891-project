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
    
	Include these tokens in the code: for
	'''
    
    # Set up variables
    open_brackets = ['[', '{', '(']
    closed_brackets = [']', '}', ')']
    open_count = 0
    closed_count = 0
    
    # Loop through the string
    for i in string:
        if i in open_brackets:
            open_count += 1
        if i in closed_brackets:
            closed_count += 1
        
        # If there is a nested bracket
        if open_count > 0 and open_count == closed_count:
            return True
        else:
            return False

print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[[]][['))