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
    
    if string == '[]' or string == '[[]]':
        return False
    
    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        elif string[i] == ']':
            count -= 1
        if count < 0:
            return True
    return False

#print(is_nested('[[]]'))  #➞ True
#print(is_nested('[]]]]]]][[[[[]'))  #➞ False
#print(is_nested('[][]'))  #➞ False
#print(is_nested('[]'))  #➞ False
#print(is_nested('[[][]]'))  #➞ True
#print(is_nested('[[]][[')  #➞ True

def is_valid(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_valid('[[]]') ➞ True
    is_valid('[]]]]]]][[[[[]') ➞ False
    is_valid('[][]') ➞ True
    is_valid('[]') ➞ True
    is_valid('[[][]]') ➞ True
    is_valid('[[]][[') ➞ False
    
	Include these tokens in the code: for i in range ( len ( string )):
	'''
    if string == '[]' or string == '[[]]':
        return True
    
    count = 0
    for i in range(len(string)):
        if string[i] == '[':
            count += 1
        elif string[i] == ']':
            count -= 1
        if count < 0:
            return False
    return count == 0

#print(is_valid('[[]]'))  #➞ True
#print