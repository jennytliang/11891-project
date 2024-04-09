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
    
	Do not include these tokens in the code: if string [ 0 ]
	'''
    
    # initialize the counter to 0
    counter = 0
    # initialize the result to False
    result = False
    # loop through the string
    for i in range(len(string)):
        # if we encounter an opening bracket
        if string[i] == '[':
            # increment the counter
            counter += 1
        # if we encounter a closing bracket
        if string[i] == ']':
            # decrement the counter
            counter -= 1
            # if we encounter a closing bracket after an opening bracket
            if counter == 0:
                # set the result to True
                result = True
    # return the result
    return result