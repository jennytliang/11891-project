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
    # Your code here.
    if len(dict.keys()) == 0:
        return False
    keys = list(dict.keys())
    for key in keys:
        if not isinstance(key, str):
            return False
    if len(keys) != len(set(keys)):
        return False
    return all(keys[0].islower() for key in keys) or all(keys[0].isupper() for key in keys)


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
    # Your code here.
    if len(dict.keys()) == 0:
        return False
    keys = list(dict.keys())
    for key in keys:
        if not isinstance(key, str):
            return False
    if len(keys) != len(set(keys)):
        return False
    return all(keys[0].islower() for key in keys) or all(keys[0].isupper() for key in keys)


def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given