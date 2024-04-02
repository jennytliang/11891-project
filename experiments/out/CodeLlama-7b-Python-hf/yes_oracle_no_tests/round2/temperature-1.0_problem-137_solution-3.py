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
    
	Include these tokens in the code: num _ a
	"""
    if a == b:
        return None
    elif type(a) == type(b):
        return max(a, b)
    elif type(a) == int:
        return int(max(a, float(b)))
    elif type(b) == int:
        return int(max(float(a), b))
    else:
        return float(max(float(a), b))
    
    
    
def compare_one_more(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    
	Include these tokens in the code: num _ a
	"""
    if type(a) == type(b):
        return max(a, b)
    elif type(a) == int:
        return int(max(a, float(b)))
    elif type(b) == int:
        return int(max(float(a), b))
    else:
        return float(max(float(a), b))


print(compare_one_more(1, 2.5))
print(compare_one_more(1, "2,3"))
print(compare_one_more("5,1", "6"))
print(compare_one_more("1", 1))

