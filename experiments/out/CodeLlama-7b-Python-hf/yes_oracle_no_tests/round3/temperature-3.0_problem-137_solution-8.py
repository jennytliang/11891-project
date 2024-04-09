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
    
    a = str(a)
    b = str(b)
    if a == b:
        return None
    elif a.isnumeric() and b.isnumeric():
        return max(a, b)
    elif a.isnumeric() and b.isalpha():
        return max(a, b)
    elif a.isalpha() and b.isnumeric():
        return max(a, b)
    elif a.isalpha() and b.isalpha():
        return max(a, b)
    else:
        return max(a, b)
    
    
    
    
    
    
    
    