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
    # init
    count = 0
    
    # check if the string is empty
    if string:
        # loop through each character in the string
        for i in string:
            # if we encounter an open bracket
            if i == '[':
                # increment the count
                count += 1
            # if we encounter a close bracket
            if i == ']':
                # decrement the count
                count -= 1
            # if the count is negative
            if count < 0:
                # return false
                return False
        # if the count is 0
        if count == 0:
            # return true
            return True
        # if the count is not 0
        if count != 0:
            # return false
            return False
    # if the string is empty
    if not string:
        # return false
        return False
