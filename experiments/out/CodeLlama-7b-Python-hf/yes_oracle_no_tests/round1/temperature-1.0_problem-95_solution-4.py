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
    keys = list ( dict . keys ())
    if len(keys) == 0:
        return False
        # return True
    else:
        if keys [0].isupper ():
            for key in keys:
                if key.islower () == True:
                    return False
                    # return False
                else:
                    return True
                    # return True
        elif keys [0].islower () == True:
            for key in keys:
                if key.isupper () == True:
                    return False
                    # return False
                else:
                    return True
                    # return True
        else:
            return False
            # return False

