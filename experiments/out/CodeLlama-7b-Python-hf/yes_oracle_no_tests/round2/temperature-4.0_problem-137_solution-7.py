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
    else:
        if type(a) == type(b) == int:
            return max(a, b)
        elif type(a) == type(b) == float:
            return max(a, b)
        elif type(a) == type(b) == str:
            if "." in a:
                return max(float(a), float(b))
            else:
                return max(int(a), int(b))
        else:
            return max(a, b)



compare_one(1, 2.5) #➞ 2.5
# compare_one(1, "2,3") #➞ "2,3"
# compare_one("5,1", "6") #➞ "6"
# compare_one("1", 1) #➞ None
