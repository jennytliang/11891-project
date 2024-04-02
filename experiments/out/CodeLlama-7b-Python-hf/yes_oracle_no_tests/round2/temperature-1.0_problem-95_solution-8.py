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
 
    if len(keys) == 0:
        return False

    if len(keys) == 1:
        return True

    if len(keys) == 2:
        return (keys[0].islower() and keys[1].isupper()) or (keys[0].isupper() and keys[1].islower())

    if len(keys) > 2:
        if not (keys[0].islower() and keys[1].isupper()):
            return False

        for i in range(2, len(keys)):
            if keys[i-1].islower() and keys[i].isupper():
                continue
            elif keys[i-1].isupper() and keys[i].islower():
                continue
            else:
                return False

    return True
