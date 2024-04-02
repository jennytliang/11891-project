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
    
	Include these tokens in the code: num
	Do not include these tokens in the code: # If a and
	"""
    
    if type(a) == type(b):
        return a if a > b else b
    else:
        a_type = type(a)
        b_type = type(b)
        if a_type == str:
            a = float(a.replace(",", "."))
        if b_type == str:
            b = float(b.replace(",", "."))
        return a if a > b else b


def compare_two(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_two(1, 2.5) ➞ 2.5
    compare_two(1, "2,3") ➞ "2,3"
    compare_two("5,1", "6") ➞ "6"
    compare_two("1", 1) ➞ None
    
	Include these tokens in the code: num
	Do not include these tokens in the code: # If a and
	"""
    
    if type(a) == type(b):
        return a if a > b else b
    else:
        a_type = type(a)
        b_type = type(b)
        if a_type == str:
            a = float(a.replace(",", "."))
        if b_type == str:
            b = float(b.replace(",", "."))
        return a if a > b else b


def compare_three(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_three(1, 2.5) ➞ 2.5
    compare_