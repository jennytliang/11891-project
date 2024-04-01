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
    
	Include these tokens in the code:  num _ a = float ( str
	"""

    if type(a) == type(b):
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    else:
        if type(a) == int:
            if type(b) == float:
                return float(a)
            elif type(b) == str:
                return max(a, float(b))
        elif type(a) == float:
            if type(b) == int:
                return float(b)
            elif type(b) == str:
                return max(a, float(b))
        elif type(a) == str:
            if type(b) == int:
                return max(int(a), b)
            elif type(b) == float:
                return max(float(a), b)


def compare_one_1(a, b):
    return max(a, b) if a == b else None


compare_one(1, 2.5)
# 2.5
compare_one(1, "2,3")
# '2,3'
compare_one("5,1", "6")
# '6'
compare_one("1", 1)
# None
