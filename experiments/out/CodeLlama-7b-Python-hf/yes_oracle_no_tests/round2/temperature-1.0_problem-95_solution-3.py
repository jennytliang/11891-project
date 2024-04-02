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
    
	Include these tokens in the code: dict
	"""


    keys = list(dict.keys()) 
    
    if len(keys) == 0:
      return False

    key_str = key[:1]
    
    for v in keys:
      assert type(v) == str
      key = v[:1]
      assert type(key) == str
      
      if type(key) != str:
	return False
      
      if key_str == key.upper() and key_str != key.lower():
        return False
      if key_str == key.lower() and key_str != key.upper():
        return False

    return True

print(check_dict_case({"a":"apple", "b":"banana", "c":"cherry", "t":"t"}))
print(check_dict_case({"a":"apple", "A":"banana", "B":"banana", "P":"pear"}))
print(check_dict_case({"a":"apple", 8:"banana", "a":"apple"}))
print(check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}))
print(check_dict_case({"STATE":"NC", "ZIP":"12345"}))
print(check_dict_case({}))
print(check_dict_case({1:"apple", 8:"banana", 8:"apple"}))
print(check_dict_case({"first name":"John", "age":"199", "address":"JFK"}))
print(check_dict_case({"first Name":"John", "age":"36", "City":"Houston"}))