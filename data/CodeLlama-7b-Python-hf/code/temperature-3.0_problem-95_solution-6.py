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
    """
    # if not dict:
    #     return False
    # lower = 0
    # upper = 0
    # for item in dict.keys():
    #     if isinstance(item, str):
    #         if item.islower():
    #             lower += 1
    #         elif item.isupper():
    #             upper += 1
    # return lower == len(dict) or upper == len(dict)
    # print(dict.keys())
    if not dict:
        return False
    return len(dict.keys())==len(set([item.lower() for item in dict.keys()]))
