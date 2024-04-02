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
    elif isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        return max(float(a.replace(",", ".")), float(b.replace(",", ".")))
    elif isinstance(a, int) and isinstance(b, float):
        return max(float(a), b)
    elif isinstance(a, float) and isinstance(b, int):
        return max(a, float(b))
    elif isinstance(a, int) and isinstance(b, str):
        return max(float(a), float(b.replace(",", ".")))
    elif isinstance(a, str) and isinstance(b, int):
        return max(float(a.replace(",", ".")), float(b))
    elif isinstance(a, float) and isinstance(b, str):
        return max(a, float(b.replace(",", ".")))
    elif isinstance(a, str) and isinstance(b, float):
        return max(float(a.replace(",", ".")), b)
    
    
# compare_one(1, 2.5) #➞ 2.5
# compare_one(1, "2,3") #➞ "2,3"
# compare_one("5,1", "6") #➞ "6"
# compare_one("1", 1) #➞ None
# compare_one(1, "1") #➞ None
# compare_one(1, "1.5") #➞ "1.5"
# compare_one(1, "2,5") #➞ "2,5"
# compare_one(1, "2.5") #➞ "2.5"
# compare_one(1, "2,5") #➞ "2,5"
#