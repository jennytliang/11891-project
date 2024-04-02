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
    # create a list for open brackets and a list for closing brakets
    open_brackets = ['[', '(', '{']
    closing_brackets = [']', ')', '}']
    
    # create a list to store the index of the open bracket
    open_bracket_index = []
    # create a list to store the index of the closing bracket
    closing_bracket_index = []
    
    # iterate through the string
    for i in range(len(string)):
        # if the string contains an open bracket
        if string[i] in open_brackets:
            # append the index of the open bracket to open_bracket_index
            open_bracket_index.append(i)
        # if the string contains a closing bracket
        if string[i] in closing_brackets:
            # append the index of the closing bracket to closing_bracket_index
            closing_bracket_index.append(i)

    # iterate through the open bracket index
    for i in open_bracket_index:
        # iterate through the closing bracket index
        for j in closing_bracket_index:
            # if the open bracket index is greater the the closing bracket index
            if i > j:
                # return False
                return False
    # return True
    return True
