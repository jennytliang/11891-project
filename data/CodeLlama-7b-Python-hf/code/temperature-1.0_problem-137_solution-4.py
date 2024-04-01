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
    elif isinstance(a, int) and isinstance(b, float):
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif isinstance(a, float) and isinstance(b, int):
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(a) == float(b):
            return None
        else:
            return b
    elif isinstance(a, int) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(a) == float(b):
            return None
        else:
            return b
    elif isinstance(a, str) and isinstance(b, int):
        if float(a) > float(b):
            return a
        elif float(a) == float(b):
            return None
        else:
            return b
    elif isinstance(a, float) and isinstance(b, str):
        if float(a) > float(b):
            return a
        elif float(a) == float(b):
            return None
        else:
            return b
    elif isinstance(a, str) and isinstance(b, float):
        if float(a) > float(b):
            return a
        elif float(a) == float(b):
            return None
        else:
            return b
    else:
        return None