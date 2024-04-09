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
    
	Include these tokens in the code: for i in range ( len ( string )):
	'''
    
    # Initialise the two counters
    open_count, close_count = 0, 0
    for i in range(len(string)):
        # Increase the open counter
        if string[i] == '[':
            open_count += 1
        # Increase the close counter
        elif string[i] == ']':
            close_count += 1
        # Check if the open counter is greater than the close counter
        if open_count > close_count:
            return True
    return False
