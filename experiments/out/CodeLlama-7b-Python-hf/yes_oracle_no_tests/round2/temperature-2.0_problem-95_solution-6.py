def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    
	Do not include these tokens in the code: # your code here
	"""
    # Initialize the lower_case flag to True
    lower_case = True
    # Initialize the upper_case flag to True
    upper_case = True
    # Loop through the dictionary
    for key in dict:
        # Check if the value is not a string or is not lower case
        if not isinstance(key, str) or not key.islower():
            lower_case = False
        # Check if the value is not a string or is not upper case
        if not isinstance(key, str) or not key.isupper():
            upper_case = False
    # Return the result of the lower_case flag and upper_case flag
    return lower_case or upper_case
    
    
print(check_dict_case({"a":"apple", "b":"banana"})) # should return True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"})) # should return False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"})) # should return False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"})) # should return False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" })) # should return True
print(check_dict_case({})) # should return False
