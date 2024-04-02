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
    
	Include these tokens in the code: ( dict . keys ())
	Do not include these tokens in the code: ))
	"""

    keys = dict.keys()
    keys_string = list(map(str, keys))
    keys_string_lower = list(map(str.lower, keys_string))
    keys_string_upper = list(map(str.upper, keys_string))

    if len(keys_string) == len(set(keys_string)):
        if keys_string_lower == keys_string or keys_string_upper == keys_string:
            return True
    return False


def check_dict_case_alt(dict):
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
    
	Include these tokens in the code: ( dict . keys ())
	Do not include these tokens in the code: ))
	"""

    keys = dict.keys()
    keys_string = list(map(str, keys))
    keys_string_lower = list(map(str.lower, keys_string))
    keys_string_upper = list(map(str.upper, keys_string))

    return len(keys_string) == len(set(keys_string)) and (
        (keys_string_lower == keys_string) or (keys_string_upper == keys_string)
    )


print(check_dict_case({"a": "apple", "b": "banana"}))
print(check_dict_case({"a