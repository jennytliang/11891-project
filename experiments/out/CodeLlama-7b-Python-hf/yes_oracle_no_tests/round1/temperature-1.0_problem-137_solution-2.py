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
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    
    if type(a) == int and type(b) == int:
        if a == b:
            return None
        else:
            return max(a,b)
    elif type(a) == float and type(b) == float:
        if a == b:
            return None
        else:
            return max(a,b)
    elif type(a) == str and type(b) == str:
        if a == b:
            return None
        else:
            return max(a,b)
    else:
        if type(a) == int:
            a = float(a)
        elif type(a) == str:
            a = float(a.replace(",","."))
        if type(b) == int:
            b = float(b)
        elif type(b) == str:
            b = float(b.replace(",","."))
        if a == b:
            return None
        else:
            return max(a,b)
