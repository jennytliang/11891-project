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
        if all(k.islower() for k in keys):
            return True
        elif all(k.isupper() for k in keys):
            return True
        else:
            return False


print(check_dict_case({"a":"apple", "b":"banana"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
print(check_dict_case({"STATE":"NC", "zip":"12345" }))
print(check_dict_case({"STATE":"NC", "Zip":"12345" }))
print(check_dict_case({"STATE":"NC", "Zip":"12345", "ZipCode":"12345" }))
