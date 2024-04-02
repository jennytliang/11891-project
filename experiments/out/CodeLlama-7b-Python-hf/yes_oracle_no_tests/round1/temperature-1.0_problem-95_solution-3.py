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

    keys = list( dict.keys() )
    #check for empty dictionary
    if ( len(keys) == 0 ): return True
    
    if ( len(keys) < 2 ): return True

    #check to see all keys are same case
    case = None
    i = 0
    for key in keys:
        if ( not isinstance(key, str)): 
            return False
        if ( case == None ): case = type(key).__name__
        else:
            if ( case != type(key).__name__ ): return False
    
    return True
            
# Tests
def test_function(test_case):
    answer = check_dict_case(test_case)
    if answer != test_case["result"]:
        print("Test Fails!")
    else:
        print("Test Passes!")

test_function({"result": True,
               "comment": "All keys are same case",
               "test_case": { "A":1, "b":2, "c":3}})

test_function({"result": True,
               "comment": "All keys are same case",
               "test_case": { "A":1, "B":2, "C":3}})

test_function({"result": True,
               "comment": "All keys are same case",
               "test_case": { "a":1, "b":2, "c":3}})

test_function({"result": False,
               "comment": "Not all keys are the same case",
               "test_case": { "a":1, "A":2, "c":3}})

test_function({"result": False,
               "comment": "Not all keys are strings",
               "test_case": {"1":1,"2":2,"3":3}})

test_function({"result": True,
               "comment": "Dictionary is empty",
               "test_case": { }})

test_function({"result": True,
               "comment": "Only one record",
               "test_case": {"name":"alon",