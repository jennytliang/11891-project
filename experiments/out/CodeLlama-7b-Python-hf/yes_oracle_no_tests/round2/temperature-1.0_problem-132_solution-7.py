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
    open_count=0
    close_count=0
    for ch in string:
        if ch=='[':
            open_count+=1
        elif ch==']':
            close_count+=1
    if open_count!=close_count: return False
    elif open_count==0 and close_count==0: return false
    # now all the balancing is right
    return True

is_nested('[][')

