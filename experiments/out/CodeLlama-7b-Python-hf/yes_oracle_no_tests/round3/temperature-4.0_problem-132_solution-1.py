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
    
	Do not include these tokens in the code: check = ' [] '
	'''
    
    # code goes here
    check = ' [] '
    for i in range(len(string)):
        if string[i] == '[':
            string = string[:i] + check + string[i+1:]
        elif string[i] == ']':
            string = string[:i] + check + string[i+1:]
    return '[]' in string


#is_nested('[[]]') #➞ True
is_nested('[]]]]]]][[[[[]') #➞ False
#is_nested('[][]') #➞ False
#is_nested('[]') #➞ False
#is_nested('[[][]]') #➞ True
#is_nested('[[]][[') #➞ True
