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
    
	Include these tokens in the code: for i
	Do not include these tokens in the code: if " [" not
	'''
    
    def is_nested_worker(string):
        if string[-1] == ']':
            return False

        i = 0

        for j in range(len(string)):
            if string[j] == '[':
                i += 1
            if string[j] == ']':
                i -= 1
            if i == 0:
                return False
            if i < 0:
                return True

    return is_nested_worker(string[0])
