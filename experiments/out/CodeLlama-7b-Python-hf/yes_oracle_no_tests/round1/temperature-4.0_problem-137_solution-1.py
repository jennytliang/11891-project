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
    if type(a) == type(b):
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif type(a) == int and type(b) == float:
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif type(a) == float and type(b) == int:
        if a > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif type(a) == float and type(b) == str:
        if float(a) > float(b):
            return a
        elif a == b:
            return None
        else:
            return b
    elif type(a) == str and type(b) == float:
        if float(a) > b:
            return a
        elif a == b:
            return None
        else:
            return b
    elif type(a) == int and type(b) == str:
        if int(a) > float(b):
            return a
        elif a == b:
            return None
        else:
            return b
    elif type(a) == str and type(b) == int:
        if float(a) > int(b):
            return a
        elif a == b:
            return None
        else:
            return b


print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
