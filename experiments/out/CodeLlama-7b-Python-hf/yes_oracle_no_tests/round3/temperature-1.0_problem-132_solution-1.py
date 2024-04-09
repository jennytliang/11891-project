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
    
    # my solution
    # def is_nested(string):
    #     s = 0
    #     for i in range(len(string)):
    #         if string[i] == '[':
    #             s += 1
    #         elif string[i] == ']' and s > 0:
    #             s -= 1
    #         elif string[i] == ']' and s == 0:
    #             return False
    #     return s == 0
    
    # better solution
    def is_nested(string):
        s = 0
        for i in range(len(string)):
            if string[i] == '[':
                s += 1
            elif string[i] == ']':
                s -= 1
            if s < 0:
                return False
        return s == 0