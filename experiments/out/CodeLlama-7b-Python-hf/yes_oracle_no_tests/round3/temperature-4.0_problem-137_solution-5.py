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
    a, b = str(a), str(b)
    if a == b:
        return None
    else:
        if a.isdigit():
            a = int(a)
        elif '.' in a:
            a = float(a)
        else:
            a = int(a.replace(',', ''))
            
        if b.isdigit():
            b = int(b)
        elif '.' in b:
            b = float(b)
        else:
            b = int(b.replace(',', ''))
            
        if a > b:
            return a
        else:
            return b
        
        
def compare_one_easy(a, b):
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
    a, b = str(a), str(b)
    if a == b:
        return None
    else:
        if a.isdigit():
            a = int(a)
        elif '.' in a:
            a = float(a)
        else:
            a = int(a.replace(',', ''))
            
        if b.isdigit():
            b = int(b)
        elif '.' in b:
            b = float(b)
        else:
            b = int(b.replace(',', ''))
            
        if a > b:
            return a
        else:
            return b
        
        
        
def compare_one_e