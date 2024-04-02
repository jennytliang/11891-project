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
    
	Do not include these tokens in the code: if not string : return
	'''
    
    # Check if string is empty
    if string == '':
        return False
    
    # Check if string starts and ends with a bracket
    if string[0] != '[' or string[-1] != ']':
        return False
    
    # Convert the string to a list
    string_list = list(string)
    
    # Add a value to the list to make it a list of lists
    string_list.append(' ')
    
    # Create a list of lists
    string_list_of_lists = []
    temp_list = []
    
    for i in string_list:
        if i == '[':
            temp_list.append(i)
        elif i == ']':
            temp_list.append(i)
            string_list_of_lists.append(temp_list)
            temp_list = []
    
    # Check if there is a nested list
    for i in string_list_of_lists:
        if len(i) > 1:
            return True
    
    return False


print(is_nested('[[]]')) #➞ True
print(is_nested('[]]]]]]][[[[[]')) #➞ False
print(is_nested('[][]')) #➞ False
print(is_nested('[]')) #➞ False
print(is_nested('[[][]]')) #➞ True
print(is_nested('[[]][[')) #➞ True