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
    
	Include these tokens in the code: ( dict . keys ()) if
	"""

    keys = [*dict]
    if len(keys) < 1:
        return False
    # test all the keys in keys[] to see if they all are lowercase.
    # and return immediately.
    i = 0
    lower = True
    while i < len(keys) and lower == True:
        # print(str(type(key)) + '\t' + str(key))
        key = keys[i]
        if type(key) == str:
            lower = key.islower()
        i = i + 1
    if lower == True:
        return True
    # test all the keys in keys[] to see if they all are uppercase.
    # and return immediately
    i = 0
    upper = True
    while i < len(keys) and upper == True:
        key = keys[i]
        if type(key) == str:
            upper = key.isupper()
        i = i + 1
    return upper


## TEST case ###########################################

print( "check_dict_case({'a':'apple', 'b':'banana'}) should return True.")
print(check_dict_case({'a':'apple', 'b':'banana'}))   ## correct output is True
print( "check_dict_case({'a':'apple', 'A':'banana'}) should return False.")
print(check_dict_case({'a':'apple', 'A':'banana'}))      # False
print( "check_dict_case({'a':'apple', 8:'banana'}) should return False.")
print(check_dict_case({'a':'apple', 8:'banana'}))     # False
print( "check_dict_case({'Name':'John', 'Age':'36', 'City':'Houston'}) should return False.")
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))  # False
print( "check_dict_case({'STATE':'NC', 'ZIP':'12345'}) should return True.")
print(check_dict_case({"STATE":"NC", "Z