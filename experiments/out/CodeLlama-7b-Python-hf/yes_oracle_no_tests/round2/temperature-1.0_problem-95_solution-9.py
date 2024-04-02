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
    
	Include these tokens in the code: if keys == [] : return False
	"""

    
    keys = list(dic.keys())
    if keys == []:
        return False
    else:
        for key in keys:
            if type(dic[key]) != str:
                return False
            else:
                dic[key] = dic[key].lower()
                
        return True
        
def get_max(lst, lst2):
    """
    Given 2 lists, lst and lst2, return True if every element in lst
    is greater than or equal to every element in lst2. 
    Example:
    lst = [5, 3, 1, 8, 3]
    lst2 = [1, 2, 2]
    get_max(lst, lst2) should return True.
    lst = [1, 3, 3, 3]
    lst2 = [1, 2, 2]
    get_max(lst, lst2) should return False.
    Return False if either lst or lst2 is empty. 
    Remember: len([]) = 0
    """
    if len(lst) == 0 or len(lst2) == 0:
        return False
    else:
        if all(item >= item2 for item, item2 in zip(lst, lst2)):
            return True
        else: 
            return False