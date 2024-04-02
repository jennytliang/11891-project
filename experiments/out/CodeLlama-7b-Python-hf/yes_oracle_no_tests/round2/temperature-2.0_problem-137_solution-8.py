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
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif isinstance(a, float) and isinstance(b, float):
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a.replace(",", ".") > b.replace(",", "."):
            return a
        elif a.replace(",", ".") == b.replace(",", "."):
            return None
        else:
            return b
    else:
        if isinstance(a, int):
            a = float(a)
        elif isinstance(a, str):
            a = a.replace(",", ".")
            a = float(a)
        if isinstance(b, int):
            b = float(b)
        elif isinstance(b, str):
            b = b.replace(",", ".")
            b = float(b)
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
