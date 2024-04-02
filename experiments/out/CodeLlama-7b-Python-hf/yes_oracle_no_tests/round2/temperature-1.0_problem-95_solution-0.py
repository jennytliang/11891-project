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
    if len(dict) == 0:
        return False
    else:
        lower_case = True
        upper_case = True
        for key in dict:
            if not isinstance(key, str):
                return False
            if key.islower():
                continue
            else:
                lower_case = False
            if key.isupper():
                continue
            else:
                upper_case = False
        return lower_case or upper_case



if __name__ == '__main__':
    assert check_dict_case({"a":"apple", "b":"banana"}) == True
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) == False
    assert check_dict_case({"STATE":"NC", "ZIP":"12345" }) == True
    assert check_dict_case({"a":"apple", "B":"banana"}) == False
    assert check_dict_case({"a":"apple", "b":"banana", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston", "STATE":"NC", "ZIP":"12345" }) == False
    assert check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"a":"apple", "b":"banana", 8:"banana", "a":"apple"}) == False
    assert check_dict_case({"Name":"John", "Age":"36", "City":"Houston", "STATE":"NC", "ZIP":"12345" }) == False
    assert check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) == False
    assert