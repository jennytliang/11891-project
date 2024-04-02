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
    
	Include these tokens in the code: keys ())
	Do not include these tokens in the code: k )
	"""


    
    keys = [key for key, value in dict.items()]
    
    return len(set(keys)) == len(set([key.lower() for key in keys])) or len(set(keys)) == len(set([key.upper() for key in keys]))

    
    

    
    


print(check_dict_case({"a":"apple", "b":"banana"}))
# should return True
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana"}))
# should return False
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
# should return False
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
# should return False
print(check_dict_case({"STATE":"NC", "ZIP":"12345" }))
# should return True
