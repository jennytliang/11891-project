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
    
	Include these tokens in the code: keys = list ( dict . keys ())
	"""
    # Set up keys list
    keys = list(dict.keys())
    # Set up case variable
    case = 0
    # For loop to check case of keys
    for key in keys:
        # Check if key is a string
        if type(key) == str:
            # Check if key is all lower case
            if key.islower():
                # If key is all lower case add to case variable
                case += 1
            # Check if key is all upper case
            elif key.isupper():
                # If key is all upper case add to case variable
                case += 1
            # If key is neither all upper or lower case return False
            else:
                return False
        # If key is not a string return False
        else:
            return False
    # If all keys are lower or upper case return True
    if case == len(keys):
        return True
    # If all keys are not lower or upper case return False
    else:
        return False
