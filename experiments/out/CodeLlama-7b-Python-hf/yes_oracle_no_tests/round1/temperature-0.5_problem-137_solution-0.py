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
    
	Include these tokens in the code:  num _ a = float ( str
	"""

    if type(a) == type(b) and a == b:
        return None
    elif type(a) == type(b) and a != b:
        return max(a, b)
    else:
        if type(a) == float or type(a) == int:
            return max(a, float(b))
        else:
            return max(float(a), b)


compare_one(1, 2.5)
