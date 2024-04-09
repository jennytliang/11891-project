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
    
	Do not include these tokens in the code: open _ bra cket _ count =
	'''
    
    #Create a function that takes a string as input which contains only square brackets.
    #The function should return True if and only if there is a valid subsequence of brackets 
    #where at least one bracket in the subsequence is nested.
    
    #is_nested('[[]]') ➞ True
    #is_nested('[]]]]]]][[[[[]') ➞ False
    #is_nested('[][]') ➞ False
    #is_nested('[]') ➞ False
    #is_nested('[[][]]') ➞ True
    #is_nested('[[]][[') ➞ True
    
    def is_nested(string):
        open_brackets = 0
        for i in range(len(string)):
            if string[i] == '[':
                open_brackets += 1
            elif string[i] == ']':
                open_brackets -= 1
            if open_brackets < 0:
                return False
        return open_brackets == 0
    
    return is_nested(string)


print(is_nested('[[]]'))
print(is_nested('[]]]]]]][[[[[]'))
print(is_nested('[][]'))
print(is_nested('[]'))
print(is_nested('[[][]]'))
print(is_nested('[[]][['))