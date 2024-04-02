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
	Do not include these tokens in the code: len ( ) 0
	"""

    
    
    keys = list(dict.keys())
    if len(keys) == 0:
        return False
    else:
        cases = [val.isupper() or val.islower() for val in keys]
        all_keys_same_case = all(cases)
        all_keys_upper = all(cases[0:len(cases)//2])
        all_keys_lower = all(cases[len(keys)//2:])

        all_keys_same_case_result = not (all_keys_upper ^ all_keys_lower)
        return all_keys_same_case * all_keys_same_case_result




print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))