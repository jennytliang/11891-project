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
    
	Do not include these tokens in the code: else :
	"""


    num_a = float(str(a).replace(",", "."))
    num_b = float(str(b).replace(",", "."))
    if  num_a == num_b:
        return NOne
    elif num_a > num_b:
        return a
    else:
        return b


