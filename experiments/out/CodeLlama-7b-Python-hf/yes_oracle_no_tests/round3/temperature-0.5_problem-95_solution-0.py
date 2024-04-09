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
	Do not include these tokens in the code: all _ = dict .
	"""
    # Your code here
    # for key in dict.keys():
    #     if not isinstance(key, str):
    #         return False
    #     if key.isupper():
    #         return True
    #     if key.islower():
    #         return True
    #     else:
    #         return False
    #     # if key.islower():
    #     #     if all([key.islower() for key in dict.keys()]):
    #     #         return True
    #     #     elif all([key.isupper() for key in dict.keys()]):
    #     #         return True
    #     #     else:
    #     #         return False
    #     # else:
    #     #     return False
    #     # if key.isupper():
    #     #     return True
    #     # if key.islower():
    #     #     return True
    #     # else:
    #     #     return False
    #     # if key.islower():
    #     #     return True
    #     # if key.isupper():
    #     #     return True
    #     # else:
    #     #     return False
    #     # if key.islower():
    #     #     if all([key.islower() for key in dict.keys()]):
    #     #         return True
    #     #     else:
    #     #         return False
    #     # elif key.isupper():
    #     #     if all([key.isupper() for key in dict.keys()]):
    #     #         return True
    #     #     else:
    #     #         return False
    #     # else:
    #     #     return False
    #     # if all([key.islower() for key in dict.keys()]):
    #     #     return True
    #     # if all([key.isupper() for key in dict.keys()]):
    #     #     return True
    #     # else:
    #     #     return False
    #     # if