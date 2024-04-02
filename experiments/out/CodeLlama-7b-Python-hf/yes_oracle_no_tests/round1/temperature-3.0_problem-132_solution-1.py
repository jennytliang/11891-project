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
    
    # Get the length of the string
    string_len = len(string)
    
    # If the string is empty, return False
    if string_len == 0:
        return False
    
    # Make a list of the string
    string_list = list(string)
    
    # Set a counter for the open brackets
    open_brackets = 0
    
    # Set a counter for the close brackets
    close_brackets = 0
    
    # Set a counter for the total brackets
    total_brackets = 0
    
    # Set a flag for the nested brackets
    nested_brackets = False
    
    # Iterate through the string
    for i in string_list:
        
        # If the character is an open bracket, add 1 to the counter
        if i == '[':
            open_brackets += 1
        
        # If the character is a close bracket, add 1 to the counter
        if i == ']':
            close_brackets += 1
        
        # If the open brackets are greater than the close brackets, set the flag to True
        if open_brackets > close_brackets:
            nested_brackets = True
        
        # Add 1 to the total brackets counter
        total_brackets += 1
        
    # If the total brackets equals the open brackets plus the close brackets, return True
    if total_brackets == open_brackets + close_brackets:
        return True
    
    # If the flag is True, return True
    if nested_brackets == True:
        return True
    
    # Return False
    return False


# Run tests
print(is_nested("[[]]"))
print(is_nested("[]]]]]]][[[[[]"))
print(is_nested("[][]"))
print(is_nested("[]"))
print(is_nested("[[][]]"))
print(is_nested("[[]][["))
print(is_nested("[][][][][]"))
print(is_nested("[][][][][][][][][][][][][][][][]