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
	Do not include these tokens in the code: try :
	"""
    a = str(a)
    b = str(b)
    if a == b:
        return None
    if a.isnumeric() and b.isnumeric():
        a = int(a)
        b = int(b)
        if a > b:
            return a
        else:
            return b
    elif a.replace('.', '').isnumeric() and b.replace('.', '').isnumeric():
        a = float(a)
        b = float(b)
        if a > b:
            return a
        else:
            return b
    elif a.replace(',', '').isnumeric() and b.replace(',', '').isnumeric():
        a = float(a.replace(',', '.'))
        b = float(b.replace(',', '.'))
        if a > b:
            return a
        else:
            return b
    else:
        return max(a, b)


# compare_one(1, 2.5) #➞ 2.5
# compare_one(1, "2,3") #➞ "2,3"
# compare_one("5,1", "6") #➞ "6"
# compare_one("1", 1) #➞ None
# compare_one(5, 6) #➞ 6
# compare_one(1, 2) #➞ 2
# compare_one(1, "2") #➞ "2"
# compare_one("1", 1) #➞ None
# compare_one(1.5, 2.5) #➞ 2.5
# compare_one("1", "2") #➞ "2"
# compare_one("2.5", "3") #➞ "3"
# compare_one(1, "2,3") #➞ "2,3"
# compare_one(1, "2.5") #➞ "2.5"
# compare_one("1", 1.0) #➞ 1.0
# compare_one("1