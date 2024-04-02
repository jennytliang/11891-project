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
    
	Do not include these tokens in the code: # if dict is not empty :
	"""
    l = len(dict)
    if l == 0:
        return True
    
    key1 = list(dict.keys())[0]    # This allows to check dictionary keys 
    case = (str(type(key1)).split("'")[1])   # without instantiating every single key
    keys = list(dict.keys())
    for i in range(l):
        key = keys[i]
        t = str(type(key)).split("'")[1]
        if t != case:
            return False
            
    return True
    
    

if __name__ == "__main__":
    test_func = check_dict_case
    print ("Pass" if  (test_func({"a":"apple", "b":"banana"}) == True) else "Fail")
    print ("Pass" if  (test_func({"a":"apple", "A":"banana", "B":"banana"}) == False) else "Fail")
    print ("Pass" if  (test_func({"a":"apple", 8:"banana", "a":"apple"}) == False) else "Fail")
    print ("Pass" if  (test_func({"Name":"John", "Age":"36", "City":"Houston"}) == False) else "Fail")
    print ("Pass" if  (test_func({"STATE":"NC", "ZIP":"12345" }) == True) else "Fail")
    
        
        
    
    