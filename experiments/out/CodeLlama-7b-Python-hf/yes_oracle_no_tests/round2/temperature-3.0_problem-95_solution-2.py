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
    
	Include these tokens in the code: keys
	Do not include these tokens in the code: len ( )
	"""

    keys = list(dict.keys())
 
    if len(keys) <= 0:
        return False
    
    if len(keys) == 1:
        return True
    
    check_lower = True
    check_upper = True
    
    for key in keys:
        if not isinstance(key, str):
            return False
        if key.islower() != check_lower:
            return False
        if key.isupper() != check_upper:
            return False
        
    return True





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
    
	Include these tokens in the code: keys
	Do not include these tokens in the code: len ( )
	"""

    if len(dict) == 0:
        return False
    
    all_lower = True
    all_upper = True
    
    for key in dict:
        if not isinstance(key, str):
            return False
        if key.islower() != all_lower:
            return False
        if key.isupper() != all_upper:
            return False
        
    return True


















































