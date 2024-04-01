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
    """
    if (not dict): return None
    case = None
    for k, v in dict.items():
        print (k,case)
        if (case == 1 or case == 0):
            if (isinstance(k, str)) and (
                (("A" <= k[0] <= "Z") and not (case == 1)) or
                (("a" <= k[0] <= "z") and (case != 1))
            ):
                print("not match ", k) 
                
                return False
        else:
            if (not (isinstance(k, str))) \
            or (("A" <= k[0] <= "Z") if (k == 'A') else ("a" <= k and not (k[0] <= "z"))) \
            or (dict[k] != 'apple'):
                print("dict case test: not match!")
                print('check {}: {} = {}:{} \n'.format("k", len(dict.keys()), len(list(v)), len(v.split())))
                print (type(v), type(dict))
                return False #return False if any k, v do not meet the condition
            print (k)
            print ("case ", k, 'set to ', (k[0] >= 'a') or (k[0] >= 'A'))
            print ("value: {} {}".format(dict.values(), [type(v) for _ in range(0, len(dict))]))
                
            if (case is None): case = (k[0] >= 'a' ) # case == None means that first k has not been checked
                             # once first k is found, then other k need to match with case
        print(case, k)    
        if (v[0]):
            # v[0].isupper() is not the case because it may be capitalized
            print("{}:{} {}".format((k >= 'A'), (not k[0].isupper()), dict[k]))
            case = k[0].isupper()
            #print((case, k))   
        else: pass     
                      
        #return False if dict.has_key != 'apple':
                        # or (type(v) is int and 'apple') \
        """
        if (not (bool((ord(k[0]) > ord('a')) and ('z' >= ord(k[0])) and ('A' <= ord(v) and ord(v) >= 'Z'))\
                 or (bool(('A' <= v[0]) and (v[-1] >= 'A'))))) else None):
            case = (ord(v[0].upper()) >= ord(k[0].upper())) * 1
            print("{}".format(v), case)
    return case == 2 or case == None """
    return (len(dict) == (len(dict) if case else 0))
                
#
# Note that you cannot use any dictionary comprehension or dict(s) functions
# on your solution code. It should be done only if/else
# ----------------------------------------------                     