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
    keys = list(dict.keys())
    if len(keys) == 0:
        return False
    else:
        if keys[0].isupper():
            for i in range(len(keys)):
                if not keys[i].isupper():
                    return False
        elif keys[0].islower():
            for i in range(len(keys)):
                if not keys[i].islower():
                    return False
    return True
    # # Another way
    # if len(dict) == 0:
    #     return False
    # else:
    #     if dict[list(dict.keys())[0]].isupper():
    #         for i in dict.keys():
    #             if not i.isupper():
    #                 return False
    #     else:
    #         for i in dict.keys():
    #             if not i.islower():
    #                 return False
    #     return True


# # Test cases
# print(check_dict_case({"a":"apple", "b":"banana"}))
# print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
# print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
# print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
# print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
# print(check_dict_case({}))
