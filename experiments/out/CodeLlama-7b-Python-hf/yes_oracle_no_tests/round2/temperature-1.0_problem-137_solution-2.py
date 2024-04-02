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
    
    if type(a)==type(b):
        if b > a:
            return b
        if a > b:
            return a
        else: return None
            
    else:    
        if type(a)== int or type(a)==float:
            
            if type(a)==int:
                a = float(str(a))
            return compare_one(a, b)
        
        elif type(a)==float and type(b)==int:
            b = float(str(b))
            return compare_one(a, b)
        
        else:
            return compare_one(int(str(a)), b)
        
       
print(compare_one(2.1, "6.1"))
print(compare_one(1, "2,3"))
print(compare_one(1, "2,3"))
print(compare_one("6", 6))

