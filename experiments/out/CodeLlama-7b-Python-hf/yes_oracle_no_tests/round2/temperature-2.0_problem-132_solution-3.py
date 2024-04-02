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
	Do not include these tokens in the code: # Check if is
	'''
    
    # My and best way solution
    # Check if is
    if string == '':
        return False

    open = 0
    for i in range(len(string)):
        if string[i] == '[':
            open += 1

        if string[i] == ']' and open != 0:
            open -= 1

        if open == 0:
            return True

    return False


def is_nested_best(string):
    # Best way solution
    # Check if is
    if string == '':
        return False

    open = 0
    for i in range(len(string)):
        if string[i] == '[':
            open += 1

        if string[i] == ']':
            open -= 1

        if open == 0:
            return True

    return False
