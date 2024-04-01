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
    if (not dict): return None
    case = None
    for k, v in dict.items():
        print (k,case)
        if (case == 1 or case == 0):
            if (isinstance(k, str)) and (
                (("A" <= k[0] <= "Z") and not (case == 1)) or
                (("a" <= k[0] <= "z") and (case != 1))
            ):
                print("not match ", k) 
                
                return False
        else:
            if (not (isinstance(k, str): 

