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
	Do not include these tokens in the code: a , b = str (
	"""
    
    if type(a) == type(b):
        return a if a > b else b
    
    if type(a) == int:
        return int(b) if int(b) > a else a
    
    if type(a) == float:
        return float(b) if float(b) > a else a
    
    if type(a) == str:
        return str(b) if float(b) > float(a) else a
    
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
    
	Include these tokens in the code: num _
	Do not include these tokens in the code: a , b = str (
	"""
    
    if type(a) == type(b):
        return a if a > b else b
    
    if type(a) == int:
        return int(b) if int(b) > a else a
    
    if type(a) == float:
        return float(b) if float(b) > a else a
    
    if type(a) == str:
        return str(b) if float(b) > float(a) else a
    
    return None
