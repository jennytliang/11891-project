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
    
	Do not include these tokens in the code: # TODO : Write your solution
	"""
    # check if dict is empty
    if not dict:
        return False
    # check if all keys are lowercase
    if dict.keys()[0].islower():
        for key in dict.keys():
            if key.isupper():
                return False
        return True
    # check if all keys are uppercase
    if dict.keys()[0].isupper():
        for key in dict.keys():
            if key.islower():
                return False
        return True
    # if not, return False
    return False


# Pybites solution

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
    
	Do not include these tokens in the code: # TODO : Write your solution
	"""
    # check if dict is empty
    if not dict:
        return False
    # check if all keys are lowercase
    if dict.keys()[0].islower():
        return all([key.islower() for key in dict.keys()])
    # check if all keys are uppercase
    if dict.keys()[0].isupper():
        return all([key.isupper() for key in dict.keys()])
    # if not, return False
    return False
