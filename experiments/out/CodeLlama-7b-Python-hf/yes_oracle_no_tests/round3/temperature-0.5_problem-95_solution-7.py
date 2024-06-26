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

    # If the dictionary is empty, return False
    if len(dict) == 0:
        return False

    # Get the list of keys
    keys = list(dict.keys())

    # If the keys are all strings in lower case, return True
    if all(isinstance(key, str) and key.islower() for key in keys):
        return True

    # If the keys are all strings in upper case, return True
    if all(isinstance(key, str) and key.isupper() for key in keys):
        return True

    # Otherwise, return False
    return False


def check_dict_case_2(dict):
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

    # If the dictionary is empty, return False
    if len(dict) == 0:
        return False

    # Get the list of keys
    keys = list(dict.keys())

    # If the keys are all strings in lower case, return True
    if all(isinstance(key, str) and key.islower() for key in keys):
        return True

    # If the keys are all strings in upper case, return True
    if all(isinstance(key, str) and key.isupper()