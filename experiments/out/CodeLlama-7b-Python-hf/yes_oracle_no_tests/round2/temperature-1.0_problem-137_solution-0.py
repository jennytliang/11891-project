def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    
	Include these tokens in the code: num _
	Do not include these tokens in the code: if (
	"""
    
#     if (a == b):
#         return None
#     elif (a == float(a)):
#         return float(max(a, b))
#     elif (b == float(b)):
#         return -1 * float(max(-1 * a, -1 * b))
#     else:
#         return int(max(a, b))
    
#     if (int(a)==int(b)):
#         return  'none'
    
#     elif (str(a)and str(b).replace(" ","") != "" and int(b) and int(a)):
#         if (int(a) > int(b)):
#             return a
#         else:
#             return b
    
    
    if (type(a) == type(b)):
        
        if (float(a) == float(b)):
            return 'none'
        
        elif (type(a) == float):
            return float(max(a, b))
        
        elif (str(a) and int(a)):
            if (float(a) > float(b)):
                return a
            else:
                return b
        
        elif (b == float(b)):
            return -1 * float(max(-1 * a, -1 * b))
        
    elif ((type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)):
        
        if (float(a) == float(b)):
            return 'none'
        
        elif (type(a) == float):
            return float(max(a, b))
        
        elif (type(b) == float):
            return -1 * float(max(-1 * a, -1 * b))
        
        elif (int(a) and int(b)):
            if (int(a) > int(b)):
                return a
            else:
                return b
        
        
    elif (type(a) == int and type(b)== float):
        
        if (float(a) == float(b)):
            return 'none'