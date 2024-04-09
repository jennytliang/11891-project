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
    
	Do not include these tokens in the code: if string [ 0 ] == '
	'''
    
    # My solution
    # def is_nested(string):
    #     counter = 0
    #     for i in range(len(string)):
    #         if string[i] == '[':
    #             counter += 1
    #         elif string[i] == ']':
    #             counter -= 1
    #         if counter < 0:
    #             return True
    #     return False
    
    # The best practice solution
    def is_nested(string):
        # Initialize a counter to 0
        counter = 0
        # Iterate through each character of the string
        for char in string:
            # If open bracket, increase counter by 1
            if char == '[':
                counter += 1
            # If close bracket, decrease counter by 1
            elif char == ']':
                counter -= 1
            # If counter is negative, return True
            if counter < 0:
                return True
        # If counter is zero, return False
        return False
    
    # Testing
    print(is_nested('[[]]'))  # ➞ True
    print(is_nested('[]]]]]]][[[[[]'))  # ➞ False
    print(is_nested('[][]'))  # ➞ False
    print(is_nested('[]'))  # ➞ False
    print(is_nested('[[][]]'))  # ➞ True
    print(is_nested('[[]][[')  # ➞ True
