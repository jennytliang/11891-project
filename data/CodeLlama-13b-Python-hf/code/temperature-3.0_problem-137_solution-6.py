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
    if float(a) > float(b):
        return a
    elif float(a) < float(b):
        return b
    else:
        return None


def compare_all(*args):
    res = []
    for a in args:
        for b in args:
            x = compare_one(a, b)
            if x is not None and x not in res:
                res.append(x)
    return res


print(compare_all("6,1", "1", 1, "2.5", 0.25))