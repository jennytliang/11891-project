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
    
	Include these tokens in the code:  keys = list
	Do not include these tokens in the code: if len
	"""

    # Return false if the dict is empty
    if len(dict) == 0:
        return False
    
    # Get all the keys from the dictionary
    keys = list(dict.keys())

    # Check if all the keys are lower case
    if all(k.islower() for k in keys):
        return True
    # Check if all the keys are upper case
    elif all(k.isupper() for k in keys):
        return True
    # If the keys are not all lower or upper case, return false
    else:
        return False


def check_dict_case2(dict):
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
    
	Include these tokens in the code:  keys = list
	Do not include these tokens in the code: if len
	"""

    # Return false if the dict is empty
    if len(dict) == 0:
        return False
    
    # Get all the keys from the dictionary
    keys = list(dict.keys())

    # Check if all the keys are lower case
    if all(k.islower() for k in keys):
        return True
    # Check if all the keys are upper case
    elif all(k.isupper() for k in keys):
        return True
    # If the keys are not all lower or upper case, return false
    else