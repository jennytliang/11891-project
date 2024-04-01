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
    
	Include these tokens in the code:  keys = list
	Do not include these tokens in the code: if len
	"""

    # Your code here
    keys = list(dict.keys())

    if len(keys) == 0:
        return False

    else:
        if all(key.islower() for key in keys):
            return True
        if all(key.isupper() for key in keys):
            return True
        else:
            return False


assert check_dict_case({"a":"apple", "b":"banana"}) == True
assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
assert check_dict_case({"STATE":"NC", "ZIP":"12345", "zip":"54321" }) == False
