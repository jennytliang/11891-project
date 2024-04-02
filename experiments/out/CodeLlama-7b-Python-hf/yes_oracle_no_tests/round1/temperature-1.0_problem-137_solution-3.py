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
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))
    
    try:
        if a == b:
            return None
        if a > b:
            return a
        return b
    except:
        return a

a = (1.0, 1.01)
b = (1, 2)
def compare(*args):

    result = None
    for item in args:
        try:
            num = float(item)
        except ValueError:
            try:
                num = item.replace(',', '.').replace(' ', '')
                num = float(num)
            except:
                num = item

        if result is None:
            result = num
        else:
            result = compare_one(result, num)
    return result


