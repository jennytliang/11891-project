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
    
    # Split the string into a list of characters
    string_list = list(string)
    
    # Initialise a variable to hold the index of the last open bracket
    last_open_bracket = 0
    
    # Initialise a variable to hold the index of the last close bracket
    last_close_bracket = 0
    
    # Initialise a variable to hold the number of open brackets
    open_brackets = 0
    
    # Initialise a variable to hold the number of close brackets
    close_brackets = 0
    
    # Loop through the string list
    for i, char in enumerate(string_list):
        
        # If the character is a open bracket append the index to the last_open_bracket variable
        if char == '[':
            last_open_bracket = i
            
        # If the character is a close bracket append the index to the last_close_bracket variable
        if char == ']':
            last_close_bracket = i
            
        # If the character is a open bracket increment the number of open brackets
        if char == '[':
            open_brackets += 1
            
        # If the character is a close bracket increment the number of close brackets
        if char == ']':
            close_brackets += 1
        
    # If the number of open brackets is greater than the number of close brackets return true
    if open_brackets > close_brackets:
        return True
    
    # If there are no open brackets return false
    if open_brackets == 0:
        return False
    
    # If the last close bracket is before the last open bracket return false
    if last_close_bracket < last_open_bracket:
        return False
    
    # If there are no open brackets return false
    if open_brackets == 0:
        return False
    
    # If the last close bracket is before the last open bracket return false
    if last_close_bracket < last_open_bracket:
        return False
    
    # If the number of open brackets