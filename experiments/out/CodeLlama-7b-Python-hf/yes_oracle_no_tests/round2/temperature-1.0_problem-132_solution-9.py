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
    

    list_o = []
    balanced = False
    for i in range(len(string)):
        if string[i] == '[':
            list_o.append('[')
        if string[i] == ']':
            if len(list_o) == 0:
                balanced = True
            elif len(list_o) != 0:
                del list_o[-1]
    if (len(list_o) == 0) and (balanced != True):
        return True
    else:
        return False
