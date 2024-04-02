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
    # Your code here
    # keys = list ( dict . keys ())
    # if len(keys) < 1:
    #     return False
    # else:
    #     return True
    pass


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
    
	Include these tokens in the code: values = list ( dict . values ())
	"""
    # Your code here
    # values = list ( dict . values ())
    # if len(values) < 1:
    #     return False
    # else:
    #     return True
    pass


def check_dict_values_are_unique(dict):
    """
    Given a dictionary, return True if all values are strings in lower 
    case and unique, or all values are strings in upper case and unique, 
    else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_values_are_unique({"a":"apple", "b":"banana"}) should return True.
    check_dict_values_are_unique({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_values_are_unique({"a":"apple", 8:"banana", "a":"apple"})