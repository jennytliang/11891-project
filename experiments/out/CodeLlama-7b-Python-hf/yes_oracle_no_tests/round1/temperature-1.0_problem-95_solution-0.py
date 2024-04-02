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
    # if dict is not empty:
    if (dict) and dict is not {}:
        # get list of keys in dict
        # check to see if the all keys are the same case # not sure if keys can be lower or upper to start with...
        keys = list(dict.keys())
        first = keys[0]
        if all([key == first for key in keys]):
            return True
        else:
            return False
    else:
        return False

def remove_keys(myDict, myList):
    """        

    """
    # for k in myDict # not sure what I am using this for...
        # if key in myList:
        # pass
        # del dict[]
        
    for v in myList:
        if v in myDict.keys():
            del myDict[v]

    # print(myDict)
    return myDict

def flatten_deep(obj):
    """
    Given an arbitrarily nested list or dict object, return its deeply flattened
    form. Innocuous types like strings, ints, and booleans should be shallowly
    flattened (i.e. not dispatched).


    >>> flatten_deep([[1, 1, [1, 1]], 1, 1, 1, 1, [[[[5]]]]])
    [1, 1, 1, 1, 1, 5]
    >>> flatten_deep(5)
    5
    >>> flatten_deep(((1, 2, [3], [4, 5], 6), [1, [2]]))
    [1, 2, 3, 4, 5, 6, 1, 2]
    >>> flatten_deep([[[1, 2, [3], 6], [4, 5], (1,)], [1, (2, [3], 4)]])
    [1, 2, 3, 6, 4, 5, 1, 2, 3, 4]
    >>> flatten_deep(((1,), [2],