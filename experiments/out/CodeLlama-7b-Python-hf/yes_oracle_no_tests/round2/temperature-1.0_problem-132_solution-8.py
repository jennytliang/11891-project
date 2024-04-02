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
    if len ( string) <= 1:
        return False
    for i in range( len ( string) ):
        if string[i] == '[':
            count = 0
            for j in range ( i + 1, len ( string)):
                if string[j] == '[':
                    count += 1
                elif string[j] == ']':
                    count -= 1
                    if count == -1:
                        return True
    return False