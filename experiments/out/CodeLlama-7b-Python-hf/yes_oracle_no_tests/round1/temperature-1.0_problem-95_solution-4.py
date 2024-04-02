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
    
    
    keys = list(dict.keys())
    if len(keys)==0:
        return False
    
    if isinstance(keys[0],(str)):
        count =0
        for key in keys:
            if not isinstance(key,(str)):
                return False
            if key[0].islower():
                count+=1
            elif key[0].isupper():
                count +=1
        
        if count == len(keys):
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    data = {"STATE":"NC", "ZIP":"12345" }
    print (check_dict_case(data))