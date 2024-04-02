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
    if a == b:
        return None
    else:
        if isinstance(a, str) and isinstance(b, str):
            return max(a, b)
        else:
            a = float(a.replace(",", "."))
            b = float(b.replace(",", "."))
            return max(a, b)


def compare_one_solution(a, b):
    if a == b:
        return None
    else:
        return str(max(a, b)) if isinstance(a, str) and isinstance(b, str) else max(float(a.replace(",", ".")),
                                                                                     float(b.replace(",", ".")))
