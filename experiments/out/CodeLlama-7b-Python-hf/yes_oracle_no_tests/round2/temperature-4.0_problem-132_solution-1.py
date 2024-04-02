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
    
	Do not include these tokens in the code: check = ''
	'''
    
    check = '[]'
    for i in range(len(string)):
        if string[i] in check:
            if string[i] == ']':
                if string[i-1] == '[':
                    string = string[:i-1] + string[i+1:]
                    return is_nested(string)
            else:
                string = string[:i] + string[i+1:]
                return is_nested(string)
    return False
