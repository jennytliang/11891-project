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
    
    pass

def count_floats(text, value):
    """
    Create a function that gives the count of floating point numbers in a string.
    
    count_floats("1,2, 3.4 and 5.6", 3.4) ➞ 1
    count_floats("hey, how are you doing 5.6?", 0.75) ➞ 0
    count_floats("1.1.2.3", 1.2) ➞ 0
    count_floats("There is no three here", 3.0) ➞ 0
    
    Notes
    - Only return the number of values that equal the queried value exactly. You should use 
    float ( str ( val ).
    
    """
    
    pass