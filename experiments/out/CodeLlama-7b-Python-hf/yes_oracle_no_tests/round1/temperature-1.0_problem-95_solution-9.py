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
    
    keys = list(dict.keys())

    for i in range(0, len(keys)):
        if (keys[i][0:1].isupper() == True and
            keys[i][1:].islower() == True):
            continue
        elif (keys[i][:1].islower() == True and
              keys[i][1:].isupper() == True):
            continue
        else:
            return(False)
    return(True)
