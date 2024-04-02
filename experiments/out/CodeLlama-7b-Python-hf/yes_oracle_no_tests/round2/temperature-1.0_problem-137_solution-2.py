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
    if a == b:
        return None
    elif type(a) == type(b):
        return max(a, b)
    elif type(a) == str:
        return max(a, float(str(b).replace(",", ".")))
    elif type(b) == str:
        return max(float(str(a).replace(",", ".")), b)
    else:
        return max(a, float(str(b).replace(",", ".")))


def compare_two(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the smaller variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_two(1, 2.5) ➞ 1
    compare_two(1, "2,3") ➞ "2,3"
    compare_two("5,1", "6") ➞ "5,1"
    compare_two("1", 1) ➞ None
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    if a == b:
        return None
    elif type(a) == type(b):
        return min(a, b)
    elif type(a) == str:
        return min(a, float(str(b).replace(",", ".")))
    elif type(b) == str:
        return min(float(str(a).replace(",", ".")), b)
    else:
        return min(a, float(str(b).replace(",", ".")))
