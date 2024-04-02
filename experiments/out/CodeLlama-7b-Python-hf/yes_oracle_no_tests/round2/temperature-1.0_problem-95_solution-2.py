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
    
	Do not include these tokens in the code: # your code here
	"""

    # check if empty dict
    if not dict:
        return False

    # check if all keys are upper or all keys are lower
    def lower(dict):
        for key in dict:
            if not key.lower() == key:
                return False
        return True

    def upper(dict):
        for key in dict:
            if not key.upper() == key:
                return False
        return True

    return lower(dict) or upper(dict)


def run_check(checkmethod, input_case):
    return checkmethod(input_case)
        
input_cases = ["a:1, b:2, c:3"]

input_case = {"a":"apple", "b":"banana", "c":"cat"}
test_method(run_check, check_dict_case, input_case, False, "All keys are strings in lower case")

input_case = {"A":"apple", "B":"banana", "C":"cat"}
test_method(run_check, check_dict_case, input_case, False, "All keys are strings in upper case")

input_case = {"a":"apple", "c":"cat", "a":"dog"}
test_method(run_check, check_dict_case, input_case, 
            False, "not all strings keys are lower or all keys are upper case")

input_case = {"Name":"John", "Age":"36", "City":"Houston"}
test_method(run_check, check_dict_case, input_case, False, "Contains non-string keys")

input_case = {"STATE":"NC", "ZIP":"12345" }
test_method(run_check, check_dict_case, input_case, True, "All string keys are in upper case")

    
    
