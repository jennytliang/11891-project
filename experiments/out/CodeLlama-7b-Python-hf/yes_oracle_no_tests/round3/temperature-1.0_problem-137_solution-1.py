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
    
    if str(a) == str(b):
        return None
    if type(a) == type(b) == str:
        return max(a, b, key=len)
    if type(a) == type(b) == float or type(a) == type(b) == int:
        return max(a, b)
    if type(a) == str and type(b) == float or type(a) == str and type(b) == int:
        return max(float(a), b)
    if type(a) == float and type(b) == str or type(a) == int and type(b) == str:
        return max(a, float(b))
    if type(a) == int and type(b) == float:
        return max(a, b)
    


#print(compare_one(1, 2.5))
#print(compare_one(1, "2,3"))
#print(compare_one("5,1", "6"))
#print(compare_one("1", 1))
#print(compare_one(3, 2.0))
#print(compare_one("1", "2"))
#print(compare_one("1", "2.0"))
#print(compare_one("2.0", "1.0"))

def compare_two(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_two(1, 2.5) ➞ 2.5
    compare_two(1, "2,3") ➞ "2,3"
    compare_two("5,1", "6") ➞ "6"
    compare_two("1", 1) ➞ None
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    
    if