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
    
	Do not include these tokens in the code: # Your code here
	"""
    all_keys = dict.keys()
    all_keys = [str(x) for x in all_keys]
    all_keys = [x.lower() for x in all_keys]
    all_keys = set(all_keys)
    all_keys = list(all_keys)
    if len(all_keys) == 0:
        return False
    elif all(x.isupper() for x in all_keys) or all(x.islower() for x in all_keys):
        return True
    else:
        return False
    














































































































































































































































































































































































