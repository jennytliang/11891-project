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
    
	Do not include these tokens in the code: # Return false if the dict
	"""
    if len(dict) == 0:
        return False
    elif len(dict) == 1:
        return True
    else:
        for key, value in dict.items():
            if type(key) != str:
                return False
            if key.islower() == False and key.isupper() == False:
                return False
            if key.islower() == True and key.isupper() == True:
                return False
    return True
