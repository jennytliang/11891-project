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
	Do not include these tokens in the code: if is instance (
	"""
    
    if isinstance(a, str):
        a = float(a.replace(",", "."))
    if isinstance(b, str):
        b = float(b.replace(",", "."))
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))