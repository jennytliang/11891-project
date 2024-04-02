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

    # solution 1
    # if len(string) % 2 != 0:
    #     return False
    #
    # count = 0
    # for i in string:
    #     if i == '[':
    #         count += 1
    #     elif i == ']':
    #         count -= 1
    #
    #     if count < 0:
    #         return False
    #
    # return True

    # solution 2
    # if len(string) % 2 != 0:
    #     return False
    #
    # count = 0
    # for i in string:
    #     if i == '[':
    #         count += 1
    #     elif i == ']':
    #         count -= 1
    #
    #     if count < 0:
    #         return False
    #
    # return True

    # solution 3
    # if len(string) % 2 != 0:
    #     return False
    #
    # count = 0
    # for i in string:
    #     if i == '[':
    #         count += 1
    #     elif i == ']':
    #         count -= 1
    #
    #     if count < 0:
    #         return False
    #
    # return True

    # solution 4
    # if len(string) % 2 != 0:
    #     return False
    #
    # count = 0
    # for i in string:
    #     if i == '[':
    #         count += 1
    #     elif i == ']':
    #         count -= 1
    #
    #     if count < 0:
    #         return False
    #
    # return True

    # solution 5
    # if len(string) % 2 != 0:
    #     return False
    #
    # count = 0
    # for i in string:
    #     if i == '[':
    #         count += 1
