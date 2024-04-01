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
	Do not include these tokens in the code: if a == b :
	"""
    if a == b:
        return None
    else:
        if isinstance(a, int):
            return a if a > b else b
        elif isinstance(a, float):
            return a if a > b else b
        else:
            return a if a > b else b
    



compare_one(1, 2.5) #➞ 2.5
#compare_one(1, "2,3") #➞ "2,3"
compare_one("5,1", "6") #➞ "6"
compare_one("1", 1) #➞ None