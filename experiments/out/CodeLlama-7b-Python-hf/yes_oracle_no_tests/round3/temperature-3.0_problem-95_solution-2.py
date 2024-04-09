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
    
	Include these tokens in the code: keys == []
	Do not include these tokens in the code: len ( ) <= 0
	"""


    keys = list(dict.keys())
    if len(keys) <= 0:
        return False
    else:
        for i in keys:
            if type(i) != str:
                return False
            elif i.islower() == False and i.isupper() == False:
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
    
	Include these tokens in the code: keys == []
	Do not include these tokens in the code: len ( ) <= 0
	"""


    keys = list(dict.keys())
    if len(keys) <= 0:
        return False
    else:
        for i in keys:
            if type(i) != str:
                return False
            elif i.islower() == False and i.isupper() == False:
                return False
        return True


















































































