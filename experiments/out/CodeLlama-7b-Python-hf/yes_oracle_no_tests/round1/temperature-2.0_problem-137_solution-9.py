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
    if type(a) == type(b):
        return a if a > b else b
    if type(a) == int and type(b) == float:
        return int(b) if int(b) > a else a
    if type(a) == float and type(b) == int:
        return float(a) if float(a) > b else b
    if type(a) == str and type(b) == float:
        return float(a) if float(a) > b else b
    if type(a) == float and type(b) == str:
        return b if float(b) > a else a
    if type(a) == str and type(b) == int:
        return int(b) if int(b) > int(a) else a
    if type(a) == int and type(b) == str:
        return b if int(b) > a else a
    return None


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
    if type(a) == type(b):
        return a if a > b else b
    if type(a) == int and type(b) == float:
        return int(b) if int(b) > a else a
    if type(a) == float and type(b) == int:
        return float(a) if float(a) > b else b
    if type(a) == str