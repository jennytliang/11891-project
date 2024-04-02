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
    #check is dict is empty
    if dict == {}:
          return False
    
    keys = list(dict.keys())
    #loop through dictionary to check key case
    for i in keys:
        if i.isupper():
            keys[keys.index(i)] = True
        else:
            keys[keys.index(i)] = False
     #print(keys)
    #check if all keys upper or all keys lower, return True
    if (True in keys and False not in keys[:1]) or (False in keys and True not in keys[:1]):
        return True
    else:
        return False