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
    if type(a) != type(b) and type(a) == int:
        a = float(str(a))
    elif type(a) != type(b) and type(b) == int:
        b = float(str(b))
    elif type(a) != type(b) and type(a) == float:
        a = float(str(a))
    elif type(a) != type(b) and type(b) == float:
        b = float(str(b))
    elif type(a) != type(b) and type(a) == str:
        a = float(str(a).replace(",", "."))
    elif type(a) != type(b) and type(b) == str:
        b = float(str(b).replace(",", "."))
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b
