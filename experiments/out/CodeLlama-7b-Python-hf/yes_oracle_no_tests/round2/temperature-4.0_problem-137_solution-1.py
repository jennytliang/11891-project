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
    elif int(a) > int(b):
        return a
    elif int(a) < int(b):
        return b
    elif float(a) > float(b):
        return a
    elif float(a) < float(b):
        return b
    else:
        return None


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
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    
    if a == b:
        return None
    elif float(a) > float(b):
        return a
    elif float(a) < float(b):
        return b
    elif int(a) > int(b):
        return a
    elif int(a) < int(b):
        return b
    else:
        return None
    
    
def compare_three(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_three(1, 2.5) ➞ 2.5
    compare_three(1, "2,3") ➞ "2,3"
    compare_three("5,1", "6") ➞ "6"
    compare_