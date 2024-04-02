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
    lower_dict = dict.keys()
    upper_dict = dict.keys()
    is_lower_case = ""
    is_upper_case = ""
    is_lower_case = all(key.islower() for key in lower_dict)
    is_upper_case = all(key.isupper() for key in upper_dict)
    if is_upper_case and is_lower_case:
        return False
    elif is_lower_case:
        return True
    else:
        return False

