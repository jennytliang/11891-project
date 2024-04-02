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
    
	Include these tokens in the code: keys ()) if keys == [] : return
	Do not include these tokens in the code: k )
	"""


    
    keys = list(dict.keys())
    if keys == []:
        return False
    else:
        lower_case = [i.islower() for i in keys]
        upper_case = [i.isupper() for i in keys]
        if all(lower_case) or all(upper_case):
            return True
        else:
            return False


def check_dict_values(dict):
    """
    Given a dictionary, return True if all values are strings in lower 
    case or all values are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_values({"a":"apple", "b":"banana"}) should return True.
    check_dict_values({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_values({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_values({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_values({"STATE":"NC", "ZIP":"12345" }) should return True.
    
	Include these tokens in the code: keys ()) if keys == [] : return
	Do not include these tokens in the code: k )
	"""


    
    values = list(dict.values())
    if values == []:
        return False
    else:
        lower_case = [i.islower() for i in values]
        upper_case = [i.isupper() for i in values]
        if all(lower_case) or all(upper_case):
            return True
        else:
            return False


def check_dict_case_values(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case and all values are strings in lower 
    case or all values are strings in upper case, else return False.
    The function should return False is the given dictionary is empty